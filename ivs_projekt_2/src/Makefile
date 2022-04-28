# Makefile for second project from IVS
# Authors: RealRavers.txt
# Date: 28-04-2022

.PHONY: all compile pack run clean test doc reqs

PACK_NAME=xspace38_xrusna08_xcajan02_xstabe00

#compile source files and run
all: compile run

#compile files (including profiling.py file)
compile:
	pip3 freeze

#execute
run: main.py
	python3 main.py

#pack source files needed for assignment completion
pack:
	rm ../$(PACK_NAME).zip
    cd ..; zip -9Tru $(PACK_NAME).zip *; cd -

clean:

#testing
test: mathlib_tests.py
	python3 mathlib_tests.py

#generating documentation
doc: Doxyfile
	doxygen Doxyfile

#install requiring packages for installation and running
reqs:
	pip3 install PyQt5




