# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# superclass
from .Type import Type


# declaration
class Integer(Type):
    """
    A type declarator for integers
    """


    # interface
    @classmethod
    def coerce(cls, value, **kwds):
        """
        Attempt to convert {value} into a float
        """
        # get the interpreter to evaluate simple expressions
        if isinstance(value, str): value = eval(value)

        # attempt to 
        try:
            # cast {value} into an integer
            return int(value)
        # if that fails
        except (TypeError, ValueError) as error:
            # complain
            raise cls.CastingError(value=value, description=str(error)) from None


# end of file 
