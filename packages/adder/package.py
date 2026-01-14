from spack.package import *

class Adder(PythonPackage):
    """ADDER is a Python-based fuel management and depletion tool."""

    homepage = "https://github.com/anl-rtr/adder"
    git = "https://github.com/anl-rtr/adder.git"

    version("develop", branch="main")

    # Imports
    import_modules = ["adder"]

    extends("python")

    # README-required Python deps
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-configobj", type=("build", "run"))
    depends_on("py-pyparsing", type=("build", "run"))

    # External dependency 
    depends_on("mcnptools", type=("build", "run"))

    # Stand-alone smoke test (for `spack test run adder`)
    def test_cli_help(self):
        adder = which("adder", required=True)
        adder("--help")

