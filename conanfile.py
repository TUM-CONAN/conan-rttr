from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout, CMakeDeps
from conan.tools.scm import Git
from conan.tools.files import load, update_conandata, copy, replace_in_file, collect_libs
import os



class rttrConan(ConanFile):
    name = "rttr"
    version = "0.9.7-dev"
    license = "MIT License"
    homepage = "https://www.github.com/ulricheck/rttr"
    description = """rttr project"""
    url = "https://github.com/ulricheck/conan-rttr"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "rtti": [True, False],
        }

    default_options = {
        "shared": True,
        "rtti": True,
    }

    def export(self):
        update_conandata(self, {"sources": {
            "commit": "master",
            "url": "https://github.com/ulricheck/rttr.git"
        }})

    def source(self):
        git = Git(self)
        sources = self.conan_data["sources"]
        git.clone(url=sources["url"], target=self.source_folder)
        git.checkout(commit=sources["commit"])

    def generate(self):
        tc = CMakeToolchain(self)

        def add_cmake_option(option, value):
            var_name = "{}".format(option).upper()
            value_str = "{}".format(value)
            var_value = "ON" if value_str == 'True' else "OFF" if value_str == 'False' else value_str
            tc.variables[var_name] = var_value

        for option, value in self.options.items():
            add_cmake_option(option, value)

        tc.cache_variables["BUILD_STATIC"] = not self.options.shared
        tc.cache_variables["BUILD_WITH_RTTI"] = self.options.rtti
        tc.cache_variables["BUILD_EXAMPLES"] = False
        tc.cache_variables["BUILD_BENCHMARKS"] = False
        tc.cache_variables["BUILD_UNIT_TESTS"] = False
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self, src_folder="source_folder")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        #self.cpp_info.libs = collect_libs(self)
        self.cpp_info.libs = ["rttr_core_d"] if self.settings.build_type == "Debug" else ["rttr_core"]
