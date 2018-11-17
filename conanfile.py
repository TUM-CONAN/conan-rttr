import os
import shutil
from conans import ConanFile, tools, CMake


class rttrConan(ConanFile):
    name = "rttr"
    version = "0.11-dev"
    license = "MIT License"
    homepage = "https://www.github.com/rttrorg/rttr"
    description = """rttr project"""
    url = "https://github.com/ulricheck/conan-rttr"

    generators = "cmake"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False], 
        }

    default_options = (
        "shared=True", 
    )

    scm = {
        "type": "git",
        "subfolder": "rttr",
        "url": "https://github.com/rttrorg/rttr.git",
        # "revision": "rttrorg-rttr-%s"% version
        "revision": "master"
     }


    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir='rttr')
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ['rttr_core']
