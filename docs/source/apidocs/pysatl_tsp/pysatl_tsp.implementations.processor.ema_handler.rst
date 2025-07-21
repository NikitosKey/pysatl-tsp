:py:mod:`pysatl_tsp.implementations.processor.ema_handler`
==========================================================

.. py:module:: pysatl_tsp.implementations.processor.ema_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EMAHandler <pysatl_tsp.implementations.processor.ema_handler.EMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler
          :summary:

API
~~~

.. py:class:: EMAHandler(length: int = 10, adjust: bool = False, sma: bool = True, alpha: float | None = None, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.ema_handler.EMAHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.InductiveHandler`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler.__init__

   .. py:method:: _compute_result(state: dict[str, typing.Any]) -> float | None
      :canonical: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._compute_result

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._compute_result

   .. py:method:: _initialize_state() -> dict[str, typing.Any]
      :canonical: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._initialize_state

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._initialize_state

   .. py:method:: _update_state(state: dict[str, typing.Any], value: float | None) -> dict[str, typing.Any]
      :canonical: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._update_state

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.ema_handler.EMAHandler._update_state
