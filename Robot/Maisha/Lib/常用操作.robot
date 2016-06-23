*** Settings ***
Library           AppiumLibrary
Library           WshLibrary

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
    Open Application    http://localhost:4723/wd/hub    alias=maisha    platformName=Android    platformVersion=4.4.2    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug
    ...    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True

启动App2
    Open Application    http://localhost:4722/wd/hub    alias=maisha    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug
    ...    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True

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
    Switch To Context    ${a[1]}

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
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500    # 设置滑动次数设备大小等参数
    @{list}=    Get Slide Args V    ${device }
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5

向下滑动
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500    # 滑动次数
    @{list}=    Get Slide Args V    ${device }
    : FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[3]    @{list}[2]    @{list}[1]    ${interval}

返回顶部
    Click Element    id=ivBackToTop

关闭App
    Close Application

向左滑动
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}=    Get Slide Args H    ${device }
    :FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5

向右滑动
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}=    Get Slide Args H    ${device }
    :FOR    ${i}    IN RANGE    ${n}
    \    Swipe    @{list}[0]    @{list}[1]    @{list}[2]    @{list}[3]    ${interval}
    \    Sleep    0.5
