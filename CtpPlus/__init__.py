# encoding:utf-8
import platform
import os


def find_lib():
    dll_dir = ''

    arch = platform.architecture()
    if arch[0] == "64bit":
        myArch = "64"
    elif arch[0] == "32bit":
        myArch = "32"
    else:
        raise EnvironmentError("The architecture of platform is error.")

    l_myOS = platform.system()
    if l_myOS == "Linux":
        dll_dir = os.path.join(os.path.dirname(__file__), 'CTP', 'api', 'linux' + myArch)
    elif l_myOS == "Windows":
        dll_dir = os.path.join(os.path.dirname(__file__), 'CTP', 'api', 'windows' + myArch)

    path = dll_dir + os.pathsep

    os.environ['PATH'] = path
    os.environ['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'  # py3.10版本


find_lib()
del find_lib

