# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# superclass
from .Facility import Facility


# declaration
class Catalog(Facility):
    """
    A component container
    """


    # value coercion
    def instantiate(self, node, value, **kwds):
        """
        Attach a component catalog as my trait value
        """
        # initialize the component index, a {dict} for now; it's not useful to remember the
        # order in which these settings were encountered, because what you really want is a
        # container sorted by the priorities of the settings
        index = dict()
        # get my target key
        key = node.key
        # if it is unregistered, there is nothing to do
        if not key: return index

        # get my protocol
        protocol = self.schema
        # use it to get the executive
        executive = protocol.pyre_executive
        # the nameserver
        nameserver = executive.nameserver
        # and the configurator
        configurator = executive.configurator
        # get the full name of my slot
        _, slotName = nameserver.lookup(key)

        # go through the children of this key
        for childKey, childNode in nameserver.children(key):
            # look up the name of the node
            _, childName = nameserver.lookup(childKey)
            # take it apart and keep the trailing part
            tag = nameserver.split(childName)[-1]
            # store the (tag, value) pair in my index
            index[tag] = super().instantiate(node=childNode, value=childNode.value)

        # now, for the deferred assignments
        for assignment, priority in configurator.deferred[key]:
            # for each condition
            for name, family in assignment.conditions:
                # hash them
                name = nameserver.hash(name)
                family = nameserver.hash(family)
                # get the class record of the referenced component
                target = type(nameserver[name])
                # verify
                if target.pyre_inventory.key is not family: break
            # if they all passed
            else:
                # get the name of this entry
                tag = nameserver.join(*assignment.key)
                # for each candidate
                for entry in self.resolve(value=assignment.value, locator=assignment.locator):
                    # if is assignment compatible with my protocol
                    if entry.pyre_isCompatible(protocol):
                        # if it's a component class
                        if isinstance(entry, self.actor):
                            # build its name
                            name = nameserver.join(slotName, tag)
                            # instantiate it
                            entry = entry(name=name, locator=assignment.locator)
                        # place it in the index
                        index[tag] = entry

        # store the index as my value
        return index
    

# end of file 