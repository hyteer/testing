*** Settings ***
Suite Setup       启动App
Library           AppiumLibrary
Resource          ../../../Lib/常用操作.robot
Resource          ../../../Lib/功能菜单.robot
Resource          ../../../Lib/系统按键.robot

*** Test Cases ***
首页滑动
    Wait Until Page Contains Element    id=ivDiscover
    向上滑动
    向下滑动

查看商品
    Wait Until Page Contains Element    id=ivDiscover
    Click Element    xpath=//android.view.View//android.widget.LinearLayout[@clickable='true']
    #Click Element    xpath=//android.widget.LinearLayout[contains(@index,0)][contains(@clickable,true)]
    Sleep    2s
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='拼啥嘞']
    向上滑动
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@NAF='true']
    返回-Text
    #返回键
