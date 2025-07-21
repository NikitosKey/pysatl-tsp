:py:mod:`pysatl_tsp.implementations.processor.dema_handler`
===========================================================

.. py:module:: pysatl_tsp.implementations.processor.dema_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DEMAHandler <pysatl_tsp.implementations.processor.dema_handler.DEMAHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler
          :summary:

API
~~~

.. py:class:: DEMAHandler(length: int = 10, source: pysatl_tsp.core.Handler[typing.Any, float | None] | None = None)
   :canonical: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`float | None`\ , :py:obj:`float | None`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[float | None]
      :canonical: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler.__iter__

   .. py:method:: _combine(ema: float | None, ema_of_ema: float | None) -> float | None
      :canonical: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler._combine
      :staticmethod:

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.dema_handler.DEMAHandler._combine
