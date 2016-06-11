*** Settings ***
Library           Selenium2Library
Resource          ../Args/Global.robot
Resource          ../Args/Users.robot
Resource          ../Args/Locators.robot

*** Keywords ***
打开系统
    Open Browser    ${HOME}
    set selenium speed    ${SPEED}

输入登录信息
    Input Text    ${e_login_id}    admin
    Input Password    ${e_login_pass}    1

点击登录按钮
    Click Element    ${e_login_submit}

打开登录页
    Go To    ${HOME}
