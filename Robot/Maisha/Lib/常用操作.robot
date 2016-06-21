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
    Open Application    http://localhost:4723/wd/hub    alias=maisha    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug
    ...    appActivity=com.maishalei.seller.ui.activity.LauncherActivity    unicodeKeyboard =True    resetKeyboard=True

点击分类
    Wait Until Page Contains    首页
    Click Element    xpath=//android.widget.ImageView[@index='2']

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
