*** Settings ***
Documentation     Tests for named cases.
Suite Setup       输入登录信息
Suite Teardown    Close Browser
Test Setup        打开登录页
Library           Selenium2Library
Resource          ../../Args/Global.robot
Resource          ../../Args/Users.robot
Resource          ../../Args/Locators.robot
Resource          ../../Actions/Login.robot

*** Test Cases ***
Case1
    打开系统
    输入登录信息
    点击登录按钮

Case2

*** Keywords ***
