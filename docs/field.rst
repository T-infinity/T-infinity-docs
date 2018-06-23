FieldInterface
==============
A field is data defined across a mesh domain. 
Fields consist of entries (scalar, vector, or tensor data) defined at either the cells or nodes of a mesh.
An entry can be integers (either 32 bit or 64 bit) or floating point values (either single or double precision).
Each entry in a field must be the same length (if the field represents scalar data, all nodes must have scalar data).
Entries of a field are accessed using local entity IDs by calling ``void Field::value(int entity_id, void* data)``.
Fields have a string description to help identify what the field represents.  

Additional requirements are placed on fields based on their usage.  
For example, mesh adaptation plugins take a field as input that represents the target metric spacing.
These metric fields must be 6 double precision numbers defined at each mesh node.  The 6 numbers must be the upper 
triangular entries of the metric tensor at the node in row ordering.

