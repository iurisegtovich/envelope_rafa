#1 from pip install git+

pip install git+https://github.com/iurisegtovich/envelope_rafa --install-option='--someopt=windows'
pip install git+https://github.com/iurisegtovich/envelope_rafa --install-option='--someopt=linux' --global-option build_ext --global-option --compiler=mingw32

#2 from git clone / pip intall .

#3 test:

git clone --single-branch --branch test https://github.com/iurisegtovich/envelope_rafa
