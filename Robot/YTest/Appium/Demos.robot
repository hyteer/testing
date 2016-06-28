*** Settings ***
Library           AppiumLibrary
Library           String

*** Test Cases ***
switchActivity

SMS
    Open Application    http://localhost:4723/wd/hub    alias=sms    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.android.contacts
    ...    appActivity=com.android.mms.ui.ConversationList    unicodeKeyboard=True    resetKeyboard=True
    Sleep    2
    Click Element    xpath=//huawei.android.widget.TimeAxisWidget//android.widget.TextView[@text='通知信息']
    Sleep    1
    Click Element    xpath=//android.widget.TextView[@text='1069036572380227']
    Sleep    1
    @{el}    Get Elements    xpath=//huawei.android.widget.TimeAxisWidget
    Log    '@{el}'
    ${num}=    Get Count    '@{el}'    element=
    Log    Length is: '@{el}'
    Log    Num is : ${num}
    ${message}    Get Element Attribute    xpath=//huawei.android.widget.TimeAxisWidget[${num}]//android.widget.TextView[@resource-id='com.android.contacts:id/text_view']    text
    Log    Message: ${message}
    ${code}    Get Regexp Matches    ${message}    \\d{4,}
    Log    Code is: ${code}
    ${code2}    Get Substring    ${message}    7    11
    Log    Code2 is: ${code2}

switchApp

*** Keywords ***
获取验证码
    [Arguments]    ${message}
    Log    Message: ${message}
    ${code}    Get Regexp Matches    ${message}    \\d{4,}
    Log    Code is: ${code}
    ${code2}    Get Substring    ${message}    7    11
    Log    Code2 is: ${code2}
