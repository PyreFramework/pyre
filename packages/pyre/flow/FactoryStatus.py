# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2019 all rights reserved
#


# my superclass
from .Status import Status


# declaration
class FactoryStatus(Status):
    """
    A helper that watches over the traits of factories and records value changes
    """


    # interface
    def addOutputBinding(self, factory, product):
        """
        Add {product} as an output of my {factory}
        """
        # add the {product} monitor to the pile of my observers
        return self.addObserver(observer=product.pyre_status)


    def removeOutputBinding(self, factory, product):
        """
        Remove {product} as an output of my {factory}
        """
        # remove the {product} monitor from my pile of observers
        return self.removeObserver(observer=product.pyre_status)


    def replaceInput(self, new, old):
        """
        Replace the {old} input with a {new} one
        """
        # remove me from the list of {old} observers
        old.pyre_status.removeObserver(observer=self)
        # and add to the list of {new} observers
        new.pyre_status.addObserver(observer=self)
        # if the {new} product is stale
        if new.pyre_stale:
            # mark the downstream graph
            self.flush(observable=new.pyre_status)
        # all done
        return


    def replaceOutput(self, new, old):
        """
        Replace the {old} output with a {new} one
        """
        # remove the {old} product from the list of my observers
        self.removeObserver(observer=old.pyre_status)
        # add the new one
        self.addObserver(observer=new.pyre_status)
        # and mark it
        new.pyre_stale = True
        # all done
        return


# end of file