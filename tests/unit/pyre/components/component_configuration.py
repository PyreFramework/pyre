#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


"""
A more elaborate component declaration
"""


def declare():
    import pyre.components
    from pyre.components.Component import Component
    from pyre.components.Property import Property

    class component(Component, family="sample.configuration"):
        """a test component"""
        # properties
        p1 = Property()
        p1.default = "p1"

        p2 = Property()
        p2.default = "p2"

        # behaviors
        @pyre.components.export
        def do(self):
            """behave"""
            return True
      
    return component


def test():
    component = declare()
    # check that the setting were read properly
    assert component._pyre_Inventory.p1.value == "sample - p1"
    assert component._pyre_Inventory.p2.value == "sample - p2"
    # and return the executive and the component
    return component
    

# main
if __name__ == "__main__":
    test()


# end of file 
