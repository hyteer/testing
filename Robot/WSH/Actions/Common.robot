*** Settings ***
Library           Selenium2Library
Resource          ../Conf/Common.robot

*** Keywords ***
登录系统
    Open Browser    ${BASEURL}    chrome
    Capture Page Screenshot
    Title Should Be    微商户后台管理
    Input Text    staff_id    ${USR}
    Input Password    password    ${PASSWD}
    Input Text    id=captcha    1111
    Click Element    id=login
