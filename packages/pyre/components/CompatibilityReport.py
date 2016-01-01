# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2016 all rights reserved
#


import collections


class CompatibilityReport:
    """
    Class that holds the assignment incompatibilities among configurables
    """


    # public data
    this = None # the target of the search
    other = None # the specification we are trying to match


    # meta methods
    def __init__(self, this, other, **kwds):
        super().__init__(**kwds)

        self.this = this
        self.other = other
        self.incompatibilities = collections.defaultdict(list)

        return


    def __bool__(self):
        """
        Convert to True if no incompatibilities were reported
        """
        return len(self.incompatibilities) == 0


# end of file
