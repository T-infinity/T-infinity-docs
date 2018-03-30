FluidSolver
===========
Fluid solvers are plugins expected to solve 3D flow equations on a grid.
Fluid solvers operate on a single domain.  They are expected to communicate using the MPI communicator that is given to the fluid solver during initialization.
Fluid solvers using any other communicator (especially ``MPI_COMM_WORLD``) will cause major problems.


Initialization
--------------
During initialization fluid solvers are given a ``MeshInterface``, an `MPI_Comm` and an ascii string of options.
The solver should use the initialization phase to initialize all data structures within the solver.  
Initialization must include allocating the solution stored within the solver. 


``get`` and ``set`` state
-------------------------
After initialization, the solver must be prepared to accept new solution states at either nodes (for node based solvers) or cells (for cell based solvers).
The framework may choose to overwrite the solver's initial flow state using the ``set`` methods.  
Some reasons why the framework may choose to overwrite the flow state include:

  -to initialize the flow from previously saved state snapshots (snap files)
  -to initialize the flow by seeding the initial field from interpolations from a coarse grid
  -to initialize the flow to help aid in stability during the first few solution iterations
  -to overwrite the flow state at overset receptor locations during an overset simulation

Solve
-----
The ``solve()`` method is used for steady problems.  
When called the fluid solver should solve the steady fluid problem.
The solver should also allocate and compute any output quantity the solver is capable of emitting.

Post Processing
---------------
After ``solve()`` is called the framework may choose to call the ``get`` method to retrieve field data.  
The framework may choose to access all, some, or none of the variables a ``FluidSolver`` is capable of outputting
as listed by the ``listNode/CellFields()`` method.  


Updating Mesh node locations
----------------------------
Even for steady problems the ``solve()`` method may be called multiple times.
For quasi-steady problems, such as static static fluid structures deformation, 
the mesh node locations may move between ``solve()`` calls.  If the node locations
of the mesh change the fluid solver will be notified through the ``updateNodeLocations()`` call. 
A new mesh will be passed in.  This mesh will have the same topology as the mesh used during initialization -
only the mesh node locations may have moved.

A note on internal state
------------------------

