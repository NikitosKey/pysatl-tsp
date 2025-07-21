:py:mod:`pysatl_tsp.core.scrubber.segmentation_scrubber`
========================================================

.. py:module:: pysatl_tsp.core.scrubber.segmentation_scrubber

.. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OfflineSegmentationScrubber <pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber
          :summary:
   * - :py:obj:`OnlineSegmentationScrubber <pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber
          :summary:

API
~~~

.. py:class:: OfflineSegmentationScrubber(segmentation_rule: typing.Callable[[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]], list[int]], source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber

   Bases: :py:obj:`pysatl_tsp.core.scrubber.abstract.Scrubber`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]]
      :canonical: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OfflineSegmentationScrubber.__iter__

.. py:class:: OnlineSegmentationScrubber(segmentation_rule: typing.Callable[[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]], bool], max_segment_size: int = 2**64, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber

   Bases: :py:obj:`pysatl_tsp.core.scrubber.abstract.Scrubber`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]]
      :canonical: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.segmentation_scrubber.OnlineSegmentationScrubber.__iter__
