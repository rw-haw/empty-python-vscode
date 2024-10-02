from my_package.dummy_module import dummy_method as module_dummy_method
from my_package import *

def test_dummy_method():
  assert module_dummy_method() is None

def test_all_import_works():
  assert dummy_method() is None