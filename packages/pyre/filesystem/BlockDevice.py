# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


from .File import File


class BlockDevice(File):
    """
    Representation of block devices, a type of unix device driver
    """


    def identify(self, explorer, **kwds):
        """
        Tell {explorer} that it is visiting a block device
        """
        return explorer.onBlockDevice(self, **kwds)


# end of file 
