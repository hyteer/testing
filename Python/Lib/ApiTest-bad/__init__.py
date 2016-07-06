# encoding: utf-8
from maisha import *
from utils import Utils
from version import VERSION

_version_ = VERSION


class ApiTest(
    MaishaCommon,
    MaishaUser,
    Utils
):
    """
    *ApiTest-bad Library*
        writen by YT
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
