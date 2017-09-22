import os
dir_path = os.path.dirname(os.path.realpath(__file__))

import pyximport
pyximport.install(setup_args={'include_dirs': [dir_path]})
from .clambert import xyToWgs84

__all__ = ['clambert.xyToWgs84']