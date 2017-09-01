MeshInterface
===============================
The heart of :math:`T^{\infty}` is the ``MeshInterface`` that describes read-only access to an unstructured grid.
``MeshInterface`` objects are the primary output of the pre-processing step but are used nearly all :math:`T^{\infty}` plugins.

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
Local Ids cannot be sparse.
Local Ids begin at ``0`` and end ``total number of local entities - 1``. 
Local Ids are only used by the local partition, no other partition should know a local Id for any entity.
This allows a local partition to reorder entities (for cache efficiency, bandwidth reduction, or convienience) without communicating that reordering.

Unlike local Ids, the global Id of an entity is unique across all partitions that entity is *resident*.
The set of global Ids across all partitions cannot be sparse, they must begin at ``0`` and end at ``total number of entities - 1``. 
However, global Ids on a single partition will almost always be sparse.

.. note::
   Local Ids are represented using a 32 bit integer, global ids are represented using a 64 bit integer. 
   Complex simulations may require more than 2.2 billion total mesh entities; however it is considered unlikely that any one partition will have over 2.2 billion resident entities.

Mesh Domains
~~~~~~~~~~~~
:math:`T^{\infty}` supports multiple simultaneous mesh domains.  Multiple domains are required for overset simulations.
Each domain is partitioned across all the ranks of a specific MPI communicator. Global Ids are only valid within a single domain.  
There is no entity identifier valid across multiple domains.


Conventions
-----------
Cells are accessed by calling ``void MeshInterface::cell(int cell_id, int* cell_ptr)``, the same call is used for both volume and surface cells.
This call writes the local node Ids for the cell into the passed pointer using the CGNS convention for node ordering.
(See https://cgns.github.io/CGNS_docs_current/sids/conv.html).
It is the caller's responsibility to ensure there is sufficient memory to fit all the nodes in the requested cell.
The length of a cell is determined calling ``CellType MeshInterface::cellType(int cell_id)`` to get the cell's type.  
Then calling ``int MeshInterface::cellTypeLength(CellType type)`` to get the length of that type.
At this time only fixed width cell types are supported (``NGON`` and ``NFACE`` are not supported).

