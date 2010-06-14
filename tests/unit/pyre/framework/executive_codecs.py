#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
Sanity check: verify that the codec manager can be instantiated
"""


def test():
    import pyre.framework
    # build the executive
    executive = pyre.framework.executive()

    # access the codec manager
    codecs = executive.codecs
    assert codecs is not None

    # all done
    return executive


# main
if __name__ == "__main__":
    test()


# end of file 
