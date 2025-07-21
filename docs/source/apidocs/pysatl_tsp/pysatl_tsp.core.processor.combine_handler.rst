:py:mod:`pysatl_tsp.core.processor.combine_handler`
===================================================

.. py:module:: pysatl_tsp.core.processor.combine_handler

.. autodoc2-docstring:: pysatl_tsp.core.processor.combine_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CombineHandler <pysatl_tsp.core.processor.combine_handler.CombineHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.combine_handler.CombineHandler
          :summary:

API
~~~

.. py:class:: CombineHandler(combine_func: typing.Callable[[list[typing.Any]], pysatl_tsp.core.U], *handlers: pysatl_tsp.core.Handler[pysatl_tsp.core.T, typing.Any], continue_on_partial: bool = True)
   :canonical: pysatl_tsp.core.processor.combine_handler.CombineHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.combine_handler.CombineHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.combine_handler.CombineHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.U]
      :canonical: pysatl_tsp.core.processor.combine_handler.CombineHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.combine_handler.CombineHandler.__iter__
