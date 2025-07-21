:py:mod:`pysatl_tsp.implementations.processor.midpoint_handler`
===============================================================

.. py:module:: pysatl_tsp.implementations.processor.midpoint_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.midpoint_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`MidpointHandler <pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler
          :summary:

API
~~~

.. py:class:: MidpointHandler(length: int = 10, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.handler.T] | None = None)
   :canonical: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.moving_window_handler.MovingWindowHandler`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler.__init__

   .. py:method:: _compute_result(state: dict[str, typing.Any]) -> float | None
      :canonical: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler._compute_result

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.midpoint_handler.MidpointHandler._compute_result
