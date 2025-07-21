:py:mod:`pysatl_tsp.implementations.processor.kalman_filter_handler`
====================================================================

.. py:module:: pysatl_tsp.implementations.processor.kalman_filter_handler

.. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`KalmanFilterHandler <pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler
          :summary:

API
~~~

.. py:class:: KalmanFilterHandler(F: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]], H: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]], B: typing.Union[float, numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]]] | None = None, Q: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]] | None = None, R: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]] | None = None, P: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]] | None = None, x0: numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]] | None = None, source: pysatl_tsp.core.Handler[typing.Any, float] | None = None)
   :canonical: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler

   Bases: :py:obj:`pysatl_tsp.core.processor.OnlineFilterHandler`\ [\ :py:obj:`float`\ , :py:obj:`float`\ ]

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler.__init__

   .. py:method:: _apply_kalman_filter(window: pysatl_tsp.core.scrubber.ScrubberWindow[float], _: typing.Any) -> float
      :canonical: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler._apply_kalman_filter

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler._apply_kalman_filter

   .. py:method:: predict(u: typing.Union[float, numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]]] = 0) -> numpy.ndarray[typing.Any, numpy.dtype[numpy.float64]]
      :canonical: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler.predict

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler.predict

   .. py:method:: update(z: float) -> None
      :canonical: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler.update

      .. autodoc2-docstring:: pysatl_tsp.implementations.processor.kalman_filter_handler.KalmanFilterHandler.update
