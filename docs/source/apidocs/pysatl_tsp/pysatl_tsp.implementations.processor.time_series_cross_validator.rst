:py:mod:`pysatl_tsp.implementations.processor.time_series_cross_validator`
==========================================================================

.. py:module:: pysatl_tsp.implementations.processor.time_series_cross_validator

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.time_series_cross_validator
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`TimeSeriesCrossValidator <pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator
          :summary:

API
~~~

.. py:class:: TimeSeriesCrossValidator(min_train_size: int, val_size: int, source: typing.Optional[pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T]] = None)
   :canonical: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`tuple`\ [\ :py:obj:`pysatl_tsp.core.scrubber.ScrubberWindow`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]\ , :py:obj:`pysatl_tsp.core.scrubber.ScrubberWindow`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]\ ]\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[tuple[pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T], pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T]]]
      :canonical: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator.__iter__

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.time_series_cross_validator.TimeSeriesCrossValidator.__iter__
