# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


# superclass
from .File import File

# class declaration
class NamedPipe(File):
    """
    Representation of named pipes, a unix interprocess communication mechanism
    """

    # constant
    marker = 'p'

    # implementation details
    __slots__ = ()


# end of file
