FC = gfortran
FFLAGS =  -g -fbacktrace -fcheck=array-temps -fcheck=bounds -fcheck=do -fcheck=mem -cpp -fmax-errors=1 -ffree-line-length-0 -Wall -fimplicit-none -O0

all:
	$(FC) $(FFLAGS) -fPIC -fno-second-underscore -o GaussElimination.o -c GaussElimination.f90
	$(FC) $(FFLAGS) -fPIC -fno-second-underscore -o cubic_solver.o -c cubic_solver.f90
	$(FC) $(FFLAGS) -fPIC -fno-second-underscore -o EOS.o -c EOS.f90
	$(FC) $(FFLAGS) -fPIC -fno-second-underscore -o PhaseEnvelope.o -c PhaseEnvelope.f90



