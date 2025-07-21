:py:mod:`pysatl_tsp.implementations.processor.fwma_handler`
===========================================================

.. py:module:: pysatl_tsp.implementations.processor.fwma_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FWMAHandler <pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler
          :summary:

API
~~~

.. py:class:: FWMAHandler(length: int = 10, asc: bool = True, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.weighted_moving_average_handler.WeightedMovingAverageHandler`

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler.__init__

   .. py:method:: _calculate_weights(length: int, asc: bool) -> list[float]
      :canonical: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler._calculate_weights

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler._calculate_weights

   .. py:method:: _fibonacci_sequence(n: int) -> list[float]
      :canonical: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler._fibonacci_sequence

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.fwma_handler.FWMAHandler._fibonacci_sequence
