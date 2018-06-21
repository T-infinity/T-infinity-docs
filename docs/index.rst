.. image:: _static/images/t-inf-logo-black.png
   :width: 32px
   :align: center
   :alt: T-infinity logo

Getting Started
===============

First you must obtain a T-infinity distribution. 
T-infinity is still under development and currently only available to beta testers.


Installation
------------

Install T-infinity using the install.sh script. 

::
  ./install.sh --help 


Example Usage:
::
  ./install.sh --install-path=~/Desktop/ \
               --mpi-path=/usr/local/mpich/ \
               --c++-compiler=/usr/local/bin/g++ \
               --c-compiler=/usr/local/bin/gcc \
               --fortran-compiler=/usr/local/bin/gfortran

The c, c++, and fortran compiler paths should point to the compiler executables.
The mpi-path should be a folder that contains the `include` and `lib` folder for your mpi installation.

.. toctree::
   :maxdepth: 2

   domain
   mesh
   field
   pre-processor
   mesh-adaptation
   metric-field-calculator
   mesh-deformation
   overset-domain-assembly
   fluid-solver
   structural-solver
   transfer-scheme
   visualization
   examples
   FAQ
   contact
   about
   proposals
