:py:mod:`pysatl_tsp.core.processor.mapping_handler`
===================================================

.. py:module:: pysatl_tsp.core.processor.mapping_handler

.. autodoc2-docstring:: pysatl_tsp.core.processor.mapping_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`MappingHandler <pysatl_tsp.core.processor.mapping_handler.MappingHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.mapping_handler.MappingHandler
          :summary:

API
~~~

.. py:class:: MappingHandler(map_func: typing.Callable[[pysatl_tsp.core.T], pysatl_tsp.core.U], source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.processor.mapping_handler.MappingHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.mapping_handler.MappingHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.mapping_handler.MappingHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.U]
      :canonical: pysatl_tsp.core.processor.mapping_handler.MappingHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.mapping_handler.MappingHandler.__iter__
