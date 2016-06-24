*** Settings ***
Suite Setup       启动App
Suite Teardown    关闭App
Library           AppiumLibrary
Resource          ../../../Lib/常用操作.robot
Resource          ../../../Lib/功能菜单.robot
Resource          ../../../Lib/系统按键.robot
Resource          ../../../Lib/配置参数.robot

*** Test Cases ***
首页滑动
    [Tags]    Smoke
    Wait Until Page Contains Element    id=ivDiscover    ${TIMEOUT}
    Sleep    2s
    ${device}    Set Variable    medium
    向上滑动    3    400
    向下滑动    3    400

查看商品
    Wait Until Page Contains Element    id=ivDiscover    ${TIMEOUT}
    #Click Element    xpath=//android.view.View//android.widget.LinearLayout[@clickable='true']
    Sleep    2s
    #每日上新
    Click Element    xpath=//android.view.View[@id='com.maishalei.seller.debug:id/flexboxGroupBuyCommodities']/android.widget.LinearLayout[0]
    Sleep    2s
    #Wait Until Page Contains Element    xpath=//android.widget.TextView[contains(@id,'com.maishalei.seller:id/centerView')][contains(@text,'拼啥嘞')]    ${TIMEOUT}
    Wait Until Page Contains    拼啥嘞    ${TIMEOUT}
    向上滑动
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@NAF='true']    ${TIMEOUT}
    返回-Text
    #返回键
