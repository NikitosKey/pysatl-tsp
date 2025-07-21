:py:mod:`pysatl_tsp.core.processor.sampling_handler`
====================================================

.. py:module:: pysatl_tsp.core.processor.sampling_handler

.. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OfflineSamplingHandler <pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler
          :summary:
   * - :py:obj:`OnlineSamplingHandler <pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler
          :summary:

API
~~~

.. py:class:: OfflineSamplingHandler(sampling_rule: typing.Callable[[pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T]], list[int]], source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.T]
      :canonical: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OfflineSamplingHandler.__iter__

.. py:class:: OnlineSamplingHandler(sampling_rule: typing.Callable[[pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T]], bool], source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.T]
      :canonical: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.sampling_handler.OnlineSamplingHandler.__iter__
