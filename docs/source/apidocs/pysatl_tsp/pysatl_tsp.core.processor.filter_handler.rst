:py:mod:`pysatl_tsp.core.processor.filter_handler`
==================================================

.. py:module:: pysatl_tsp.core.processor.filter_handler

.. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`OfflineFilterHandler <pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler
          :summary:
   * - :py:obj:`OnlineFilterHandler <pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler
          :summary:

API
~~~

.. py:class:: OfflineFilterHandler(filter_func: typing.Callable[[pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T], typing.Any], list[pysatl_tsp.core.U]], filter_config: typing.Any = None, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.U]
      :canonical: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OfflineFilterHandler.__iter__

.. py:class:: OnlineFilterHandler(filter_func: typing.Callable[[pysatl_tsp.core.scrubber.ScrubberWindow[pysatl_tsp.core.T], typing.Any], pysatl_tsp.core.U], filter_config: typing.Any = None, source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.U]
      :canonical: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.filter_handler.OnlineFilterHandler.__iter__
