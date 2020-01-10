OBJECTS = \
../library/PhaseEnvelope.o \
../library/EOS.o \
../library/GaussElimination.o \
../library/cubic_solver.o \

build:
	f2py -m envelope_rafa -h interface.pyf interface.f90 --overwrite-signature
	f2py --fcompiler=gfortran --compiler=mingw32 -c interface.pyf interface.f90 $(OBJECTS) --opt='-ffree-line-length-none -I../library'
	cp -rf envelope_rafa*.pyd ../envelope_rafa_pkg/

