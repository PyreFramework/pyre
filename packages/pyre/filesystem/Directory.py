# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


# superclass
from .File import File

# class declaration
class Directory(File):
    """
    Representation of local filesystem folders
    """

    # constants
    marker = 'd'
    isDirectory = True

    # implementation details
    __slots__ = ()


# end of file
