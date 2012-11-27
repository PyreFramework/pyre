# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 2010-2012 all rights reserved
#
#


PROJECT = pyre

RECURSE_DIRS = \
    images \

#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


# end of file 