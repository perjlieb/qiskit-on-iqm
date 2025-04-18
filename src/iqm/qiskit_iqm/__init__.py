# Copyright 2022-2025 Qiskit on IQM developers
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
"""Qiskit adapter for IQM's quantum computers.
"""
import sys
from warnings import warn

from qiskit import __version__ as qiskit_version

from iqm.qiskit_iqm.fake_backends import IQMErrorProfile, IQMFakeAdonis, IQMFakeAphrodite, IQMFakeApollo, IQMFakeDeneb
from iqm.qiskit_iqm.fake_backends.iqm_fake_backend import IQMFakeBackend
from iqm.qiskit_iqm.iqm_circuit import IQMCircuit
from iqm.qiskit_iqm.iqm_job import IQMJob
from iqm.qiskit_iqm.iqm_move_layout import generate_initial_layout
from iqm.qiskit_iqm.iqm_naive_move_pass import IQMNaiveResonatorMoving, transpile_to_IQM
from iqm.qiskit_iqm.iqm_provider import IQMBackend, IQMProvider, __version__
from iqm.qiskit_iqm.iqm_transpilation import IQMOptimizeSingleQubitGates, optimize_single_qubit_gates
from iqm.qiskit_iqm.move_gate import MoveGate
from iqm.qiskit_iqm.transpiler_plugins import *

warn(
    DeprecationWarning(
        "The qiskit-iqm package is deprecated and new versions of Qiskit on IQM will be published as part of "
        "iqm-client. Please uninstall qiskit-iqm and install iqm-client[qiskit] to get the newest version."
    )
)
