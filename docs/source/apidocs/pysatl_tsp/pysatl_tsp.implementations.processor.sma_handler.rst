:py:mod:`pysatl_tsp.implementations.processor.sma_handler`
==========================================================

.. py:module:: pysatl_tsp.implementations.processor.sma_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.sma_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SMAHandler <pysatl_tsp.implementations.processor.sma_handler.SMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.sma_handler.SMAHandler
          :summary:

API
~~~

.. py:class:: SMAHandler(length: int = 10, min_periods: int | None = None, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.sma_handler.SMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.moving_window_handler.MovingWindowHandler`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.sma_handler.SMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.sma_handler.SMAHandler.__init__

   .. py:method:: _compute_result(state: dict[str, typing.Any]) -> float | None
      :canonical: pysatl_tsp.implementations.processor.sma_handler.SMAHandler._compute_result

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.sma_handler.SMAHandler._compute_result
