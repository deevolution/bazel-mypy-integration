import os
import sys
from mypy.main import main
import mypy.modulefinder
from mypy.version import __version__

if __name__ == '__main__':
    additional_package_paths = [p for p in sys.path if 'pypi__' in p]
    original_get_site_packages_dirs = mypy.modulefinder.get_site_packages_dirs

    def get_site_packages_dirs(*args, **kwargs):
      egg_dirs, site_packages = original_get_site_packages_dirs(*args, **kwargs)
      site_packages += tuple(additional_package_paths)
      return egg_dirs, site_packages

    mypy.modulefinder.get_site_packages_dirs = get_site_packages_dirs

    main(None, sys.stdout, sys.stderr)

