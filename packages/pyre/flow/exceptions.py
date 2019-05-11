# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2019 all rights reserved
#


"""
Definitions for all exceptions raised by this package
"""


# grab the base framework exception
from ..framework.exceptions import FrameworkError


# the local ones
class FlowError(FrameworkError):
    """
    Base class for all flow exceptions
    """

    # public data
    description = "flow error: {0.error}"

    # meta-methods
    def __init__(self, node=None, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the error info
        self.node = node
        # all done
        return


class IncompleteFlowError(FlowError):
    """
    Exception raised when a request was made to compute a flow that has unbound products
    """

    # public data
    description = "incomplete flow error: factory {0.node} has unbound products"

    # meta-methods
    def __init__(self, **kwds):
        # chain up
        super().__init__(**kwds)
        # save the local info
        self.traits = tuple(traits)
        # all done
        return


# end of file
