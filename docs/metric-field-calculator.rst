.. _metric_field_calculator:

Metric Field Calculator
=======================
A metric field calculator takes a Mesh, 
and a field that defines a hessian at each node of the input mesh.  
The output must be a field that defines Riemannian Metric Tensor at 
each node of the input mesh.  The adaptation community has settled 
on defining the RMT at mesh nodes, even when interacting with cell
based fluid solvers.  

The RMT field is a symmetric 3x3 tensor.  Only the unique 6 elements of the tensor are in the field.  
The field will contain the RMT tensor at each node in the input mesh as a 6 element array defining the upper triangular 
portion of the tensor in row-wise ordering.
