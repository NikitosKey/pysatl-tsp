:py:mod:`pysatl_tsp.core.data_providers.websocket_data_provider`
================================================================

.. py:module:: pysatl_tsp.core.data_providers.websocket_data_provider

.. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`WebSocketDataProvider <pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider>`
     - .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider
          :summary:

API
~~~

.. py:class:: WebSocketDataProvider(uri: str, subscribe_message: dict[str, typing.Any] | None = None)
   :canonical: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider

   Bases: :py:obj:`pysatl_tsp.core.data_providers.abstract.DataProvider`\ [\ :py:obj:`str`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[str]
      :canonical: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider.__iter__

   .. py:method:: _receiver() -> None
      :canonical: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider._receiver
      :async:

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider._receiver

   .. py:method:: _thread_main() -> None
      :canonical: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider._thread_main

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider._thread_main

   .. py:method:: close() -> None
      :canonical: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider.close

      .. autodoc2-docstring:: pysatl_tsp.core.data_providers.websocket_data_provider.WebSocketDataProvider.close
