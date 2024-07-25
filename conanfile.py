from conans import ConanFile

class HelloWorldConan(ConanFile):
    name = "hello_world"  # Replace with your package name
    version = "1.0.0"  # Replace with your package version
    description = "A simple Hello World package"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*"

    def build(self):
        self.run("g++ -o hello_world hello_world.cpp")  # Assuming g++ is available

    def package(self):
        self.copy("hello_world", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello_world"]
