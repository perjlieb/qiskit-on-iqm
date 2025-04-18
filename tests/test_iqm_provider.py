# Copyright 2022-2024 Qiskit on IQM developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Testing IQMProvider.
"""
from importlib.metadata import version
import uuid

from mockito import ANY, matchers, mock, when
import pytest
from qiskit import QuantumCircuit
import requests

from iqm.iqm_client import IQMClient, RunRequest, RunResult, RunStatus
from iqm.qiskit_iqm.iqm_provider import IQMBackend, IQMFacadeBackend, IQMProvider
from tests.utils import get_mock_ok_response


@pytest.fixture
def circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(5)
    circuit.cz(0, 1)
    return circuit


@pytest.fixture
def run_request():
    run_request = mock(RunRequest)
    run_request.circuits = []
    run_request.shots = 1
    return run_request


def test_get_backend(linear_3q_architecture):
    url = 'http://some_url'
    when(IQMClient).get_dynamic_quantum_architecture(None).thenReturn(linear_3q_architecture)
    when(requests).get('http://some_url/info/client-libraries', headers=matchers.ANY, timeout=matchers.ANY).thenReturn(
        get_mock_ok_response({'iqm-client': {'name': 'IQM Client', 'min': '0.0', 'max': '999.0'}})
    )

    provider = IQMProvider(url)
    backend = provider.get_backend()

    assert isinstance(backend, IQMBackend)
    assert backend.client._api.iqm_server_url == url
    assert backend.num_qubits == 3
    assert set(backend.coupling_map.get_edges()) == {(0, 1), (1, 2)}
    assert backend._calibration_set_id == linear_3q_architecture.calibration_set_id


def test_client_signature(adonis_architecture):
    url = 'http://some_url'
    provider = IQMProvider(url)
    when(requests).get('http://some_url/info/client-libraries', headers=matchers.ANY, timeout=matchers.ANY).thenReturn(
        get_mock_ok_response({'iqm-client': {'name': 'IQM Client', 'min': '0.0', 'max': '999.0'}})
    )
    when(requests).get(
        'http://some_url/api/v1/calibration/default/gates', headers=matchers.ANY, timeout=matchers.ANY
    ).thenReturn(get_mock_ok_response(adonis_architecture.model_dump(mode='json')))
    backend = provider.get_backend()
    version_string = version('qiskit-iqm')
    assert f'qiskit-iqm {version_string}' in backend.client._signature


def test_get_facade_backend(adonis_architecture):
    url = 'http://some_url'
    when(IQMClient).get_dynamic_quantum_architecture(None).thenReturn(adonis_architecture)
    when(requests).get('http://some_url/info/client-libraries', headers=matchers.ANY, timeout=matchers.ANY).thenReturn(
        get_mock_ok_response({'iqm-client': {'name': 'IQM Client', 'min': '0.0', 'max': '999.0'}})
    )

    provider = IQMProvider(url)
    backend = provider.get_backend('facade_adonis')

    assert isinstance(backend, IQMFacadeBackend)
    assert backend.client._api.iqm_server_url == url
    assert backend.num_qubits == 5
    assert set(backend.coupling_map.get_edges()) == set(backend.target.build_coupling_map())


def test_get_facade_backend_raises_error_non_matching_architecture(linear_3q_architecture):
    url = 'http://some_url'

    when(IQMClient).get_dynamic_quantum_architecture(None).thenReturn(linear_3q_architecture)
    when(requests).get('http://some_url/info/client-libraries', headers=matchers.ANY, timeout=matchers.ANY).thenReturn(
        get_mock_ok_response({'iqm-client': {'name': 'IQM Client', 'min': '0.0', 'max': '999.0'}})
    )

    provider = IQMProvider(url)
    with pytest.raises(ValueError, match='Quantum architecture of the remote quantum computer does not match Adonis.'):
        provider.get_backend('facade_adonis')


def test_facade_backend_raises_error_on_remote_execution_fail(adonis_architecture, circuit, run_request):
    url = 'http://some_url'
    result = {
        'status': 'failed',
        'measurements': [],
        'metadata': {
            'request': {
                'shots': 1024,
                'circuits': [
                    {
                        'name': 'circuit',
                        'instructions': [{'name': 'measure', 'qubits': ['0'], 'args': {'key': 'm1'}}],
                    }
                ],
            }
        },
    }
    result_status = {'status': 'failed'}

    when(IQMClient).get_dynamic_quantum_architecture(None).thenReturn(adonis_architecture)
    when(IQMClient).create_run_request(...).thenReturn(run_request)
    when(IQMClient).submit_run_request(...).thenReturn(uuid.uuid4())
    when(IQMClient).get_run(ANY(uuid.UUID)).thenReturn(RunResult.from_dict(result))
    when(IQMClient).get_run_status(ANY(uuid.UUID)).thenReturn(RunStatus.model_validate(result_status))
    when(requests).get('http://some_url/info/client-libraries', headers=matchers.ANY, timeout=matchers.ANY).thenReturn(
        get_mock_ok_response({'iqm-client': {'name': 'IQM Client', 'min': '0.0', 'max': '999.0'}})
    )

    provider = IQMProvider(url)
    backend = provider.get_backend('facade_adonis')

    with pytest.raises(RuntimeError, match='Remote execution did not succeed'):
        backend.run(circuit)
