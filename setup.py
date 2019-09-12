from setuptools import setup, Extension

gpio = Extension(
    "mipea.gpio",
    sources = ["mipea/gpiomodule.c"],
    libraries = ["mipea"],
    language = "c"
)

setup(
    name = "mipea",
    version = "0.0.1",
    description = "minimalistic peripheral access for the Raspberry Pi",
    author = "jasLogic",
    author_email = "jaslo@jaslogic.tech",
    # url =
    packages = ["mipea"],
    ext_modules = [gpio],
)
