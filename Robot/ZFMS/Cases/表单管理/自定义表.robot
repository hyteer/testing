*** Settings ***
Documentation     测试自定义表相关操作。
Library           Selenium2Library
Resource          ../../Actions/Menu.robot
Resource          ../../Actions/Login.robot
Resource          ../../Actions/菜单-流程管理.robot
Resource          ../../Actions/按钮-通用.robot
Resource          Res.robot

*** Test Cases ***
打开自定义表
    打开系统
    Maximize Browser Window
    输入登录信息
    点击登录按钮
    sleep    1s
    点击流程管理
    点击自定义表
    sleep    1s
    Select Frame    83
    添加2
    sleep    2s

添加自定义表
    打开自定义表
    sleep    2s
    注释
    sleep    1s
    表名
    主表
    添加列2
    Unselect Frame
    选择弹出框架
    字段描述
    字段名称
    sleep    1s
    保存
    关闭
    Unselect Frame
    选择表单框架
    保存

*** Keywords ***
打开自定义表
    打开系统
    Maximize Browser Window
    输入登录信息
    点击登录按钮
    sleep    1s
    点击流程管理
    点击自定义表
    sleep    1s
    选择表单框架
    添加2
    #Unselect Frame
