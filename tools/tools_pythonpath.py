# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the hdl_modules project, a collection of reusable, high-quality,
# peer-reviewed VHDL building blocks.
# https://hdl-modules.com
# https://gitlab.com/hdl_modules/hdl_modules
# --------------------------------------------------------------------------------------------------

"""
Import this file to have the default paths of some third party packages added to PYTHONPATH.
"""

# Standard libraries
import sys

# First party libraries
from tools.tools_env import REPO_ROOT

# Do PYTHONPATH insert() instead of append() to prefer any local repo checkout over any pip install

# Paths e.g.
# repo/hdl_modules/hdl_modules
# repo/tsfpga/tsfpga
PATH_TO_TSFPGA = REPO_ROOT.parent.parent.resolve() / "tsfpga" / "tsfpga"
sys.path.insert(0, str(PATH_TO_TSFPGA))

# Paths e.g.
# repo/hdl_modules/hdl_modules
# repo/hdl_registers/hdl_registers
PATH_TO_HDL_REGISTERS = REPO_ROOT.parent.parent.resolve() / "hdl_registers" / "hdl_registers"
sys.path.insert(0, str(PATH_TO_HDL_REGISTERS))

# Paths e.g.
# repo/hdl_modules/hdl_modules
# repo/vunit/vunit
PATH_TO_VUNIT = REPO_ROOT.parent.parent.resolve() / "vunit" / "vunit"
sys.path.insert(0, str(PATH_TO_VUNIT))

# Alternative repo layout where hdl_modules, tsfpga, hdl_registers are git submodules in a
# development repo, and VUnit is outside of this structure.
# Paths e.g.
# repo/path_a/path_b/external/tsfpga/tsfpga
# repo/vunit/vunit
PATH_TO_VUNIT = REPO_ROOT.parent.parent.parent.parent.parent.resolve() / "vunit" / "vunit"
sys.path.insert(0, str(PATH_TO_VUNIT))