*** Settings ***
Library           RequestsLibrary

*** Keywords ***
登录
    Create Session    wsh    http://betanewwsh.vikduo.com
    ${url}    Set Variable    http://betanewwsh.vikduo.com
    &{data}=    Create Dictionary    username=20151228    password=123456    captcha=1111
    &{headers}=    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    ${resp}    Post Request    wsh    /login/login-ajax    data=${data}    headers=${headers}
