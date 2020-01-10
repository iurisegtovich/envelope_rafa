#rename whichever setup_xxx.py to plain setup.py, then

cp setup_win.py setup.py

pip install . --global-option build_ext --global-option --compiler=mingw32