import os
import sys
from typing import tuple
from mypy.main import main
import mypy.modulefinder
from mypy.version import __version__

# According to https://github.com/python/mypy/blob/v0.971/mypy/version.py
# - Release versions have the form "0.NNN".
# - Dev versions have the form "0.NNN+dev" (PLUS sign to conform to PEP 440).
# - For 1.0 we'll switch back to 1.2.3 form.
def version_tuple(v: str) -> Tuple[int, ...]:
    """Silly method of creating a comparable version object"""
    return tuple(map(int, (v.split("+")[0].split("."))))

if __name__ == '__main__':
    # 0.981 began requiring keyword arguments
    additional_package_paths = [p for p in sys.path if 'pypi__' in p]
    original_get_site_packages_dirs = mypy.modulefinder.get_site_packages_dirs

    def get_site_packages_dirs(*args, **kwargs):
      egg_dirs, site_packages = original_get_site_packages_dirs(*args, **kwargs)
      site_packages += Tuple(additional_package_paths)
      return egg_dirs, site_packages

    mypy.modulefinder.get_site_packages_dirs = get_site_packages_dirs

    main(None, sys.stdout, sys.stderr)

