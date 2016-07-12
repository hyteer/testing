from api import *
from version import VERSION


_version_ = VERSION

class ApiWsh(
       Shop,
       Common,
       CommonUtils,
       Marketing):
       ROBOT_LIBRARY_SCOPE = 'GLOBAL'