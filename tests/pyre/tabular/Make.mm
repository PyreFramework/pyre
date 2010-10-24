# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity records sheets

sanity:
	${PYTHON} ./sanity.py

records:
	${PYTHON} ./record.py
	${PYTHON} ./record_accessors.py
	${PYTHON} ./record_csv.py
	${PYTHON} ./record_csv_partial.py

sheets:
	${PYTHON} ./sheet.py
	${PYTHON} ./sheet_class_layout.py
	${PYTHON} ./sheet_class_inheritance.py
	${PYTHON} ./sheet_class_inheritance_multi.py
	${PYTHON} ./sheet_class_record.py
	${PYTHON} ./sheet_class_inheritance_record.py
	${PYTHON} ./sheet_instance.py
	${PYTHON} ./sheet_instance_populate.py


# end of file 
