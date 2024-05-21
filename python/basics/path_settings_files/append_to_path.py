import os
import sys


def try_import_module():
    try:
        import test_module
    except ModuleNotFoundError:
        print("Module import went wrong!")

try_import_module()
sys.path.append("some_hidden_module")
try_import_module()
