*** Settings ***
Library           AppiumLibrary

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
    ${b}    Get Current Context
    Switch To Context    ${a[1]}

返回
    Click Element    xpath=//android.widget.ImageView[@NAF='true']

取消
    Click Element    xpath=//android.widget.TextView[@id='com.maishalei.seller.debug:id/tvCancel']

关闭
    Click Element    xpath=//android.widget.TextView[@text='关闭']

返回-Text
    Click Element    xpath=//android.widget.TextView[@NAF='true']

向上滑动
    [Arguments]    ${n}=1    # 设置滑动次数
    :FOR    ${i}    IN RANGE    ${n}
    \    Swipe    500    1400    500    400    500
    \    Sleep    0.5
    #:FOR ${i} IN RANGE \ 5?
    #:FOR    ${n}    IN    @{var}

向下滑动
    :FOR    ${i}    IN RANGE    3
    \    Swipe    500    400    500    1400    500
    \    Sleep    0.5
