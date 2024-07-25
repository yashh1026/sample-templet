from conans import ConanFile, tools

class MyPrecompiledLibConan(ConanFile):
    name = "my_precompiled_lib" 
    version = "1.0.0"
    description = "My pre-compiled library"
    license = "MIT" 
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*" 

    def package(self):
        self.copy("*", dst="include", src="include")  # Include headers
        self.copy("*", dst="lib", src="lib")    # Copy library binaries
        self.copy("*", dst="bin", src="bin")   # Copy executables (if any)
        
    def package_info(self):
        self.cpp_info.libs = ["my_precompiled_lib"] # Add any required libs
        self.cpp_info.includedirs = ["include"] # Add include dirs
