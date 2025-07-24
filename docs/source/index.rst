
PySATL-TSP
==========

.. image:: https://img.shields.io/github/actions/workflow/status/PySATL/pysatl-tsp/.github/workflows/check.yaml?branch=main&event=push&style=for-the-badge&label=Checks
   :target: https://github.com/PySATL/pysatl-tsp/blob/main/.github/workflows/check.yaml
   :alt: Checks

.. image:: https://img.shields.io/github/license/PySATL/pysatl-tsp.svg?style=for-the-badge&color=blue
   :target: LICENSE
   :alt: MIT License

PySATL **Time Series Processing** subproject (*abbreviated pysatl-tsp*) is a module designed for adaptive processing of time series data with a focus on streaming architecture. It implements a `chain of responsibility pattern <https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern>`_ that enables building complex data processing pipelines with minimal boilerplate code, making it suitable for real-time applications and large dataset analysis.


.. toctree::
   :hidden:
   :caption: Contents

   apidocs/index
   contributing
   license

Requirements
------------

* Python 3.10+
* Poetry 1.8.0+

Installation
------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/PySATL/pysatl-tsp

Install dependencies:

.. code-block:: bash

   poetry install

Basic Pipeline Example:
-----------------------

.. code-block:: python

   from pysatl_tsp.core.data_providers import SimpleDataProvider
   from pysatl_tsp.core.processor import MappingHandler
   from pysatl_tsp.core.scrubber import LinearScrubber

   # Create a data source
   data = [i for i in range(100)]
   provider = SimpleDataProvider(data)

   # Define a simple processing pipeline:
   # 1. Create windows of 10 elements with 50% overlap
   # 2. Calculate the average of each window
   pipeline = (
       provider
       | LinearScrubber(window_length=10, shift_factor=0.5)
       | MappingHandler(map_func=lambda window: sum(window.values) / len(window))
   )

   # Process the data
   results = []
   for avg in pipeline:
       results.append(avg)

   print(f"Number of windows: {len(results)}")
   print(f"First 3 window averages: {results[:3]}")

   # Visualize results
   import matplotlib.pyplot as plt
   plt.figure(figsize=(10, 5))
   plt.plot(results)
   plt.title('Window Averages')
   plt.xlabel('Window Index')
   plt.ylabel('Average Value')
   plt.grid(True)
   plt.show()

Development
-----------

Install requirements

.. code-block:: bash

   poetry install --with dev

Pre-commit
----------

Install pre-commit hooks:

.. code-block:: shell

   poetry run pre-commit install

Starting manually:

.. code-block:: shell

   poetry run pre-commit run --all-files --color always --verbose --show-diff-on-failure
