:py:mod:`pysatl_tsp.core.data_providers.file_data_provider`
===========================================================

.. py:module:: pysatl_tsp.core.data_providers.file_data_provider

.. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FileDataProvider <pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider>`
     - .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`X <pysatl_tsp.core.data_providers.file_data_provider.X>`
     - .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.X
          :summary:

API
~~~

.. py:class:: FileDataProvider(filename: str, handler: typing.Callable[[str], pysatl_tsp.core.data_providers.file_data_provider.X])
   :canonical: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider

   Bases: :py:obj:`pysatl_tsp.core.data_providers.abstract.DataProvider`\ [\ :py:obj:`pysatl_tsp.core.data_providers.file_data_provider.X`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.data_providers.file_data_provider.X]
      :canonical: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.FileDataProvider.__iter__

.. py:data:: X
   :canonical: pysatl_tsp.core.data_providers.file_data_provider.X
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.file_data_provider.X
