MeshAdaptation
==============
A ``MeshAdaptation`` plugin takes a ``Mesh``, a Riemannian Metric Tensor ``Field``, and a json formatted string of options.  
The plugin must return a new ``Mesh`` that has been adapted to better conform with the metric field.

The RMT field is a symmetric 3x3 tensor.  Only the unique 6 elements of the tensor are in the field.  
The field will contain the RMT tensor at each node in the input mesh as a 6 element array defining the upper triangular 
portion of the tensor in row-wise ordering.

The output ``Mesh`` must match all the conventions for parallel partitioning, and cell windings as described in :ref:`mesh`.
