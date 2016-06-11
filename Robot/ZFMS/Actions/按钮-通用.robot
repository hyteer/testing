*** Settings ***
Library           Selenium2Library

*** Keywords ***
查询
    Click Element    btnSearch

添加
    Click Link    xpath=//div[@class='panel-toolbar']//a[@href="edit.ht"]

添加列
    Click Element    xpath=//div[@class='panel-toolbar']//a/span/parent::a[contains(text(),'添加列')]

添加2
    Click Element    xpath=//div[@class='panel-toolbar']//a/span/parent::a[contains(text(),'添加')]

注释
    Input Text    id=comment    An auto test

表名
    Clear Element Text    name
    sleep    1s
    Input Text    name    ${tbName}

主表
    Click Element    xpath=//label[contains(text(),'主表')]/input

从表
    #Select Radio Button    isMain    0
    Click Element    xpath=//label[contains(text(),'从表')]/input

字段描述
    Input Text    fieldDesc    ${fieldDesc}

字段名称
    Input Text    fieldName    ${fieldName}

保存
    Click Element    dataFormSave

关闭
    Click Element    xpath=//div[@class='panel-toolbar']//a/span/parent::a[contains(text(),'关闭')]

选择表单框架
    Select Frame    83

选择弹出框架
    #Select Frame    xpath=//table[@class='l-dialog-table']//iframe
    Select Frame    xpath=//div[@ligeruiid='Dialog1001']//iframe

确认是

确认否
    Click Element    xpath=//div[@class='l-dialog-btn-inner' and contains(text(),'否')]

添加列2
    Click Element    xpath=//div[@class='panel-toolbar']//a[@onclick='clickAddRow()']
