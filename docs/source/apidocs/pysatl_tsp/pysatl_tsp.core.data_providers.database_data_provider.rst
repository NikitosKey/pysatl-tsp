:py:mod:`pysatl_tsp.core.data_providers.database_data_provider`
===============================================================

.. py:module:: pysatl_tsp.core.data_providers.database_data_provider

.. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DataBaseDataProvider <pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider>`
     - .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider
          :summary:
   * - :py:obj:`DatabaseAdapter <pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter>`
     - .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter
          :summary:

API
~~~

.. py:class:: DataBaseDataProvider(connection_params: dict[str, typing.Any], query: str, adapter: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter[pysatl_tsp.core.data_providers.abstract.T], params: tuple[typing.Any, ...] = ())
   :canonical: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider

   Bases: :py:obj:`pysatl_tsp.core.data_providers.abstract.DataProvider`\ [\ :py:obj:`pysatl_tsp.core.data_providers.abstract.T`\ ], :py:obj:`typing.Generic`\ [\ :py:obj:`pysatl_tsp.core.data_providers.abstract.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.data_providers.abstract.T]
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider.__iter__

   .. py:method:: _connection_context() -> typing.Any
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider._connection_context

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DataBaseDataProvider._connection_context

.. py:class:: DatabaseAdapter
   :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`pysatl_tsp.core.data_providers.abstract.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter

   .. py:method:: close_connection(connection: typing.Any) -> None
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.close_connection
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.close_connection

   .. py:method:: close_cursor(cursor: typing.Any) -> None
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.close_cursor
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.close_cursor

   .. py:method:: connect(connection_params: dict[str, typing.Any]) -> typing.Any
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.connect
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.connect

   .. py:method:: execute_query(connection: typing.Any, query: str, params: tuple[typing.Any, ...] = ()) -> typing.Any
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.execute_query
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.execute_query

   .. py:method:: fetch_data(cursor: typing.Any) -> collections.abc.Iterator[pysatl_tsp.core.data_providers.abstract.T]
      :canonical: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.fetch_data
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.database_data_provider.DatabaseAdapter.fetch_data
