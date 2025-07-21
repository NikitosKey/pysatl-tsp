:py:mod:`pysatl_tsp.implementations.processor.pwma_handler`
===========================================================

.. py:module:: pysatl_tsp.implementations.processor.pwma_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`PWMAHandler <pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler
          :summary:

API
~~~

.. py:class:: PWMAHandler(length: int = 10, asc: bool = True, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.weighted_moving_average_handler.WeightedMovingAverageHandler`

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler.__init__

   .. py:method:: _calculate_weights(length: int, asc: bool) -> list[float]
      :canonical: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._calculate_weights

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._calculate_weights

   .. py:method:: _combination(n: int, r: int) -> float
      :canonical: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._combination

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._combination

   .. py:method:: _factorial(n: int) -> int
      :canonical: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._factorial

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.pwma_handler.PWMAHandler._factorial
