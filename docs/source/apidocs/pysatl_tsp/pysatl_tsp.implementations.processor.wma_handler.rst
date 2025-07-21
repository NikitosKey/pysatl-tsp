:py:mod:`pysatl_tsp.implementations.processor.wma_handler`
==========================================================

.. py:module:: pysatl_tsp.implementations.processor.wma_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.wma_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`WMAHandler <pysatl_tsp.implementations.processor.wma_handler.WMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.wma_handler.WMAHandler
          :summary:

API
~~~

.. py:class:: WMAHandler(length: int = 10, asc: bool = True, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.wma_handler.WMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.weighted_moving_average_handler.WeightedMovingAverageHandler`

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.wma_handler.WMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.wma_handler.WMAHandler.__init__

   .. py:method:: _calculate_weights(length: int, asc: bool) -> list[float]
      :canonical: pysatl_tsp.implementations.processor.wma_handler.WMAHandler._calculate_weights

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.wma_handler.WMAHandler._calculate_weights
