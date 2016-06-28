*** Settings ***
Library           AppiumLibrary

*** Test Cases ***
QQ登录

微博登录

微信登录

手机密码登录
    Input Text    id=etPhoneByPwd    ${phone num}
    Input Password    id=etPwdByPwd    ${phone pwd}

手机验证码登录
