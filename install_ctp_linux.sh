rm -rf ./CtpPlus/CTP/*.cpp

rm -rf  ./build
rm -rf  ./dist
rm -rf  ./CtpPlus.egg-info

python setup.py sdist bdist_wheel

rm -rf ./CtpPlus/CTP/*.cpp
rm -rf  ./build
rm -rf  ./CtpPlus.egg-info