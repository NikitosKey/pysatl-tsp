:py:mod:`pysatl_tsp.implementations.processor.ohlc4_handler`
============================================================

.. py:module:: pysatl_tsp.implementations.processor.ohlc4_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.ohlc4_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Ohlc4Handler <pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler
          :summary:

API
~~~

.. py:class:: Ohlc4Handler(source: pysatl_tsp.core.Handler[typing.Any, tuple[float | None, float | None, float | None, float | None]] | None = None)
   :canonical: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler

   Bases: :py:obj:`pysatl_tsp.core.processor.mapping_handler.MappingHandler`\ [\ :py:obj:`tuple`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ , :py:obj:`float | None`\ , :py:obj:`float | None`\ ]\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler.__init__

   .. py:method:: _map_func(t: tuple[float | None, float | None, float | None, float | None]) -> float | None
      :canonical: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler._map_func
      :staticmethod:

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ohlc4_handler.Ohlc4Handler._map_func
