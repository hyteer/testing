*** Settings ***
Suite Setup       启动App
Suite Teardown    关闭App
Library           AppiumLibrary
Resource          ../../Lib/常用操作.robot
Resource          ../../Lib/菜单库.robot
Resource          ../../Lib/系统按键.robot
Resource          ../../Lib/配置参数.robot
Resource          ../../Lib/调试库.robot
Resource          ../../Lib/功能库.robot

*** Test Cases ***
活动主题检查
    检验等待
    Sleep    2
    活动主题检测    4
    Sleep    2

大家都在拼检查
    检验等待
    Sleep    2
    #${el}    Get Elements    xpath=//android.view.View[@resource-id='com.maishalei.seller:id/flexboxGroupBuyCommodities']/android.widget.LinearLayout
    #Log    ${el}
    大家都在拼检测
    Sleep    2

搜索功能
    Wait Until Page Contains Element    id=ivDiscover    ${TIMEOUT}
    点击搜索
    Sleep    3s
    #Input Text    id=etSearch    儿童玩具
    Input Text    xpath=//android.widget.EditText[@index='0']    儿童
    回车
    返回
    返回键
    取消

查看产品分类
    [Tags]    Smoke
    启动参数
    Wait Until Page Contains Element    id=ivDiscover    ${TIMEOUT}
    点击分类
    Log    开始分类检查...
    Log To Console    开始分类检查...
    Wait Until Page Contains Element    xpath=//android.widget.TextView[@text='母婴用品']    ${TIMEOUT}
    Run Keyword If    '${mode}'=='debug'    分类菜单检测-测试
    ...    ELSE IF    '${mode}'=='product'    分类菜单检测-生产
    ...    ELSE    Log    请输入正确的运行模式。
    Log    分类检查完成...
    Click Element    xpath=//android.widget.ImageView[@NAF='true']

首页页面滑动
    [Tags]    Smoke
    Wait Until Page Contains Element    id=ivDiscover    ${TIMEOUT}
    Sleep    1
    #${device}    Set Variable    medium
    向上滑动    3    400
    Sleep    1
    向下滑动    1    400
    Sleep    2
    返回顶部
    Sleep    2

封面产品检查
    检验等待
    Click Element    id=view_pager
    检验等待    标题
    Sleep    2
    向上滑动    2    400
    Sleep    1
    返回键
    Sleep    2
