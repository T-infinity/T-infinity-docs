:math:`T^{\infty}`MeshInterface
===============================
The ``MeshInterface`` describes read-only access to an unstructured grid.
Only two mesh entities are described: nodes and cells.  
Additional entities (edges, faces, etc) must be derrived from cells and nodes.

Partitioning
------------

Each instance of a ``MeshInterface`` represents one partition of an unstructured grid.
Nodes and cells may be *resident* on more than one partition, however they will be *owned* 
by only one partition.  If a cell is resident on a partition, all nodes within that cell must 
also be resident on the partition. Within 


Conventions
-----------
All elements are communicated in CGNS ordering. 

