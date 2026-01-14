# Platform Nine Quarters

[**Experimental Alpha Release**]

[Morton Labs AI](https://www.mortonlabs.ai/) is a computational
science company from the University of Chicago focused on accelerating
fusion energy development with a multi-physics simulation platform.

The Platform Nine Quarters provides a Virtual Test Bed (VTB)
environment to design, validate and optimize available Free and Open
Source fusion software.

The systems-engineering and integration efforts for the fusion
simulation stack includes relevant physics from plasma behavior,
neutronics, thermal-hydraulics, structural mechanics, material
response, electromagnetism and simulation of these environments.

We are continuing to work in making 100+ packages available for
nuclear fusion research for the benefit of academic users,
universities, private fusion companies, national laboratories and the
community at large.

## Objectives

Our mission is to reduce the time and cost it takes to design,
validate and optimize fusion energy systems by building and
maintaining the digital infrastructure for physics codes into usable,
well-validated multi-physics workflows.

The key objectives include:

1. Interoperability
2. Comprehensive test coverage
3. Verification and Validation
4. Performance benchmarking
5. Legacy Code Support
6. Porting Code bases

## Quick Start

On Rocky Linux 10 (x86_64):

### Pre-requisites

```bash
$ sudo dnf update
$ sudo dnf install git make patch bash tar yum gzip unzip bzip2 xz file gnupg2 git gawk python3
$ sudo dnf group install "Development Tools"
$ sudo dnf install gcc gcc-gfortran gcc-c++
```

### Install Spack

```bash
$ git clone --depth=2 https://github.com/spack/spack.git

$ . spack/share/spack/setup-env.sh

$ spack -V
1.2.0.dev0 (d9071ea6be97ea9976bce1eace84db255703777e)
```

### Install compiler

```bash
$ spack compiler list
$ spack compiler find

Added 1 new compiler to /home/morton/.spack/packages.yaml
    gcc@14.3.1
==> Compilers are defined in the following files:
    /home/morton/.spack/packages.yaml
```

### Add develop mirror

```bash
$ spack mirror add develop https://binaries.spack.io/develop
$ spack buildcache keys --install --trust
```

### Clone this repository

```bash
$ git clone https://github.com/Morton-Lab-AI/nine-quarters morton
$ spack repo add ~/morton
==> Added repo to config with name 'morton'

$ spack repo list
[+] morton v1.0 ~/morton
[+] builtin v2.2 ~/.space/package_repos/fncqgg4/repos/spack_repo/builtin
```

### Create testbed

```bash
$ spack env create testbed
$ spack env activate testbed
$ spack install -v --add mcnptools +python

$ spack find
```

## Authors

Many thanks to Spack's [contributors](https://github.com/spack/spack/graphs/contributors).

## License

The platform is distributed under both the MIT license and the Apache
License (Version 2.0), similar to Spack. Users may choose either
license, at their option.

All new contributions must be made under both the MIT and Apache-2.0 licenses.

## Contributing

You can create pull requests to this repository to contribute to the project.

Please feel free to create any issues or feature requests.

If you are interested in learning more about us, please write to
zach@mortonlabs.ai.