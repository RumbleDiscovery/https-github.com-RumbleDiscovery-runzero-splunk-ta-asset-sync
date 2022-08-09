#!/usr/bin/python
"""
This file was generated by AoB originally.
"""
import os
import sys
import re

if sys.version_info[0] < 3:
    py_version = "aob_py2"
else:
    py_version = "aob_py3"

ta_name = 'TA_runzero_asset_sync'
ta_lib_name = 'TA_runzero_asset_sync'
pattern = re.compile(r"[\\/]etc[\\/]apps[\\/][^\\/]+[\\/]bin[\\/]?$")
new_paths = [path for path in sys.path if not pattern.search(path) or ta_name in path]
new_paths.insert(0, os.path.sep.join([os.path.dirname(__file__), ta_lib_name]))
new_paths.insert(0, os.path.sep.join([os.path.dirname(__file__), ta_lib_name, py_version]))
sys.path = new_paths

import cloudconnectlib.splunktacollectorlib.cloud_connect_mod_input as mod_input

if __name__ == "__main__":
    mod_input.run()