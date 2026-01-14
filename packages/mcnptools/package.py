# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mcnptools(CMakePackage):
    """MCNPTools is a C++ library with SWIG-generated Python bindings and utilities
    for working with MCNP output files and related workflows.
    """

    homepage = "https://github.com/lanl/mcnptools"
    git = "https://github.com/lanl/mcnptools.git"

    license("BSD-3-Clause")

    # Upstream tags
    version("develop", branch="main")
    version("5.3.1", tag="v5.3.1")
    version("5.3.0", tag="v5.3.0")

    maintainers("shakthimaan")

    # Variants
    variant(
        "python",
        default=True,
        description="Build and install SWIG-generated Python bindings",
    )

    variant(
        "python_install",
        default="User",
        values=("User", "System"),
        multi=False,
        description=(
            "Value passed to -Dmcnptools.python_install. "
            "Upstream examples use 'User'."
        ),
        when="+python",
    )

    # Build dependencies
    depends_on("cmake@3.1:", type="build")
    depends_on("pkgconfig", type="build")

    # C++ build requirements
    depends_on("python@3:", type=("build", "run"), when="+python")
    depends_on("swig@3:", type="build", when="+python") 

    # Some MCNPTools tests/bindings commonly expect NumPy in Python environments.
    depends_on("py-numpy", type=("test", "run"), when="+python")

    def cmake_args(self):
        args = []

        if "+python" in self.spec:
            args.append(self.define("mcnptools.python_install", self.spec.variants["python_install"].value))
        else:
            args.append(self.define("mcnptools.enable_python", False))

        return args

    def check(self):
        # Use CTEST_OUTPUT_ON_FAILURE for actionable CI logs.
        with working_dir(self.build_directory):
            ctest(
                "--output-on-failure",
                env={"CTEST_OUTPUT_ON_FAILURE": "1"},
            )

    def test(self):
        """Spack `spack test run mcnptools` hook.

        We run ctest again post-install as a lightweight confirmation that the
        build tree remains testable in the staged test environment.
        """
        self.check()
