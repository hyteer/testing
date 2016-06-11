*** Settings ***
Library           Selenium2Library
Resource          ../Args/Global.robot
Resource          ../Args/Users.robot
Resource          ../Args/Locators.robot
Resource          ../Actions/Login.robot

*** Test Cases ***
login
    Open Browser    ${HOME}

menu
    Click Element    ${e_menu_process}

baidu
    Open Browser    http://www.baidu.com
    Click Element    xpath=//div[@id='u1']//a[@name='tj_login']

temp
    打开系统
    输入登录信息
    点击登录按钮
    sleep    2s
    Go To    http://192.168.31.237:8090/bw_sms/platform/form/bpmFormTable/list.ht
    Click Link    xpath=//div[@class='panel-toolbar']//a[@href="edit.ht"]

ytest1
    Open Browser    http://localhost/test.html
    # Click Element    xpath=//span[text()='难']
    #Click Element    xpath=//a/span/parent::a[contains(text(),'难')]
    Click Element    xpath=//a/span/parent::a[contains(text(),'难大')]
