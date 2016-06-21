*** Settings ***
Library           AppiumLibrary

*** Keywords ***
启动微信
    Open Application    http://localhost:4723/wd/hub    alias=wechat    platformName=Android    platformVersion=4.4.2    deviceName='emulator-5554'    appPackage=com.tencent.mm
    ...    appActivity=com.tencent.mm.ui.LauncherUI
    Wait Until Page Contains    微信    20s    等待超时

进入微商户助手
    Wait Until Page Contains    微商户助手
    Click Element    xpath=//android.view.View[contains(@text,'微商户助手')]
    Log    Success...
    ${a}    Get Contexts
    Log    ${a}

打开首页
    Click Element    xpath=//android.widget.TextView[contains(@text,'首页')]

打开会员服务菜单
    Wait Until Page Contains    会员服务
    Click Element    xpath=//android.widget.TextView[contains(@text,'会员服务')]
    Sleep    1s

打开商品列表
    Click Element    xpath=//android.widget.TextView[contains(@text,'商品列表')]
