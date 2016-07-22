*** Settings ***
Library           Selenium2Library
Resource          配置参数.robot
Resource          功能菜单.robot
Library           String
Library           Screenshot

*** Keywords ***
登录
    #Set Selenium Implicit Wait    10
    #Set Selenium Timeout    10
    Open Browser    ${URL}    chrome    #打开浏览器
    界面最大化
    Input Text    id=staff_id    ${USERNAME}    #输入用户名
    Input Text    id=password    ${PASSWORD}    #输入密码
    Input Text    id=captcha    111111    #输入验证码
    Click Button    id=login    #点击登陆

界面最大化
    Maximize Browser Window

关闭浏览器
    Close All Browsers

获取分组名
    登录
    点击链接菜单    微会员
    点击链接菜单    分组管理    #获取组名    #@{number}    create list    2    3
    ...    # 4    5    6    # 7    8    9
    ...    # 10
    : FOR    ${i}    IN    @{number}
    \    ${title}=    Get Webelements    xpath=//*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div/div/table/tbody
    #${title}    Get Text    xpath=//*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div/div/table/tbody/tr{j}/td[2]
    sleep    0.1
    LOG    ${title}

等待时间
    [Arguments]    ${time}=1s
    sleep    ${time}

对比校验
    [Arguments]    ${xxx}    ${expect}
    ${text}    Get Text    ${xxx}    #${xxx}是xpath路径
    #Should Contain    ${text}    ${expect}
    Run Keyword If    '${text}'=='${expect}'    log    校验通过
    ...    ELSE    log    校验失败

浏览器返回/后退
    Go Back

点击元素
    [Arguments]    ${element_xpath}    ${time}=5s    ${message}=Element Error
    [Tags]
    #Wait Until Page Contains Element    ${element_xpath}    ${time}    ${message}
    Click Element    ${element_xpath}

智能等待
    [Arguments]    ${seconds}=10s
    Set Browser Implicit Wait    ${seconds}

添加商品
    click element    xpath=//*[@id="product"]/div[1]/table/tbody[1]/tr[2]/td/table/tbody/tr[3]/td[3]
    Sleep    0.5
    Wait Until Page Contains Element    xpath=//*[@id="main-container"]/div[3]/div/div/div[3]/a[2]    5
    click element    xpath=//*[@id="main-container"]/div[3]/div/div/div[3]/a[2]    #点击确定按钮
    等待时间    1
    Wait Until Page Contains Element    id=post    5
    Click Element    id=post
    等待时间    0.5
    confirm action
    等待时间    1    #删除数据，还原初始状态    #${number}    Get Text    //*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div[4]/ul[2]/li[3]/span/span    #Click Element
    ...    # xpath=//*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[7]/div/a[2]/i    #点击删除按钮    #等待时间    1    #Click Element    xpath=//tbody/tr[3]/td/div[2]/button[1]
    ...    #确认删除    #等待时间    1    #confirm action    #等待时间    2
    ...    #${i}    Set Variable    1    #${sum}    Set Variable    0
    ...    #${number1}    Get Text    //*[@id="main-container"]/div[1]/div[2]/div[2]/div/div/div[4]/ul[2]/li[3]/span/span    #${sum}    Evaluate    ${number}-${i}
    ...    #Run Keyword If    '${sum}'=='${number1}'    log    删除后校验通过    # ELSE    log
    ...    # 删除后校验失败

返回活动列表
    点击元素    xpath=//*[@id="main-container"]/div[3]/div/div/div[3]/a[1]
    等待时间    1
    点击元素    xpath=//*[@id="modal-footer"]/a[1]
    log    由于有全场商品满减活动，无法创建活动，返回活动列表

随机字符
    [Arguments]    ${pre}=None    ${len}=10
    ${prelen}    Get Length    ${pre}
    ${randlen}    Evaluate    ${len}-${prelen}
    ${rand}    Generate Random String    ${randlen}
    ${randstr}    Set Variable    ${pre}-${rand}
    [Return]    ${randstr}

随机数字
    [Arguments]    ${len}=4
    ${num}    Generate Random String    ${len}    123456789
    [Return]    ${num}

选择时间
    #选择开始时间
    Click Element    id=start_time
    Sleep    1
    Select Frame    xpath=//iframe[@hidefocus='true']
    Click Element    xpath=/html/body/div/div[3]/table/tbody/tr[6]/td[5]
    Sleep    0.8
    Click Element    id=dpOkInput
    Sleep    1
    Unselect Frame
    #选择结束时间
    Click Element    id=end_time
    Sleep    1
    Select Frame    xpath=//iframe[@hidefocus='true']
    Click Element    xpath=//*[@id="dpTitle"]/div[6]/a
    Sleep    0.6
    Click Element    xpath=/html/body/div/div[3]/table/tbody/tr[4]/td[5]
    Sleep    0.6
    Click Element    id=dpOkInput
    Unselect Frame

失败重启
    Run Keyword If Test Failed    Take Screenshot
    Run Keyword If Test Failed    登录
    Sleep    1

查看二维码
    [Arguments]    ${xpath}
    ###查看二维码
    Click Element    xpath=${xpath}
    Sleep    1
    Select Window    二维码
    Sleep    1
    Click Element    xpath=//*[@id="main-container"]/div/div[2]/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/a/i
    Sleep    2
    Wait Until Page Contains Element    xpath=//*[@id="query"]/div/div/div[2]/div/div/img    15
    Wait Until Element Is Visible    xpath=//*[@id="query"]/div/div/div[2]/div/div/img
    Sleep    1
    Click Element    xpath=//*[@id="query"]/div/div/div[1]/a
    Sleep    2
    Close Window
    Sleep    1

查看中奖名单
    [Arguments]    ${xpath}
    Click Element    xpath=${xpath}
    Wait Until Page Contains    中奖记录    20
    Title Should Be    中奖记录
    Sleep    1
    #导出中奖记录
    Click Link    导出中奖记录
    Sleep    2

查看日志
    [Arguments]    ${xpath}
    Click Element    xpath=${xpath}
    Wait Until Page Contains    操作日志
    Title Should Be    操作日志
    Sleep    1

随机金额
    ${long}    Generate Random String    1    34567
    ${pre}    Generate Random String    1    12345
    ${zero}    Generate Random String    ${long}    0
    ${金额}    Set Variable    ${pre}${zero}
    [Return]    ${金额}

弹出信息校验
    [Arguments]    ${msg}
    ${alert}    Get Alert Message
    Should Contain    ${alert}    ${msg}
