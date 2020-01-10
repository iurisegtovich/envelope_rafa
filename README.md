# python_solution

a project template for building a fortran extension to a python package

1.  download it:

git clone https://github.com/iurisegtovich/python_solution.git

cd python_solution

python setup.py build build_ext --inplace --compiler=mingw32

python setup.py install

---

? python -m pip install -e git+https://github.com/iurisegtovich/iurisegtovich_lab.git@master#egg=iurisegtovich_lab_iurisegtovich
> vai criar uma pasta src/iurisegtovich_lab, não pode mover/renomear ela

? python setup.py sdist bdist_wheel


#--------------------------------------------------------

pip install . --install-option
pip install . --global-option
>--platform Defaults to the platform of the running system. #no mess here
>https://stackoverflow.com/questions/47210058/passing-command-line-arguments-to-pip-install


