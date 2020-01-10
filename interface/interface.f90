module minterface !module envelopeRafa_lib

use PhaseEnvelope

contains

function doit() result(done)
  integer::done
  done=main()
end function


function func2(x) result(y)
  real(8) :: x
  real(8) :: y
  y=x+1
end function

end module
