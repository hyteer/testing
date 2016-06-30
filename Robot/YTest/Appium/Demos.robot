*** Settings ***
Library           SongzAppiumLibrary
Library           String
Library           Collections
Library           AppiumYT

*** Test Cases ***
switchActivity
    Open Application    http://localhost:4723/wd/hub    alias=cal    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.android.calculator2
    ...    appActivity=.Calculator    unicodeKeyboard=True    resetKeyboard=True
    Sleep    2
    Click Element    id=digit7
    Click Element    id=mul
    Click Element    id=digit9
    Click Element    id=equal
    Sleep    1
    #------------------------------------------
    Start Activity    com.android.contacts    com.android.mms.ui.ConversationList
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
    #Wait Until Page Contains Element    id=ivDiscover    10
    #Click Element    id=ivMine
    #-----------------------------------------
    Start Activity    com.android.calculator2    .Calculator
    Click Element    id=clear
    Sleep    3
    Close All Applications

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
    ${app1}=    Open Application    http://localhost:4723/wd/hub    alias=maisha    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.maishalei.seller    appActivity=.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    Wait Until Page Contains Element    id=ivDiscover    10
    Click Element    id=ivMine
    Sleep    2
    ${app2}=    Open Application    http://localhost:4823/wd/hub    alias=sms    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.contacts    appActivity=com.android.mms.ui.ConversationList    unicodeKeyboard=True    resetKeyboard=True
    Sleep    4
    Switch Application    maisha
    Sleep    8

calculator
    ${app sms}=    Open Application    http://localhost:4823/wd/hub    alias=sms    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.contacts    appActivity=com.android.mms.ui.ConversationList    unicodeKeyboard=True    resetKeyboard=True
    Wait Until Page Contains    通知信息    10
    Sleep    2
    Click Element    xpath=//huawei.android.widget.TimeAxisWidget//android.widget.TextView[@text='通知信息']
    Sleep    1
    Click Element    xpath=//android.widget.TextView[@text='1069036572380227']
    Sleep    2
    ${app cal}    Open Application    http://localhost:4723/wd/hub    alias=calculator    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.calculator2    appActivity=.Calculator
    Sleep    4
    Click Element    id=com.android.calculator2:id/digit8
    Click Element    id=com.android.calculator2:id/mul
    Click Element    id=digit9
    Click Element    id=equal
    Sleep    1s
    #Click Element    id=clear
    Sleep    2
    Switch Application    ${app sms}
    Sleep    5
    Close All Applications

multiApp
    ${app cal}    Open Application    http://localhost:4722/wd/hub    alias=calculator    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.calculator2    appActivity=.Calculator
    Sleep    4
    Click Element    id=com.android.calculator2:id/digit8
    Click Element    id=com.android.calculator2:id/mul
    Click Element    id=digit9
    Click Element    id=equal
    Sleep    2
    #Click Element    id=clear
    ${app sms}=    Open Application    http://localhost:4822/wd/hub    alias=sms    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.contacts    appActivity=com.android.mms.ui.ConversationList    unicodeKeyboard=True    resetKeyboard=True
    Sleep    4
    Switch Application    calculator
    Sleep    5
    Close All Applications

multiApp2
    ${app cal}    Open Application    http://localhost:4722/wd/hub    alias=calculator    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.calculator2    appActivity=.Calculator
    Sleep    4
    Click Element    id=digit_8
    Click Element    id=op_mul
    Click Element    id=digit_9
    Click Element    id=eq
    Sleep    2
    #Click Element    id=clear
    ${app sms}=    Open Application    http://localhost:4822/wd/hub    alias=sms    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'
    ...    appPackage=com.android.mms    appActivity=com.android.mms.ui.ConversationList    unicodeKeyboard=True    resetKeyboard=True
    Sleep    4
    Switch Application    calculator
    Sleep    5
    Close All Applications
    \    w

SwitchActivity2
    Open Application    http://localhost:4723/wd/hub    alias=memo    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.example.android.notepad
    ...    appActivity=.NotePadActivity    unicodeKeyboard=True    resetKeyboard=True
    #Wait Until Page Contains Element    id=ivDiscover    10
    #Click Element    id=ivMine
    Start Activity    com.example.android.notepad    .NotePadActivity
    Sleep    2
    Click Element    id=menu_create_note
    Sleep    1
    Start Activity    com.android.contacts    com.android.mms.ui.ConversationList
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
    Log    Code is: ${code}[0]
    ${code0}    Evaluate    ${code}[0]
    Log    Code[0] is: ${code0}
    ${codeint}    Evaluate    int(${code}[0])
    Log    Code Int is: ${codeint}
    #${codenum}    Convert To Integer    ${code}[0]
    ${code2}    Get Substring    ${message}    7    11
    Log    Code2 is: ${code2}
    ${time}    Get Time
    ${memo}=    Set Variable    ${time} 验证码：${code0}
    Start Activity    com.example.android.notepad    .NoteEditor
    Sleep    2
    Input Text    xpath=//android.widget.EditText[@NAF='true']    ${memo}
    Sleep    3
    Capture Page Screenshot
    Close All Applications

Math
    Open Application    http://localhost:4723/wd/hub    alias=memo    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.example.android.notepad
    ...    appActivity=.NotePadActivity    unicodeKeyboard=True    resetKeyboard=True
    #Wait Until Page Contains Element    id=ivDiscover    10
    #Click Element    id=ivMine
    Start Activity    com.example.android.notepad    .NotePadActivity
    Sleep    2
    Click Element    id=menu_create_note
    Sleep    1
    Start Activity    com.android.contacts    com.android.mms.ui.ConversationList
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
    Log    Code is: ${code}[0]
    ${code0}    Evaluate    ${code}[0]
    Log    Code[0] is: ${code0}
    ${codeint}    Evaluate    int(${code}[0])
    Log    Code Int is: ${codeint}
    #${codenum}    Convert To Integer    ${code}[0]
    ${code2}    Get Substring    ${message}    7    11
    Log    Code2 is: ${code2}
    ${time}    Get Time
    ${memo}=    Set Variable    ${time} 验证码：${code}
    Start Activity    com.example.android.notepad    .NoteEditor
    Sleep    2
    Input Text    xpath=//android.widget.EditText[@NAF='true']    ${memo}
    Sleep    3
    Capture Page Screenshot
    Close All Applications

SwitchActivityMaisha
    Open Application    http://localhost:4723/wd/hub    alias=memo    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller
    ...    appActivity=.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True
    Wait Until Page Contains Element    id=ivDiscover    10
    #Start Activity    com.maishalei.seller    .ui.activity.LauncherActivity
    Sleep    2
    Click Element    id=ivMine
    Sleep    1
    Click Element    id=tvLoginHeaderBySMSCode
    Sleep    2
    Input Text    id=etPhoneBySMSCode    13924628477
    Click Element    id=btnResendBySMSCode
    Sleep    15
    #-------------------------------------
    Start Activity    com.android.contacts    com.android.mms.ui.ConversationList
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
    Log    Code is: ${code}[0]
    ${code0}    Evaluate    ${code}[0]
    Log    Code[0] is: ${code0}
    ${codeint}    Evaluate    int(${code}[0])
    Log    Code Int is: ${codeint}
    #${codenum}    Convert To Integer    ${code}[0]
    ${code2}    Get Substring    ${message}    7    11
    Log    Code2 is: ${code2}
    ${time}    Get Time
    ${memo}=    Set Variable    ${time} 验证码：${code0}    #-----------------------------------    #Open Application    http://localhost:4723/wd/hub    alias=memo
    ...    # platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller    # appActivity=.ui.activity.LauncherActivity    unicodeKeyboard=True
    ...    # resetKeyboard=True
    #Wait Until Page Contains Element    id=ivDiscover    10
    Start Activity    com.maishalei.seller    .ui.activity.LauncherActivity
    Wait Until Page Contains Element    id=ivDiscover    10
    Sleep    2
    Click Element    id=ivMine
    Sleep    1
    Click Element    id=tvLoginHeaderBySMSCode
    Sleep    1
    Capture Page Screenshot
    Input Text    id=etPhoneBySMSCode    13924628477
    Input Text    id=etCodeBySMSCode    ${code0}
    Click Element    id=btnLoginBySMSCode
    #Input Text    xpath=//android.widget.EditText[@NAF='true']    ${memo}
    Sleep    5
    Capture Page Screenshot
    Close All Applications

GetStatus
    启动App M2
    Wait Until Page Contains Element    id=ivDiscover    10
    Sleep    2
    Click Element    id=ivMine
    Sleep    1
    ${status}    Run Keyword And Return Status    Page Should Not Contain Element    xpath=//android.widget.TextView[@text='我的订单']
    Log    Status is: ${status}
    Close All Applications

GetStatus2
    启动App M2
    Wait Until Page Contains Element    id=ivDiscover    10
    Sleep    2
    Click Element    id=ivMine
    Sleep    1
    ${status}    状态判断    xpath=//android.widget.TextView[@text='我的订单']
    Log    Status back: ${status}
    Close All Applications

ArgsTransmit
    Log    ----------Scalar-----------
    ${backscalar}=    参数传递-scalar    11
    Log    Back Scalar: ${backscalar}
    Log    -----------dict-------------
    &{dict}=    Create Dictionary    x=11    y=22    z=33
    ${backdict}    参数传递-dict    &{dict}
    Log    Back Dict: ${backdict}

Convertion
    &{dict}    Convert To Dictionary    {xpath=aa,y=11}

AppiumYT
    start memo
    Click Element    id=menu_create_note
    Sleep    1
    Input Text    xpath=//android.widget.EditText[@NAF='true']    Test...
    Sleep    3

bootArgs
    Log    ${arg1}
    Log    ${arg2}

runArgs
    Log    Device:${device}
    Log    mode:${mode}

*** Keywords ***
获取验证码
    Sleep    1
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

启动App M2
    Open Application    http://localhost:4723/wd/hub    alias=memo    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.maishalei.seller
    ...    appActivity=.ui.activity.LauncherActivity    unicodeKeyboard=True    resetKeyboard=True

状态判断
    [Arguments]    &{xpath}    # 不需要开头"xpath=",直接传入后面的xpath表达式
    ${status}    Run Keyword And Return Status    Page Should Not Contain Element    &{xpath}
    Log    Status is: ${status}
    [Return]    ${status}

参数传递-scalar
    [Arguments]    ${x}=1
    Log    ${x}
    ${y}    Set Variable    back scalar...
    [Return]    ${y}

参数传递-dict
    [Arguments]    &{dict}
    Log    Original Dict: '&{dict}'
    &{backdict}    Create Dictionary    a=1    b=2    c=3
    [Return]    &{backdict}

参数传递-list
    [Arguments]    ${x}=1    &{dict}
    Log    ${x}
    Log    @{list}
    Log    &{dict}
    ${y}    Set Variable    back scalar...
    @{backlist}    Set Variable    aa    bb    cc
    &{backdict}    Set Variable    a=1    b=2    c=3
    [Return]    ${y}

start memo
    Open Application    http://localhost:4723/wd/hub    alias=memo    platformName=Android    platformVersion=5.1.1    deviceName='emulator-5554'    appPackage=com.example.android.notepad
    ...    appActivity=.NotePadActivity    unicodeKeyboard=True    resetKeyboard=True
    Sleep    2
