:py:mod:`pysatl_tsp.core.scrubber.linear_scrubber`
==================================================

.. py:module:: pysatl_tsp.core.scrubber.linear_scrubber

.. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`LinearScrubber <pysatl_tsp.core.scrubber.linear_scrubber.LinearScrubber>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.LinearScrubber
          :summary:
   * - :py:obj:`SlidingScrubber <pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber
          :summary:

API
~~~

.. py:class:: LinearScrubber(window_length: int = 100, shift_factor: float = 1.0 / 3.0, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.scrubber.abstract.T] | None = None)
   :canonical: pysatl_tsp.core.scrubber.linear_scrubber.LinearScrubber

   Bases: :py:obj:`pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber`\ [\ :py:obj:`pysatl_tsp.core.scrubber.abstract.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.LinearScrubber

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.LinearScrubber.__init__

.. py:class:: SlidingScrubber(take_condition: typing.Callable[[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.scrubber.abstract.T]], bool], shift: int, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.scrubber.abstract.T] | None = None)
   :canonical: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber

   Bases: :py:obj:`pysatl_tsp.core.scrubber.abstract.Scrubber`\ [\ :py:obj:`pysatl_tsp.core.scrubber.abstract.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.scrubber.abstract.T]]
      :canonical: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.linear_scrubber.SlidingScrubber.__iter__
