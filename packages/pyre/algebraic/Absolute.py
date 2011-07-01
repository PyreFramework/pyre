# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Unary import Unary


class Absolute(Unary):
    """
    A representation of the absolute value
    """


    # interface
    def pyre_eval(self, **kwds):
        # compute the value of my operand
        op = self.op.pyre_eval(**kwds)
        # compute its absolute value and return it
        return abs(op)


    # meta methods
    def __str__(self):
        return "abs({0.op})".format(self)


# end of file 
