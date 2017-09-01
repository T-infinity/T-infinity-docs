FluidSolver
===========
Fluid solvers are plugins expected to solve 3D flow equations on a grid.
Fluid solvers operate on a single domain.  They are expected to communicate using the MPI communicator that is given to the fluid solver during initialization.
Fluid solvers using any other communicator (especially MPI_COMM_WORLD) will cause major problems.

