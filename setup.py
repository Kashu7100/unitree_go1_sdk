"""Build the `robot_interface` pybind11 extension into a wheel.

Compiles the single python_wrapper/python_interface.cpp against the prebuilt
architecture-specific static library shipped in lib/cpp/<arch>/. Uses a modern
pybind11 (the vendored 2.6 copy is too old for Python >= 3.11).
"""
import platform

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

machine = platform.machine().lower()
if machine in ("x86_64", "amd64"):
    arch = "amd64"
elif machine in ("aarch64", "arm64"):
    arch = "arm64"
else:
    raise RuntimeError(f"Unsupported architecture: {platform.machine()}")

ext_modules = [
    Pybind11Extension(
        "robot_interface",
        ["python_wrapper/python_interface.cpp"],
        include_dirs=["include"],
        library_dirs=[f"lib/cpp/{arch}"],
        # Static SDK lib first, then the system libs it depends on (order matters).
        libraries=["unitree_legged_sdk", "pthread", "rt", "m"],
        extra_compile_args=["-O3", "-pthread"],
        cxx_std=14,
    )
]

setup(ext_modules=ext_modules, cmdclass={"build_ext": build_ext})
