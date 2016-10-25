from keywords import ReqLib

from version import VERSION

_version_ = VERSION

class YTRequests(ReqLib):

    """ YTRequests is a HTTP client keyword library that uses
    the requests module from Kenneth Reitz
        -- YT

        Examples:
        | YT Version
        | New Session | github  | http://github.com/api/v2/json |
        | ${resp} | Get  google  |  / |
        | Should Be Equal As Strings |  ${resp.status_code} | 200 |
        | ${resp} | Get  github  | /user/search/bulkan |
        | Should Be Equal As Strings  |  ${resp.status_code} | 200 |
        | ${jsondata}  | To Json |  ${resp.content} |
        | Dictionary Should Contain Value | ${jsondata['users'][0]} | Bulkan Savun Evcimen |
    """

    ROBOT_LIBRARY_SCOPE ='GLOBAL'