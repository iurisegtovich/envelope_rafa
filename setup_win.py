import setuptools

import os
import subprocess

import setuptools
from setuptools import setup
from setuptools.command.build_py import build_py


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
    """
    subprocess.run(r"make -C library -f Makefile_win.mak && make -C interface -f Makefile_win.mak", shell=True, check=True)


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


setup(
    name='python_solution_pkg',
    version='0.1.0',
    description='example',
    long_description=long_description,
    url='https://github.com/iurisegtovich/python_solution',
    author='iuri segtovich',
    author_email='iurisegtovich@gmail.com',
    license='BSD 3-Clause',
    keywords='example',
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    setup_requires=['numpy'],
    python_requires='>=3',
    package_data={'python_solution_pkg': ['python_solution*.pyd']},
    include_package_data=True,
    cmdclass={
        'build_py': make_cmd_class(build_py),
        },
)

