*** Settings ***
Suite Setup       启动App
Resource          ../Lib/常用操作.robot
Library           AppiumLibraryYT

*** Test Cases ***
查看产品分类
    Wait Until Page Contains    首页
    Sleep    1
    Click Element    xpath=//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[3]
    Sleep    2
    Click Element    xpath=//UIAApplication/UIAWindow[1]/UIANavigationBar/UIAButton[@name='返回']
    #Click Element    ios=.buttons().withName('返回')
    Sleep    3
    Close Application

首页页面滑动
    Wait Until Page Contains    首页
    Sleep    2
    向上滑动
    Sleep    3
    Close All Applications
