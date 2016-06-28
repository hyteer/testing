*** Settings ***
Library           AppiumLibrary
Library           WshLibrary
Resource          配置参数.robot
Resource          系统按键.robot

*** Keywords ***
点击搜索
    Wait Until Page Contains    首页
    #${el}    Get Elements    xpath=//android.widget.RelativeLayout
    #Log    Elements: ${el}
    Click Element    xpath=//android.widget.ImageView[@index='2']
    #Click Element

回车
    Press Keycode    66

启动App
    #Open Application    http://localhost:4723/wd/hub    alias=maisha    platformName=Android    platformVersion=4.4.2    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug
    # appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    # appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    启动参数
    Open Application    ${host}    &{caps}

启动App2
    ${mode}    Set Variable    debug    # debug/product
    ${host}    Run Keyword If    '${device}'=='small'    Set Variable    http://localhost:4722/wd/hub
    ...    ELSE IF    '${device}'=='medium'    Set Variable    http://localhost:4723/wd/hub
    ...    ELSE IF    '${device}'=='big'    Set Variable    http://localhost:4724/wd/hub
    ...    ELSE    Log    请输入正确的设备规格。
    &{caps}    Run Keyword If    '${device}'=='small'    Create Dictionary    alias=maisha    platformName=Android    platformVersion=5.1.1
    ...    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    ...    ELSE IF    '${device}'=='medium'    Create Dictionary    alias=maisha    platformName=Android    platformVersion=5.1.1
    ...    deviceName='HUAWEI MT2-L01'    appPackage=com.maishalei.seller.debug    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    ...    ELSE IF    '${device}'=='big'    Create Dictionary    alias=maisha    platformName=Android    platformVersion=4.4.2
    ...    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    ...    ELSE    Log    请输入正确的设备规格。
    Set Global Variable    &{caps}
    Set Global Variable    ${host}
    Open Application    ${host}    &{caps}

启动App3
    Open Application    http://localhost:4724/wd/hub    alias=maisha    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug
    ...    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True

点击分类
    Wait Until Page Contains    首页
    Click Element    xpath=//android.widget.ImageView[@index='3']

点击扫码
    Wait Until Page Contains    首页
    Click Element    xpath=//android.widget.ImageView[@index='1']

点击我的
    Click Element    id=ivMine

点击QQ登录
    Click Element    id=ivQQLogin

切换Web视图
    ${a}    Get Contexts
    Log    Contexts: ${a}
    ${b}    Get Current Context
    Log    Current Context is: ${b}
    Log    Context a1 is: ${a[1]}
    Switch To Context    ${a[1]}
    Get Current Context

返回
    Click Element    xpath=//android.widget.ImageView[@NAF='true']

取消
    Click Element    xpath=//android.widget.TextView[@text='取消']
    #Click Element    xpath=//android.widget.TextView[@id='com.maishalei.seller.debug:id/tvCancel']

关闭
    Click Element    xpath=//android.widget.TextView[@text='关闭']

返回-Text
    Click Element    xpath=//android.widget.TextView[@NAF='true']

向上滑动
    [Arguments]    ${n}=1    ${interval}=500    # 设置滑动次数间隔
    #@{list}=    Get Slide Args V    ${device }
    启动参数
    @{list}    Run Keyword If    '${device}'=='small'    Set Variable    240    580    240
    ...    240
    ...    ELSE IF    '${device}'=='medium'    Set Variable    350    950    350
    ...    400
    ...    ELSE IF    '${device}'=='big'    Set Variable    500    1400    500
    ...    400
    ...    ELSE    Log    无效的参数${device}
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}    ${interval}
    \    Sleep    0.5

向下滑动
    [Arguments]    ${n}=1    ${interval}=500    # 滑动次数
    启动参数
    @{list}    Run Keyword If    '${device}'=='small'    Set Variable    240    240    240
    ...    580
    ...    ELSE IF    '${device}'=='medium'    Set Variable    350    400    350
    ...    950
    ...    ELSE IF    '${device}'=='big'    Set Variable    500    400    500
    ...    1400
    ...    ELSE    Log    无效的参数${device}
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}    ${interval}
    \    Sleep    0.5

返回顶部
    Click Element    id=ivBackToTop

关闭App
    Close Application

向左滑动
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}=    Get Slide Args H    ${device }
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5

向右滑动
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}=    Get Slide Args H    ${device }
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5

TempTest
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}    Run Keyword If    ${device }==smal    Set Variable    240    580    240
    ...    240
    \    ELSE IF    ${device}==medium    Set Variable    350    950    350
    \    ...    400
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5

等待
    [Arguments]    ${time}=2s
    Sleep    ${time}

检验等待
    [Arguments]    ${object}=首页    ${time}=10
    Run Keyword If    '${object}'=='首页'    Wait Until Page Contains Element    id=ivDiscover    ${time}
    ...    ELSE IF    '${object}'=='分享'    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='分享']    ${time}
    ...    ELSE IF    '${object}'=='WebView'    Wait Until Page Contains Element    id=webview    ${time}
    ...    ELSE IF    '${object}'=='标题'    Wait Until Page Contains Element    id=centerView
