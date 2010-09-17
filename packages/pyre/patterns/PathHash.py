# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


import collections


class PathHash:
    """
    Implementation of a hash function for hierarchical namespaces with aliased entries.

    PathHash encodes the hierarchical relationships among its contents by having each node in
    the hierarchy store the names of the nodes that are its immediate children. Aliases are
    permitted and they hash to the same key as the original entry.

    PathHash does not provide storage for any values associated with the names of the various
    levelsin the hierarchy; that's the responsibility of the client. One implementation
    strategy is to create a dictionary at the client side that maps the keys generated by
    pathhash to the associated values.
    """


    def hash(self, key):
        """
        Retrieve the node given by {key}, assumed to be an iterable of address segments
        """
        # find the right spot
        node = self
        for part in key:
            node = node.nodes[part]
        # and return it
        return node


    def alias(self, alias, original):
        """
        Establish {alias} as alternative to {original}
        """
        # extract the hash key of the parent node
        address = alias[:-1]
        # the new name of the original node is the last chunk of the path
        newname = alias[-1]
        # hunt down the right parent node
        parent = self
        for part in address:
            parent = parent.nodes[part]
        # now find the original node
        node = self.hash(original)
        # create an entry for {newname} that points to the original
        parent.nodes[newname] = node
        # and return the original node
        return node


    def dump(self, graphic=''):
        """
        Dump out the names of all encountered nodes
        """
        for name, node in self.nodes.items():
            print("{}{!r}".format(graphic, name))
            node.dump(graphic=graphic+"  ")
        return


    # meta methods
    def __init__(self):
        self.nodes = collections.defaultdict(PathHash)
        return


    __slots__ = ["nodes"]


# end of file 
