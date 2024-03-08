@echo off

del .\CtpPlus\CTP\*.cpp  /F

rd/s/q .\build
rd/s/q .\dist
rd/s/q .\CtpPlus.egg-info

set nls_lang=SIMPLIFIED CHINESE_CHINA.UTF8
python setup.py sdist bdist_wheel

del .\CtpPlus\CTP\*.cpp  /F
rd/s/q .\build
rd/s/q .\CtpPlus.egg-info
pause