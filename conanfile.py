import os
import shutil
from conans import ConanFile, tools, CMake


class rttrConan(ConanFile):
    name = "rttr"
    version = "0.9.7-dev"
    license = "MIT License"
    homepage = "https://www.github.com/ulricheck/rttr"
    description = """rttr project"""
    url = "https://github.com/ulricheck/conan-rttr"

    generators = "cmake"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "rtti": [True, False],
        }

    default_options = (
        "shared=True", 
        "rtti=True", 
    )

    scm = {
        "type": "git",
        "subfolder": "rttr",
        "url": "https://github.com/ulricheck/rttr.git",
        "revision": "master"
    }



    def _cmake_configure(self):
        cmake = CMake(self)
        cmake.definitions["DBUILD_STATIC"] = not self.options.shared
        cmake.definitions["BUILD_WITH_RTTI"] = self.options.rtti
        cmake.configure(source_dir='rttr')
        return cmake


    def build(self):
        cmake = self._cmake_configure()
        cmake.build()

    def package(self):
        cmake = self._cmake_configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["rttr_core_d"] if self.settings.build_type == "Debug" else ["rttr_core"]
