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
	cd ../..; zip -9Tru $(PACK_NAME).zip $(PACK_NAME); cd -

#remove all files that shouldn't be in the final assignment
clean:
	rm -r calc_1.0_amd64.* calc-1.0/debian calc-1.0/*.py rm ../$(PACK_NAME).zip
	
#testing
test: mathlib_tests.py
	python3 mathlib_tests.py

#generating documentation
doc: Doxyfile
	doxygen Doxyfile

#install requiring packages for installation and running
reqs:
	sudo pip3 install PyQt5
	sudo apt install python3-pip
	sudo pip3 install PyQt5
	sudo apt-get install ibxcb-xinerama0

installer:
	cp *.py calc-1.0
	cd calc-1.0; dh_make -n -s -c gpl -f ../calc-1.0.tar.gz;cd -
	cp calc-1.0/dbn/install calc-1.0/debian/
	cd calc-1.0; dpkg-buildpackage -rfakeroot -uc -b; cd -



