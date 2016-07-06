# encoding: utf-8
from common import CommonUtils
from ytjson import JsonUtils
from apitest import ApiTest

from version import VERSION

_version_ = VERSION

class Ytools(CommonUtils,JsonUtils,ApiTest):

    ROBOT_LIBRARY_SCOPE ='GLOBAL'
