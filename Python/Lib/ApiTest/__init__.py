from maisha import *
from version import VERSION
from wsh import WshApi

_version_ = VERSION

class ApiTest(MaishaUser,MaishaCommon,CommonUtils):
       ROBOT_LIBRARY_SCOPE = 'GLOBAL'