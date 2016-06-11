*** Settings ***
Library           Selenium2Library
Resource          ../Args/Locators.robot

*** Keywords ***
点击流程管理
    Click Element    80
    Element Should Contain    leftTree_1    表单管理

点击组织管理
    Click Element    45
    Element Should Contain    leftTree_1    用户管理

点击系统管理
    Click Element    122
    Element Should Contain    leftTree_1    桌面管理
