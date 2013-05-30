#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Verify that syntax errors in expressions are caught
"""


def test():
    import pyre.algebraic

    # build a model
    model = pyre.algebraic.model()

    # escaped macro delimiters
    node = model.expression("{{production}}")
    # it should have made a variable
    assert type(node) is model.node.variable

    # and another
    node = model.expression("{{{{cost per unit}}}}")
    # it should have made a variable
    assert type(node) is model.node.variable

    # finally
    tricky = model.expression("{{{number of items}}}")
    # it should have made an expression
    assert type(tricky) is model.node.expression
    # with an unresolved reference
    try:
        tricky.value
        assert False
    except tricky.UnresolvedNodeError:
        pass

    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # run the test
    test()


# end of file 