:py:mod:`pysatl_tsp.core.scrubber.abstract`
===========================================

.. py:module:: pysatl_tsp.core.scrubber.abstract

.. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Scrubber <pysatl_tsp.core.scrubber.abstract.Scrubber>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.Scrubber
          :summary:
   * - :py:obj:`ScrubberWindow <pysatl_tsp.core.scrubber.abstract.ScrubberWindow>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <pysatl_tsp.core.scrubber.abstract.__all__>`
     - .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.__all__
          :summary:

API
~~~

.. py:class:: Scrubber(source: pysatl_tsp.core.Handler[typing.Any, pysatl_tsp.core.T] | None = None)
   :canonical: pysatl_tsp.core.scrubber.abstract.Scrubber

   Bases: :py:obj:`pysatl_tsp.core.Handler`\ [\ :py:obj:`pysatl_tsp.core.T`\ , :py:obj:`pysatl_tsp.core.scrubber.abstract.ScrubberWindow`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.Scrubber

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.Scrubber.__init__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]]
      :canonical: pysatl_tsp.core.scrubber.abstract.Scrubber.__iter__
      :abstractmethod:

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.Scrubber.__iter__

.. py:class:: ScrubberWindow(values: collections.deque[pysatl_tsp.core.T] | None = None, indices: collections.deque[int] | None = None)
   :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow

   Bases: :py:obj:`typing.Generic`\ [\ :py:obj:`pysatl_tsp.core.T`\ ]

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow

   .. rubric:: Initialization

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__init__

   .. py:method:: __eq__(other: object) -> bool
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__eq__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__eq__

   .. py:method:: __getitem__(key: int | slice) -> pysatl_tsp.core.T | pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__getitem__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__getitem__

   .. py:method:: __hash__() -> int
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__hash__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__hash__

   .. py:method:: __iter__() -> collections.abc.Iterator[pysatl_tsp.core.T]
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__iter__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__iter__

   .. py:method:: __len__() -> int
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__len__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__len__

   .. py:method:: __repr__() -> str
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__repr__

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.__repr__

   .. py:method:: append(value: pysatl_tsp.core.T, index: int | None = None) -> None
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.append

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.append

   .. py:method:: clear() -> None
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.clear

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.clear

   .. py:method:: copy() -> pysatl_tsp.core.scrubber.abstract.ScrubberWindow[pysatl_tsp.core.T]
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.copy

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.copy

   .. py:method:: popleft() -> None
      :canonical: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.popleft

      .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.ScrubberWindow.popleft

.. py:data:: __all__
   :canonical: pysatl_tsp.core.scrubber.abstract.__all__
   :value: ['Scrubber', 'ScrubberWindow', 'T']

   .. autodoc2-docstring:: pysatl_tsp.core.scrubber.abstract.__all__
