
import os

from conan import ConanFile
from conan.tools.gnu import AutotoolsToolchain, Autotools
from conan.tools.layout import basic_layout
from conan.tools.apple import fix_apple_shared_install_name

from conan.tools.files import get

class secp256k1Conan(ConanFile):
    name = "secp256k1"
    version = "0.2.34"

    # Optional metadata
    license = "MIT"
    author = ""
    url = "https://github.com/Gigamonkey-BSV/secp256k1-conan-recipe"
    description = "Optimized C library for EC operations on curve secp256k1 "
    topics = ("Ecliptical Curve", "secp256k1")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def source(self):
        get(self, "https://github.com/bitcoin-core/secp256k1/archive/refs/heads/master.zip",
                  strip_root=True)
        
    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        basic_layout(self)

    def generate(self):
        at_toolchain = AutotoolsToolchain(self)
        at_toolchain.generate()

    def build(self):
        autotools = Autotools(self)
        autotools.autoreconf()
        autotools.configure()
        autotools.make()

    def package(self):
        autotools = Autotools(self)
        autotools.install()
        fix_apple_shared_install_name(self)

    def package_info(self):
        self.cpp_info.libs = ["secp256k1"]
