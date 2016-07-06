from testTemp import TestTemp
from version import VERSION
from test import *

_version_ = VERSION

class MyLibrary2(
    TestTemp,
    Test2
):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

