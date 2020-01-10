#linux installs with
#pip install -vvv .

#? pip install -vvv . --global-option=build_py
#?pip install -vvv . --global-option build_ext 

import setuptools

import os
import subprocess

import setuptools
from setuptools import setup

from setuptools.command.build_py import build_py
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install



with open("README.md", "r") as fh:
    long_description = fh.read()


def build_extensions():
    """
    Instead of fighting with numpy.distutils (see
    https://stackoverflow.com/a/41896134), we use our Makefile which we know
    works well (OpenMP etc, see "make help") and copy the *.so files using the
    package_data trick below. Makefile will copy the *.so files so
    we just need to tell setuptools that these are "data files" that we wish to
    copy when installing, along with all *.py files.
    on windows requires mingw and make that can be installed from conda
    conda install -c conda-forge  m2w64-toolchain_win-64
    conda install -c conda-forge  make
    """
    global someopt
    if someopt == 'windows':
        subprocess.run(r"make -C library -f Makefile_win.mak && make -C interface -f Makefile_win.mak", shell=True, check=True)
    elif someopt == 'linux':
        subprocess.run(r"make -C library && make -C interface", shell=True, check=True)
    else:
        print("TRY WITH <pip install -vvv . --install-option='--someopt=windows'>")
        print("TRY WITH <pip install -vvv . --install-option='--someopt=linux'>")

def make_cmd_class(base):
    """
    Call build_extensions() in "python setup.py <base>" prior to anything else.
    base = build_py, install, develop, ..., i.e. a setup.py command. Use in
    setup(cmdclass={'<base>': make_cmd_class(<base>)}, ...).

    Parameters
    ----------
    base : setuptools.command.<base>.<base> instance

    Notes
    -----
    https://stackoverflow.com/a/36902139
    """
    class CmdClass(base):
        def run(self):
            build_extensions()
            super().run()

    return CmdClass

class InstallCommand(install):
    user_options = install.user_options + [
        ('someopt=', None, None), # a 'flag' option
        ('someval=', None, None) # an option that takes a value
    ]

    def initialize_options(self):
        install.initialize_options(self)
        self.someopt = None
        self.someval = None

    def finalize_options(self):
        print("value of someopt is", self.someopt)
        print("value of someval is", self.someval)
        install.finalize_options(self)
    def run(self):
        global someopt
        global someval
        someopt = self.someopt # will be 1 or None
        someval = self.someval # will be 1 or None
        install.run(self)
    




setup(
    name='envelope_rafa_pkg',
    version='0.2.0',
    description='example',
    long_description=long_description,
    url='https://github.com/iurisegtovich/envelope_rafa',
    author='iuri segtovich',
    author_email='iurisegtovich@gmail.com',
    license='BSD 3-Clause',
    keywords='example',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    setup_requires=['numpy'], #also requires conda' mingw and make
    python_requires='>=3',
    package_data={'envelope_rafa_pkg': ['envelope_rafa*.so','envelope_rafa*.pyd']}, #ship libraries, whatever made!
    include_package_data=True,
    cmdclass={
        'build_py': make_cmd_class(build_py),
        'install': InstallCommand,
        },
)

