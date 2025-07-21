:py:mod:`pysatl_tsp.core.processor.tee_handler`
===============================================

.. py:module:: pysatl_tsp.core.processor.tee_handler

.. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`TeeHandler <pysatl_tsp.core.processor.tee_handler.TeeHandler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.TeeHandler
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`S <pysatl_tsp.core.processor.tee_handler.S>`
     - .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.S
          :summary:

API
~~~

.. py:data:: S
   :canonical: pysatl_tsp.core.processor.tee_handler.S
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.S

.. py:class:: TeeHandler(processor: pysatl_tsp.core.Handler[pysatl_tsp.core.T, pysatl_tsp.core.processor.tee_handler.S], combine_func: typing.Callable[[pysatl_tsp.core.T, pysatl_tsp.core.processor.tee_handler.S], pysatl_tsp.core.U])
   :canonical: pysatl_tsp.core.processor.tee_handler.TeeHandler

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.TeeHandler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.TeeHandler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.U]
      :canonical: pysatl_tsp.core.processor.tee_handler.TeeHandler.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.processor.tee_handler.TeeHandler.__iter__
