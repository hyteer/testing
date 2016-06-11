*** Settings ***
Documentation     Tests for named cases.
Suite Teardown    Close Browser
Library           Selenium2Library
Resource          ../Args/Global.robot
Resource          ../Args/Users.robot
Resource          ../Args/Locators.robot
Resource          ../Actions/Login.robot
Resource          ../Actions/Menu.robot

*** Test Cases ***
表单
    打开系统
    Maximize Browser Window
    输入登录信息
    点击登录按钮
    点击流程管理
    Click Element    ${e process table}
    sleep    2s

Case2
    打开系统
    Maximize Browser Window
    输入登录信息
    点击登录按钮
    sleep    2s
    点击组织管理
    Element Should Contain    id=leftTree_1_a    用户管理

*** Keywords ***
