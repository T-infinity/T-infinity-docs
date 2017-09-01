PreProcessor
============
A PreProcessor is a dynamically loaded plugin that creates a ``Mesh``.  
A PreProcessor is passed only an MPI communicator and a plugin specific json string.
The PreProcessor must return a ``MeshInterface`` object to every rank on the given communicator.
The mesh returned from the PreProcessor must adhere to the conventions described in the ``MeshInterface`` section.
