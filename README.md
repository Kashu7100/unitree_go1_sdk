# v3.8.6
The unitree_legged_sdk is mainly used for communication between PC and Controller board.
It also can be used in other PCs with UDP.

### Notice
support robot: Go1

not support robot: Laikago, B1, Aliengo, A1. (Check release [v3.3.1](https://github.com/unitreerobotics/unitree_legged_sdk/releases/tag/v3.3.1) for support)

### Dependencies
* [Unitree](https://www.unitree.com/download)
```bash
Legged_sport    >= v1.36.0
firmware H0.1.7 >= v0.1.35
         H0.1.9 >= v0.1.35
```
* [Boost](http://www.boost.org) (version 1.5.4 or higher)
* [CMake](http://www.cmake.org) (version 2.8.3 or higher)
* [g++](https://gcc.gnu.org/) (version 8.3.0 or higher)


### Build
```bash
mkdir build
cd build
cmake ..
make
```

If you want to build the python wrapper, then replace the cmake line with:
```bash
cmake -DPYTHON_BUILD=TRUE ..
```

If can not find pybind11 headers, then add
```bash
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/third-party/pybind11/include)
```
at line 14 in python_wrapper/CMakeLists.txt.

If can not find msgpack.hpp, then
```bash
sudo apt install libmsgpack*
```

### Build a Python wheel (Python 3.8 – 3.12)

The legacy CMake path above vendors pybind11 2.6, which does **not** compile on
Python >= 3.11. To build an installable wheel for a modern interpreter, use the
`pyproject.toml` / `setup.py` at the repo root instead. They compile
`python_wrapper/python_interface.cpp` against a current pybind11 (pulled in
automatically as a build dependency) and link the prebuilt static library in
`lib/cpp/<arch>/`.

```bash
# Builds dist/unitree_legged_sdk-*-cp<ver>-...-<arch>.whl for the chosen Python.
pip install build
python3.12 -m build --wheel        # or python3.11, python3.10, ...
pip install dist/unitree_legged_sdk-*.whl
```

Then `import robot_interface` works without touching `sys.path`. The wheel is
architecture-specific (built for the host arch: `amd64` on x86_64, `arm64` on
aarch64) and links the matching `lib/cpp/<arch>/libunitree_legged_sdk.a`.

### Run

#### Cpp
Run examples with 'sudo' for memory locking.

#### Python
##### arm
change `sys.path.append('../lib/python/amd64')` to `sys.path.append('../lib/python/arm64')`
