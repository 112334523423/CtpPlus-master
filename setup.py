# encoding:utf-8
import sys
import os
import shutil
import platform

from setuptools import setup
from Cython.Build import cythonize, build_ext
from Cython.Distutils import Extension as Cython_Extension

arch = platform.architecture()
if arch[0] == "64bit":
    myArch = "64"
elif arch[0] == "32bit":
    myArch = "32"
else:
    raise EnvironmentError("The architecture of platform is error.")

PRJ_NAME = "CtpPlus"
API_NAME = "CTP"

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
PRJ_DIR = os.path.join(CUR_DIR, PRJ_NAME)
API_DIR = os.path.join(PRJ_DIR, API_NAME)
CTP_LIB = os.path.join(API_DIR, "api")
C2CYTHON_HEADER = os.path.join(API_DIR, "c2cython")
CYTHON2C_HEADER = os.path.join(API_DIR, "cython2c")

package_data = []
extra_link_args = None
extra_compile_args = None

l_myOS = platform.system()
if l_myOS == "Linux":
    CTP_LIB = os.path.join(CTP_LIB, "linux" + myArch)
    package_data.append(os.path.join('CTP', 'api', 'linux' + myArch, '*.so'))
    # extra_compile_args = ["-Wall"]
    # extra_link_args = ['-Wl,-rpath,$ORIGIN']
    extra_compile_args = ["-std=c++11", "-Wall"]
    extra_link_args = ["-Wl,-rpath=$ORIGIN"]
elif l_myOS == "Windows":
    CTP_LIB = os.path.join(CTP_LIB, "windows" + myArch)
    package_data.append(os.path.join('CTP', 'api', 'windows' + myArch, '*.dll'))
    extra_compile_args = ["/GR", "/EHsc"]
    extra_link_args = []
else:
    print("不支持的操作系统")
    sys.exit(1)

common_args = {
    "cython_include_dirs": [CYTHON2C_HEADER, C2CYTHON_HEADER],
    "include_dirs": [CTP_LIB, C2CYTHON_HEADER],
    "library_dirs": [CTP_LIB],
    "language": "c++",
    "extra_compile_args": extra_compile_args,
    "extra_link_args": extra_link_args,
}

l_setup_ext_modules = cythonize([Cython_Extension(name="CtpPlus.CTP.MdApiBase",
                                                  sources=[os.path.join(API_DIR, "MdApiBase.pyx")],
                                                  language='c++',
                                                  include_dirs=common_args['include_dirs'],
                                                  library_dirs=common_args['library_dirs'],
                                                  libraries=["thostmduserapi_se"],
                                                  extra_compile_args=extra_compile_args,
                                                  extra_link_args=extra_link_args),
                                 Cython_Extension(name="CtpPlus.CTP.TraderApiBase",
                                                  sources=[os.path.join(API_DIR, "TraderApiBase.pyx")],
                                                  language='c++',
                                                  include_dirs=common_args['include_dirs'],
                                                  library_dirs=common_args['library_dirs'],
                                                  libraries=["thosttraderapi_se"],
                                                  extra_compile_args=extra_compile_args,
                                                  extra_link_args=extra_link_args)
                                 ],
                                compiler_directives={'language_level': 3, "binding": True}
                                )

setup(
    name=PRJ_NAME,
    version="1.0",
    author='jyl',
    author_email='',
    license="",
    url='',
    description='CTP官方API的封装的Python版。',
    long_description='''
        从以下三个不同的维度实现低延时：
        1. 利用Cython技术释放了GIL；
        2. 同时支持接入多路行情源，降低轮询等待时间；
        3. 利用CTP的线程特性，以接口回调直接驱动策略运行，无需主事件引擎，真正实现去中心化。
        ''',
    keywords="CTP程序化交易",
    platforms=["Windows", "Linux"],
    python_requires=">=3.7",
    include_dirs=[CTP_LIB, CYTHON2C_HEADER],
    packages=["CtpPlus", "CtpPlus.CTP", "CtpPlus.utils", "CtpPlus.ta", "CtpPlus.examples"],
    ext_modules=l_setup_ext_modules,
    package_data={"CtpPlus": package_data},
    zip_safe=False,
)
