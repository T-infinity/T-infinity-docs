:math:`T^{\infty}`MeshInterface
===============================
The ``MeshInterface`` describes read-only access to an unstructured grid.
Only two mesh entities are described: nodes and cells.  
Additional entities (edges, faces, etc) must be derrived from cells and nodes.

Partitioning
------------

Each instance of a ``MeshInterface`` represents one partition of an unstructured grid.
Mesh entities (nodes and cells) may be *resident* on more than one partition, however they will be *owned* 
by only one partition.  If a cell is resident on a partition, all nodes within that cell must 
also be resident on the partition.  Entities that are *resident* but not *owned* are typically referred to as *ghost* or *halo* entities.

Node and Cell Ids
~~~~~~~~~~~~~~~~~

Each node has a local node identifier (Id) and a global node Id.  Likewise, each cell has a local cell Id and a global cell Id.
Local Ids are represented using a 32 bit integer, global ids are represented using a 64 bit integer. 
Complex simulations may require more than 2.2 billion total mesh entities; however it is considered unlikely that any one partition will have over 2.2 billion resident entities.

Local Ids cannot be sparse.
Local Ids begin at ``0`` and end ``total number of local entities - 1``. 
Local Ids are only used by the local partition, no other partition should know a local Id for any entity.
This allows a local partition to reorder entities (for cache efficiency, bandwidth reduction, or convienience) without communicating that reordering.

Unlike local Ids, the global Id of an entity is unique across all partitions that entity is *resident*.
The set of global Ids across all partitions cannot be sparse, they must begin at ``0`` and end at ``total number of entities - 1``. 
However, global Ids on a single partition will almost always be sparse.

Mesh Domains
~~~~~~~~~~~~
:math:`T^{\infty}` supports multiple simultaneous mesh domains.  Multiple domains are required for overset simulations.
Each mesh domain can be partitioned.  Global Ids are only valid within a single domain.  There is no entity identifier
valid across multiple domains.


Conventions
-----------
All elements are described using the CGNS conventions for node orderings.  (See https://cgns.github.io/CGNS_docs_current/sids/conv.html).

