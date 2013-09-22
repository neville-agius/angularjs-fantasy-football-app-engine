"""Config module that will run before serving requests.

Used to customize the environment before running applications. See:

    developers.google.com/appengine/docs/python/tools/appengineconfig

for more information.
"""


import os
import sys

# Enable imports from models submodule.
sys.path.append(os.path.join(os.path.dirname(__file__),
                             'app/models'))