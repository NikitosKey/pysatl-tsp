:py:mod:`pysatl_tsp.core.handler`
=================================

.. py:module:: pysatl_tsp.core.handler

.. autodoc2-docstring:: pysatl_tsp.core.handler
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Handler <pysatl_tsp.core.handler.Handler>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler
          :summary:
   * - :py:obj:`Pipeline <pysatl_tsp.core.handler.Pipeline>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.Pipeline
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`T <pysatl_tsp.core.handler.T>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.T
          :summary:
   * - :py:obj:`U <pysatl_tsp.core.handler.U>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.U
          :summary:
   * - :py:obj:`V <pysatl_tsp.core.handler.V>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.V
          :summary:
   * - :py:obj:`__all__ <pysatl_tsp.core.handler.__all__>`
     - .. autodoc2-docstring:: pysatl_tsp.core.handler.__all__
          :summary:

API
~~~

.. py:class:: Handler(source: pysatl_tsp.core.handler.Handler[typing.Any, pysatl_tsp.core.handler.T] | None = None)
   :canonical: pysatl_tsp.core.handler.Handler

   Bases: :py:obj:`abc.ABC`, :py:obj:`typing.Generic`\ [\ :py:obj:`pysatl_tsp.core.handler.T`\ , :py:obj:`pysatl_tsp.core.handler.U`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.handler.U]
      :canonical: pysatl_tsp.core.handler.Handler.__iter__
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler.__iter__

   .. py:method:: __or__(other: pysatl_tsp.core.handler.Handler[pysatl_tsp.core.handler.U, pysatl_tsp.core.handler.V]) -> pysatl_tsp.core.handler.Pipeline[pysatl_tsp.core.handler.T, pysatl_tsp.core.handler.V]
      :canonical: pysatl_tsp.core.handler.Handler.__or__

      .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler.__or__

   .. py:property:: source
      :canonical: pysatl_tsp.core.handler.Handler.source
      :type: pysatl_tsp.core.handler.Handler[typing.Any, pysatl_tsp.core.handler.T] | None

      .. autodoc2-docstring:: pysatl_tsp.core.handler.Handler.source

.. py:class:: Pipeline(first: pysatl_tsp.core.handler.Handler[pysatl_tsp.core.handler.T, pysatl_tsp.core.handler.U], second: pysatl_tsp.core.handler.Handler[pysatl_tsp.core.handler.U, pysatl_tsp.core.handler.V])
   :canonical: pysatl_tsp.core.handler.Pipeline

   Bases: :py:obj:`pysatl_tsp.core.handler.Handler`\ [\ :py:obj:`pysatl_tsp.core.handler.T`\ , :py:obj:`pysatl_tsp.core.handler.V`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.handler.Pipeline

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.handler.Pipeline.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.handler.V]
      :canonical: pysatl_tsp.core.handler.Pipeline.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.handler.Pipeline.__iter__

.. py:data:: T
   :canonical: pysatl_tsp.core.handler.T
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: pysatl_tsp.core.handler.T

.. py:data:: U
   :canonical: pysatl_tsp.core.handler.U
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: pysatl_tsp.core.handler.U

.. py:data:: V
   :canonical: pysatl_tsp.core.handler.V
   :value: 'TypeVar(...)'

   .. autodoc2-docstring:: pysatl_tsp.core.handler.V

.. py:data:: __all__
   :canonical: pysatl_tsp.core.handler.__all__
   :value: ['Handler', 'T', 'U', 'V']

   .. autodoc2-docstring:: pysatl_tsp.core.handler.__all__
