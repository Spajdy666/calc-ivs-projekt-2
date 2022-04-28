#Makefile for second project from IVS
# Authors: RealRavers.txt
# Date: 28-04-2022

.PHONY: all compile pack run clean test doc reqs

#compile source files and run
all: compile run

#compile files (including profiling.py file)
compile:
	pip3 freeze

#execute
run: main.py
	python3 main.py

#pack files needed for assignment completion
pack:

clean:

#testing
test: mathlib_tests.py
	python3 mathlib_tests.py

#generating documentation
doc: Doxyfile
	doxygen -g Doxyfile

#install requiring packages
reqs:
	pip3 install PyQt5




