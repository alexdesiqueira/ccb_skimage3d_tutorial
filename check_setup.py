import sys
from distutils.version import LooseVersion

EXIT_ERROR = 1


def check_python_version():
    if (sys.version_info.major < 3) or (sys.version_info.minor < 7):
        print("[!] You are running an unsupported version of Python. "
              "This tutorial requires Python version 3.7 or newer.")

        sys.exit(EXIT_ERROR)
    return None


def read_requirements(filename="requirements.txt"):
    with open(filename) as file_reqs:
        requirements = file_reqs.readlines()

    requirements = [
        (package, version) for (package, _, version) in
        (requirement.split()
            for requirement in requirements if requirement.strip())
        ]
    return requirements


def check_setup():
    pkg_names = {
        "jupyter-notebook": "notebook",
        "scikit-image": "skimage",
    }

    check_python_version()
    requirements = read_requirements()

    for (package, version_required) in requirements:
        module_name = pkg_names.get(package, package)
        try:
            module = __import__(module_name)
            status = "✓"
        except ImportError as e:
            module = None
            if (package != "numpy" and "numpy" in str(e)):
                status = "?"
                version_installed = "Needs NumPy"
            else:
                version_installed = "Not installed"
                status = "X"

        if module is not None:
            try:
                version_installed = module.__version__
            except AttributeError:  # specific for ITK version
                version_installed = module.Version.GetITKVersion()

            if LooseVersion(version_required) > LooseVersion(version_installed):
                status = "X"
        print("[{}] {:<10} {}".format(
            status, package.ljust(16), version_installed)
        )


if __name__ == '__main__':
    check_setup()
