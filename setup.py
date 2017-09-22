from distutils.core import setup
from distutils.extension import Extension
import sys

setup_args = {
    'name': 'geolambert',
    'packages': ['geolambert'],
}

if '--cython' in sys.argv:
    del sys.argv[sys.argv.index('--cython')]

    from Cython.Distutils import build_ext
    from Cython.Build import cythonize

    setup_args['ext_modules'] = cythonize([Extension('geolambert.clambert', ["geolambert/clambert/clambert.pyx"])])
    setup_args['cmdclass'] = {'build_ext': build_ext}
else:
    setup_args['ext_modules'] = [Extension('geolambert.clambert', ["geolambert/clambert/clambert.c"])]

setup(**setup_args)
