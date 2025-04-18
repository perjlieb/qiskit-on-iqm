=========
Changelog
=========

Version 18.0
============

* Deprecate the ``qiskit-iqm`` package. New versions of Qiskit on IQM are published as part of iqm-client.
  `#159 <https://github.com/iqm-finland/qiskit-on-iqm/pull/159>`_

Version 17.8
============

* Bugfix: Transpiler now supports symbolic gates again. `#158 <https://github.com/iqm-finland/qiskit-on-iqm/pull/158>`_

Version 17.7
============

* Added Garnet backend so that it can be used in simulations.
  `#156 <https://github.com/iqm-finland/qiskit-on-iqm/pull/156>`_

Version 17.6
============

* Fix unit tests compatibility with latest ``iqm-client``.
  `#157 <https://github.com/iqm-finland/qiskit-on-iqm/pull/157>`_

Version 17.5
============

* Provider tolerates unrecognized job statuses from the server to ensure forward compatibility.
  `#155 <https://github.com/iqm-finland/qiskit-on-iqm/pull/155>`_

Version 17.4
============

* Bugfix: The ``delay`` operation is now accepted by the standard transpiler.
  `#151 <https://github.com/iqm-finland/qiskit-on-iqm/pull/151>`_

Version 17.3
============

* Use the native ``reset`` operation to implement :class:`qiskit.circuit.Reset`.
  `#148 <https://github.com/iqm-finland/qiskit-on-iqm/pull/148>`_

Version 17.2
============

* Bugfix in :class:`IQMOptimizeSingleQubitGates`` where the angles are not properly computed for circuits
  with prx gates on qubits holding a resonator state, i.e. circuits that require running without move gate validation.
  `#147 <https://github.com/iqm-finland/qiskit-on-iqm/pull/147>`_

Version 17.1
============

* Small note about IQM Client's API deprecation warning added to the user guide.
  `#146 <https://github.com/iqm-finland/qiskit-on-iqm/pull/146>`_

Version 17.0
============

* Removed support for Python 3.9.
* Removed support for ``qiskit < 1.0``.
* Added support for ``qiskit == 1.2`` and ``qiskit-aer == 0.15``.
* Updated the documentation.
* :meth:`.IQMBackendBase.qubit_name_to_index` and :meth:`.IQMBackendBase.index_to_qubit_name` now
  raise an error when using an invalid qubit name or index, rather than returning None.
* Refactored :meth:`.IQMBackend.create_run_request` to improve user experience when using IQM
  specific run options.
* Moved the circuit serialization logic from :class:`.IQMProvider` to :mod:`iqm.qiskit_iqm.qiskit_to_iqm`.
* For IQM Star quantum architectures, :attr:`.IQMBackendBase.target_with_resonators` represents the
  full, physical architecture. :attr:`.IQMBackendBase.target` represents a Qiskit-compatible version.
* Using the Qiskit transpiler with :class:`.IQMBackend`:

  * You can now use the native Qiskit :func:`transpile` function to transpile a circuit to the IQM
    Star architecture as long as your initial circuit does not use any resonators.
  * The Qiskit transpiler now automatically uses the :class:`.IQMOptimizeSingleQubitGates` pass to
    optimize single-qubit gates if ``optimization_level > 0``.
  * There are many new transpiler plugins available that you can use as the ``scheduling_method``
    argument in Qiskit's :func:`transpile` function. You can find them in the
    `Qiskit documentation <https://docs.quantum.ibm.com/guides/transpiler-plugins>`_.
  * If your circuit contains resonators, and optionally :class:`.MoveGate` operations, you can use
    the :func:`.transpile_to_IQM` function to transpile your circuit for the IQM Star architecture.
  * :func:`.transpile_to_IQM` can now restrict itself to use a subset of the qubits by specifying
    the ``restrict_to_qubits`` argument. You will need to additionally provide a qubit mapping to the
    :meth:`.IQMBackend.run` method to ensure that the correct qubits are used.

* Bugfix where the :func:`.transpile_to_IQM` did not retain the circuit layout after transpiling.
* Fixed :func:`.IQMFakeDeneb` readout errors. Fidelities were reported as errors.
  `#125 <https://github.com/iqm-finland/qiskit-on-iqm/pull/125>`_
* :attr:`.IQMBackend.target` now contains symmetric gates such as CZ only in the direction they appear
  in the calibration set. `#140 <https://github.com/iqm-finland/qiskit-on-iqm/pull/140>`_
* Deprecated features:

  * :func:`.optimize_single_qubit_gates` has been deprecated in favor of using the new transpiler
    plugins or :func:`.transpile_to_IQM`. Additionally, this is now incorporated into the Qiskit
    transpiler as documented above.
  * In :meth:`.IQMBackend.create_run_request`, and as a result in :meth:`.IQMBackend.run`, the
    ``max_circuit_duration_over_t2`` and ``heralding_mode`` options have been deprecated in favor of
    using the :class:`.CircuitCompilationOptions` class from :mod:`iqm.iqm_client`.
  * The :class:`.IQMBackend` no longer uses Qiskit's ``options`` attribute to give run options in
    favor of using the arguments of the :meth:`.IQMBackend.run` method directly.


Version 15.6
============

* Added Python 3.12 support. `#139 <https://github.com/iqm-finland/qiskit-on-iqm/pull/139>`
* Python 3.9 support is deprecated and will be removed in the future.

Version 15.5
============

* Fix compatibility with ``iqm-client`` V2 APIVariant. `#132 <https://github.com/iqm-finland/qiskit-on-iqm/pull/132>`_

Version 15.4
============

* Update user guide to incorporate IQM Resonance. `#129 <https://github.com/iqm-finland/qiskit-on-iqm/pull/129>`_

Version 15.3
============

* Multiplexed measurements explained in the user guide. `#130 <https://github.com/iqm-finland/qiskit-on-iqm/pull/130>`_

Version 15.2
============

* ``reset`` operation explained in the user guide. `#127 <https://github.com/iqm-finland/qiskit-on-iqm/pull/127>`_

Version 15.1
============

* Move a part of circuit serialization into :func:`iqm.qiskit_iqm.iqm_provider._serialize_instructions`.
  `#126 <https://github.com/iqm-finland/qiskit-on-iqm/pull/126>`_

Version 15.0
============

* Add support for classically controlled R, RX, RY, X, and Y gates.
  `#123 <https://github.com/iqm-finland/qiskit-on-iqm/pull/123>`_
* Remove the deprecated native operation names ``phased_rx`` and ``measurement``.
  `#123 <https://github.com/iqm-finland/qiskit-on-iqm/pull/123>`_
* Add support for the Reset instruction.
  `#123 <https://github.com/iqm-finland/qiskit-on-iqm/pull/123>`_

Version 14.0
============

* Use dynamic quantum architecture as transpilation target for :class:`IQMBackend`. `#124 <https://github.com/iqm-finland/qiskit-on-iqm/pull/124>`_
* Require ``iqm-client >= 20.0``. `#124 <https://github.com/iqm-finland/qiskit-on-iqm/pull/124>`_
* Disable attestations on ``gh-action-pypi-publish`` to fix failing PyPI publishing. `#124 <https://github.com/iqm-finland/qiskit-on-iqm/pull/124>`_

Version 13.16
=============

* Remove unnecessary build files when publishing documentation. `#122 <https://github.com/iqm-finland/qiskit-on-iqm/pull/122>`_

Version 13.15
=============

* User guide updated. `#120 <https://github.com/iqm-finland/qiskit-on-iqm/pull/120>`_

Version 13.14
=============

* User guide and API documentation updated. `#117 <https://github.com/iqm-finland/qiskit-on-iqm/pull/117>`_

Version 13.13
=============

* Adjustments needed to support Qiskit V1 that are backwards compatible with ``qiskit < 1.0``. `#114 <https://github.com/iqm-finland/qiskit-on-iqm/pull/114>`_
* Updated Qiskit dependencies and testing to support ``qiskit >= 0.45.3 < 1.2`` and ``qiskit-aer >= 0.13 < 0.15``.
* Adjusted documentation to recommend the use of :meth:`qiskit.transpile()` or :meth:`transpile_to_IQM()` in combination with :meth:`backend.run()` instead of using :meth:`execute()`.
* Added a DeprecationWarning for use of ``qiskit < 1.0``. Users are encouraged to read the `Qiskit migration guide <https://docs.quantum.ibm.com/migration-guides>`_ to see how they need to change their code.

Version 13.12
=============

* Add IQMFakeAphrodite backend `#113 <https://github.com/iqm-finland/qiskit-on-iqm/pull/113>`_

Version 13.11
=============

* Added the option to change the timeout between waiting for results when a job is submitted. `Github issue #108 <https://github.com/iqm-finland/qiskit-on-iqm/issues/108>`_
* Added support for optional MOVE gate validation bypassing for advanced users. `#112 <https://github.com/iqm-finland/qiskit-on-iqm/pull/112>`_
* Require ``iqm-client >= 18.0``. `iqm-client PR #124 <https://github.com/iqm-finland/iqm-client/pull/124>`_

Version 13.10
=============

* Allow inspecting a run request before submitting it for execution. `#115 <https://github.com/iqm-finland/qiskit-on-iqm/pull/115>`_
* Require ``iqm-client >= 17.8``. `#115 <https://github.com/iqm-finland/qiskit-on-iqm/pull/115>`_

Version 13.9
============

* Clarify the documentation on automatic transpilation. `#104 <https://github.com/iqm-finland/qiskit-on-iqm/pull/104>`_
* Added a missing character to the docs.  `#110 <https://github.com/iqm-finland/qiskit-on-iqm/pull/110>`_
* Added IQMFakeDeneb backend for noisy simulation of the Deneb backend.  `#109 <https://github.com/iqm-finland/qiskit-on-iqm/pull/109>`_

Version 13.8
============

* Require ``iqm-client >= 17.6``. `#106 <https://github.com/iqm-finland/qiskit-on-iqm/pull/106>`_

Version 13.7
============

* Show full response error in all cases of receiving a HTTP 4xx error response. `#103 <https://github.com/iqm-finland/qiskit-on-iqm/pull/103>`_
* Add new job states to support job delete operation in the backend.

Version 13.6
============

* Update the docstring of ``max_circuits`` property of ``IQMBackend``. `#95 <https://github.com/iqm-finland/qiskit-on-iqm/pull/95>`_

Version 13.5
============

* Fix ``transpile_example`` so that it works also when less than 5 qubits are available. `#102 <https://github.com/iqm-finland/qiskit-on-iqm/pull/102>`_

Version 13.4
============

* Fix bug where Qiskit job monitoring could give an error when a job is queued. `#99 <https://github.com/iqm-finland/qiskit-on-iqm/pull/99>`_

Version 13.3
============

* Move examples inside the Python package.  `#100 <https://github.com/iqm-finland/qiskit-on-iqm/pull/100>`_

Version 13.2
============

* Update code examples in user guide.  `#97 <https://github.com/iqm-finland/qiskit-on-iqm/pull/97>`_

Version 13.1
============

* Computational resonator transpilation is now supported with ``transpile_to_IQM``. `#96 <https://github.com/iqm-finland/qiskit-on-iqm/pull/96>`_
* Require ``iqm-client >= 17.2``. `#96 <https://github.com/iqm-finland/qiskit-on-iqm/pull/96>`_
* Define ``move`` gate as ``swap``. `#96 <https://github.com/iqm-finland/qiskit-on-iqm/pull/96>`_

Version 13.0
============

* Require ``iqm-client >= 17.0``  `#90 <https://github.com/iqm-finland/qiskit-on-iqm/pull/90>`_
* Add MoveGate to model the move operation between qubit and resonator.
* Add ``IQMCircuit`` wrapper for ``QuantumCircuit`` to allow ``.move()`` operation to be used more easily.
* Add a layout pass to ensure correct qubits are selected for transpilation based on quantum architecture.

Version 12.2
============

* Use GitHub Action as a Trusted Publisher to publish packages to PyPI. `#94 <https://github.com/iqm-finland/qiskit-on-iqm/pull/94>`_

Version 12.1
============

* Remove multiversion documentation. `#92 <https://github.com/iqm-finland/qiskit-on-iqm/pull/92>`_

Version 12.0
============

* Require ``iqm-client >= 16.0``.
* Remove ``circuit_duration_check`` from ``IQMBackend`` options.
* Add ``max_circuit_duration_over_t2`` to ``IQMBackend`` options.

Version 11.10
=============

* Require ``iqm-client >= 15.2``. Bump dependencies and dev tools. `#89 <https://github.com/iqm-finland/qiskit-on-iqm/pull/89>`_

Version 11.9
============

* Add ``name`` to backends. `#88 <https://github.com/iqm-finland/qiskit-on-iqm/pull/88>`_

Version 11.8
============

* Add ``IQMFakeApollo`` fake backend. `#66 <https://github.com/iqm-finland/qiskit-on-iqm/pull/66>`_

Version 11.7
============

* Update user guide with more information of execution timestamps. `#85 <https://github.com/iqm-finland/qiskit-on-iqm/pull/85>`_

Version 11.6
============

* Update example link in user guide. (Relates to `#79 <https://github.com/iqm-finland/qiskit-on-iqm/pull/79>`_.) `#86 <https://github.com/iqm-finland/qiskit-on-iqm/pull/86>`_

Version 11.5
============

* Use latest version of ``sphinx-multiversion-contrib`` to fix documentation version sorting. `#84 <https://github.com/iqm-finland/qiskit-on-iqm/pull/84>`_

Version 11.4
============

* Fix typo in how the job status is reported. `#83 <https://github.com/iqm-finland/qiskit-on-iqm/pull/83>`_

Version 11.3
============

* Add IQM specific circuit optimization. `#81 <https://github.com/iqm-finland/qiskit-on-iqm/pull/81>`_

Version 11.2
============

* Raise warning instead of error when unknown option is passed to ``IQMBackend.run``. `#82 <https://github.com/iqm-finland/qiskit-on-iqm/pull/82>`_

Version 11.1
============

* Add ``circuit_callback`` option to ``IQMBackend``. `#80 <https://github.com/iqm-finland/qiskit-on-iqm/pull/80>`_
* Raise error when unknown option is passed to ``IQMBackend.run``. Previously they were silently ignored. `#80 <https://github.com/iqm-finland/qiskit-on-iqm/pull/80>`_
* Improve handling of options passed to ``IQMBackend.run``. `#80 <https://github.com/iqm-finland/qiskit-on-iqm/pull/80>`_
* Fix the type of ``date`` in result object. `#80 <https://github.com/iqm-finland/qiskit-on-iqm/pull/80>`_
* ``IQMBackend.run`` can now accept circuits containing `x`, `rx`, `y` and `ry` gates. `#80 <https://github.com/iqm-finland/qiskit-on-iqm/pull/80>`_

Version 11.0
============

* Move ``qiskit_iqm`` package to ``iqm`` namespace. `#79 <https://github.com/iqm-finland/qiskit-on-iqm/pull/79>`_

Version 10.11
=============

* Update user guide with information of execution timestamps. `#78 <https://github.com/iqm-finland/qiskit-on-iqm/pull/78>`_

Version 10.10
=============

* Upgrade to qiskit ~= 0.44.1. `#77 <https://github.com/iqm-finland/qiskit-on-iqm/pull/77>`_
* Make the ``max_circuits`` property of ``IQMBackend`` user-configurable. `#77 <https://github.com/iqm-finland/qiskit-on-iqm/pull/77>`_
* Implement ``error_message`` method for ``IQMJob``. `#77 <https://github.com/iqm-finland/qiskit-on-iqm/pull/77>`_
* Explicitly specify symmetric CZ properties when building the transpilation target. `#77 <https://github.com/iqm-finland/qiskit-on-iqm/pull/77>`_

Version 10.9
============

* Upgrade to iqm-client >= 13.2. `#76 <https://github.com/iqm-finland/qiskit-on-iqm/pull/76>`_

Version 10.8
============

* Fix two-qubit gate error construction in ``IQMFakeBackend``.

Version 10.7
============

* Capture execution timestamps in :meth:`IQMJob.result`.

Version 10.6
============

* More accurate mapping of job statuses in :meth:`IQMJob.status`.
* Documentation fixes.

Version 10.5
============

* Clarify the documentation on backend options. `#73 <https://github.com/iqm-finland/qiskit-on-iqm/pull/73>`_

Version 10.4
============

* Support the identity gate. `#71 <https://github.com/iqm-finland/qiskit-on-iqm/pull/71>`_

Version 10.3
============

* Add support for Python 3.11. `#70 <https://github.com/iqm-finland/qiskit-on-iqm/pull/70>`_

Version 10.2
============

* Implement ``cancel`` method for ``IQMJob``. `#69 <https://github.com/iqm-finland/qiskit-on-iqm/pull/69>`_

Version 10.1
============

* Update the script link for the Hello world example. `#68 <https://github.com/iqm-finland/qiskit-on-iqm/pull/68>`_

Version 10.0
============

* Fix a bug in the Hello world example. `#67 <https://github.com/iqm-finland/qiskit-on-iqm/pull/67>`_

Version 9.0
============
* Add readout errors to ``IQMErrorProfile``. `#50 <https://github.com/iqm-finland/qiskit-on-iqm/pull/50>`_

Version 8.3
============

* Bugfixes for ``heralding`` run with zero shots returned. `#65 <https://github.com/iqm-finland/qiskit-on-iqm/pull/65>`_
* Allow specifying ``calibration_set_id`` both as string and as ``UUID``. `#65 <https://github.com/iqm-finland/qiskit-on-iqm/pull/65>`_

Version 8.2
============

* Add ``heralding`` option to ``IQMBackend``. `#63 <https://github.com/iqm-finland/qiskit-on-iqm/pull/63>`_
* Upgrade to ``IQMClient`` version 12.5. `#63 <https://github.com/iqm-finland/qiskit-on-iqm/pull/63>`_

Version 8.1
===========

* Upgrade to IQMClient version 12.4 `#61 <https://github.com/iqm-finland/qiskit-on-iqm/pull/61>`_
* Add parameter ``circuit_duration_check`` allowing to control server-side maximum circuit duration check `#61 <https://github.com/iqm-finland/qiskit-on-iqm/pull/61>`_

Version 8.0
===========

* Update the README `#58 <https://github.com/iqm-finland/qiskit-on-iqm/pull/58>`_ and `#60 <https://github.com/iqm-finland/qiskit-on-iqm/pull/60>`_
* Clarify the example script `#62 <https://github.com/iqm-finland/qiskit-on-iqm/pull/62>`_

Version 7.15
============

* Add info about custom calibration set to user guide `#59 <https://github.com/iqm-finland/qiskit-on-iqm/pull/59>`_

Version 7.14
============

* Generate license information for dependencies on every release `#57 <https://github.com/iqm-finland/qiskit-on-iqm/pull/57>`_

Version 7.13
============

* Upgrade to IQMClient version 12.2 `#56 <https://github.com/iqm-finland/qiskit-on-iqm/pull/56>`_

Version 7.12
============

* Upgrade to IQMClient version 12.0 `#55 <https://github.com/iqm-finland/qiskit-on-iqm/pull/55>`_

Version 7.11
============

* Bump Qiskit dependency to `~= 0.42.1` `#54 <https://github.com/iqm-finland/qiskit-on-iqm/pull/54>`_

Version 7.10
============

* Add facade backend for Adonis by introducing ``facade_adonis`` backend type `#53 <https://github.com/iqm-finland/qiskit-on-iqm/pull/53>`_

Version 7.9
===========

* Add request into result metadata `#51 <https://github.com/iqm-finland/qiskit-on-iqm/pull/51>`_

Version 7.8
===========

* Drop circuit metadata if it is not JSON serializable `#49 <https://github.com/iqm-finland/qiskit-on-iqm/pull/49>`_
* Produce ``UserWarning`` if metadata is dropped `#49 <https://github.com/iqm-finland/qiskit-on-iqm/pull/49>`_

Version 7.7
===========

* "Pin down" supported Python versions to 3.9 and 3.10. `#40 <https://github.com/iqm-finland/qiskit-on-iqm/pull/40>`_
* Configure Tox to skip missing versions of Python interpreters when running tests. `#40 <https://github.com/iqm-finland/qiskit-on-iqm/pull/40>`_
* Move project metadata and configuration to ``pyproject.toml``. `#40 <https://github.com/iqm-finland/qiskit-on-iqm/pull/40>`_

Version 7.6
===========

* Check that circuit metadata is JSON serializable `#48 <https://github.com/iqm-finland/qiskit-on-iqm/pull/48>`_

Version 7.5
===========

* Adding noisy simulation by introducing ``IQMFakeAdonis`` and ``IQMFakeBackend`` `#35 <https://github.com/iqm-finland/qiskit-on-iqm/pull/35>`_

Version 7.4
===========

* Provide version information to IQMClient. `#45 <https://github.com/iqm-finland/qiskit-on-iqm/pull/45>`_

Version 7.3
===========

* Build and publish docs for older versions. `#43 <https://github.com/iqm-finland/qiskit-on-iqm/pull/43>`_

Version 7.2
===========

* Make the Hello world example even easier to follow. `#44 <https://github.com/iqm-finland/qiskit-on-iqm/pull/44>`_

Version 7.1
===========

* Add a simple example for getting started. `#41 <https://github.com/iqm-finland/qiskit-on-iqm/pull/41>`_

Version 7.0
===========

* Use new opaque UUID for ``calibration_set_id``. `#37 <https://github.com/iqm-finland/qiskit-on-iqm/pull/37>`_

Version 6.3
===========

* Construct ``IQMJob.circuit_metadata`` from data retrieved from the server, if needed. `#36 <https://github.com/iqm-finland/qiskit-on-iqm/pull/36>`_

Version 6.2
===========

* Upgrade to ``qiskit ~= 0.39.1`` and remove the life hack of adding measurement gates to the target. `#34 <https://github.com/iqm-finland/qiskit-on-iqm/pull/34>`_

Version 6.1
===========

* Add ``qubit_name_to_index`` and ``index_to_qubit_name`` methods to ``IQMBackend``. `#33 <https://github.com/iqm-finland/qiskit-on-iqm/pull/33>`_
* Fix the indexing order of qubits. `#33 <https://github.com/iqm-finland/qiskit-on-iqm/pull/33>`_

Version 6.0
===========

* Implement transpiler target for ``IQMBackend``. `#32 <https://github.com/iqm-finland/qiskit-on-iqm/pull/32>`_


Version 5.0
===========

* Remove ``settings`` option from ``IQMBackend.run``. `#28 <https://github.com/iqm-finland/qiskit-on-iqm/pull/28>`_

Version 4.6
===========

* Enable mypy support. `#27 <https://github.com/iqm-finland/qiskit-on-iqm/pull/27>`_

Version 4.5
===========

* Move calibration set ID from result's metadata to the individual results' metadata. `#25 <https://github.com/iqm-finland/qiskit-on-iqm/pull/25>`_

Version 4.4
===========

* Upgrade to iqm-client 7.0. `#24 <https://github.com/iqm-finland/qiskit-on-iqm/pull/24>`_
* Add calibration set ID to result's metadata. `#24 <https://github.com/iqm-finland/qiskit-on-iqm/pull/24>`_

Version 4.3
===========

* ``cortex-cli`` is now the preferred way of authentication.

Version 4.2
===========

* Add optional ``calibration_set_id`` parameter to ``IQMBackend.run``. `#20 <https://github.com/iqm-finland/qiskit-on-iqm/pull/20>`_
* Update documentation regarding the use of Cortex CLI. `#20 <https://github.com/iqm-finland/qiskit-on-iqm/pull/20>`_

Version 4.1
===========

* iqm-client 6.0 support. `#21 <https://github.com/iqm-finland/qiskit-on-iqm/pull/21>`_

Version 4.0
===========

* Remove ``settings_path`` from ``IQMProvider`` and add ``settings`` option to ``IQMBackend.run``. `#17 <https://github.com/iqm-finland/qiskit-on-iqm/pull/17>`_

Version 3.1
===========

* Use metadata returned from iqm-client for minor improvements. `#19 <https://github.com/iqm-finland/qiskit-on-iqm/pull/19>`_

Version 3.0
===========

* Experimental enabling of batch circuit exection. `#18 <https://github.com/iqm-finland/qiskit-on-iqm/pull/18>`_

Version 2.3
===========

* Make ``settings_path`` optional parameter for ``IQMProvider``. `#14 <https://github.com/iqm-finland/qiskit-on-iqm/pull/14>`_
* Requires iqm-client 3.3 if ``settings_path`` is not specified.

Version 2.2
===========

* Use IQM Client's ``get_run_status`` instead of ``get_run`` to retrieve status. `#13 <https://github.com/iqm-finland/qiskit-on-iqm/pull/13>`_
* Requires iqm-client 3.2

Version 2.1
===========

* Allow serialization of ``barrier`` operations. `#12 <https://github.com/iqm-finland/qiskit-on-iqm/pull/12>`_

Version 2.0
===========

* Update user authentication to use access token. `#11 <https://github.com/iqm-finland/qiskit-on-iqm/pull/11>`_
* Upgrade IQMClient to version >= 2.0 `#11 <https://github.com/iqm-finland/qiskit-on-iqm/pull/11>`_

Version 1.1
===========

* Fix code examples in `user guide <https://iqm-finland.github.io/qiskit-on-iqm/user_guide.html>`_, add missing dependency in `developer guide <https://github.com/iqm-finland/qiskit-on-iqm/blob/main/CONTRIBUTING.rst>`_. `#8 <https://github.com/iqm-finland/qiskit-on-iqm/pull/8>`_

Version 1.0
===========

* Updated documentation layout to use sphinx-book-theme. `#6 <https://github.com/iqm-finland/qiskit-on-iqm/pull/6>`_

Version 0.2
===========

* Publish ``qiskit_iqm``. `#4 <https://github.com/iqm-finland/qiskit-on-iqm/pull/4>`_
* Implement functionality to serialize compatible circuits, send for execution and parse returned results. `#3 <https://github.com/iqm-finland/qiskit-on-iqm/pull/3>`_


Version 0.1
===========

* Project skeleton created.
