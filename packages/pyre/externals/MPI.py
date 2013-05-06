# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# externals
import os
# access to the framework
import pyre
# superclass
from .Tool import Tool
from .Library import Library


# the mpi package manager
class MPI(Tool, Library, family='pyre.externals.mpi'):
    """
    The package manager for MPI packages
    """

    # constants
    category = 'mpi'

    # user configurable state
    launcher = pyre.properties.str(default='mpirun')
    launcher.doc = 'the name of the launcher of MPI jobs'


    # package factories
    @classmethod
    def pyre_select(cls):
        """
        Build a package instance
        """
        # get the os distribution
        distribution = cls.pyre_host.distribution

        # the default for {macports} machines
        if distribution == 'macports':
            # is to use openmpi
            from .OpenMPI import OpenMPI
            return OpenMPI.pyre_package()

        # for all others, just chain up and let my superclass hunt the right package down
        return super().pyre_package()


# end of file 
