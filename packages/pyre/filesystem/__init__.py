# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


# factories
def newLocalFilesystem(walker=None, **kwds):
    from .LocalFilesystem import LocalFilesystem

    # build a walker, if necessary
    walker = walker or newDirectoryWalker()


    return LocalFilesystem(**kwds)


def newSimpleExplorer(**kwds):
    from .SimpleExplorer import SimpleExplorer
    return SimpleExplorer(**kwds)


def newTreeExplorer(**kwds):
    from .TreeExplorer import TreeExplorer
    return TreeExplorer(**kwds)


def newVirtualFilesystem(**kwds):
    from .Filesystem import Filesystem
    return Filesystem(**kwds)


def newDirectoryWalker(**kwds):
    from .DirectoryWalker import DirectoryWalker
    return DirectoryWalker(**kwds)


def newStatRecognizer(**kwds):
    from .StatRecognizer import StatRecognizer
    return StatRecognizer(**kwds)


# errors
class GenericError(Exception):
    """
    Base class for all errors in this package

    Can be used as a catchall when detecting errors generated by this package
    """

    def __init__(self, message, **kwds):
        super().__init__(**kwds)
        self.message = message
        return

    def __str__(self):
        return self.message


class DirectoryListingError(GenericError):
    """
    Exception raised when something goes wrong with listing the contents of a local dierctory
    """

    def __init__(self, path, error, **kwds):
        msg = "error while accessing {0!r}: {1}".format(path, error)
        super().__init__(message=msg, **kwds)
        self.path = path
        return


class FilesystemError(GenericError):
    """
    Base class for all filesystem errors

    Can be used as a catchall when detecting filesystem related exceptions
    """

    def __init__(self, filesystem, node, **kwds):
        super().__init__(**kwds)
        self.filesystem = filesystem
        self.node = node
        return


class FolderInsertionError(FilesystemError):

    def __init__(self, path, target, **kwds):
        msg = "error while inserting {0!r}: {1!r} is not a folder".format(path, target)
        super().__init__(message=msg, **kwds)
        self.path = path
        self.target = target
        return


# package constants
PATH_SEPARATOR = '/'


# debugging support
_metaclass_Node = type
_metaclass_Filesystem = type

# end of file 
