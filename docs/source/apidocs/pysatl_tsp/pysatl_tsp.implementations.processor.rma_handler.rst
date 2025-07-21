:py:mod:`pysatl_tsp.implementations.processor.rma_handler`
==========================================================

.. py:module:: pysatl_tsp.implementations.processor.rma_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RMAHandler <pysatl_tsp.implementations.processor.rma_handler.RMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler
          :summary:

API
~~~

.. py:class:: RMAHandler(length: int = 10, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.rma_handler.RMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.inductive.inductive_handler.InductiveHandler`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler.__init__

   .. py:method:: _compute_result(state: dict[str, float | int]) -> float | None
      :canonical: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._compute_result

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._compute_result

   .. py:method:: _initialize_state() -> dict[str, float | int]
      :canonical: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._initialize_state

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._initialize_state

   .. py:method:: _update_state(state: dict[str, float | int], value: float | None) -> dict[str, float | int]
      :canonical: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._update_state

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.rma_handler.RMAHandler._update_state
