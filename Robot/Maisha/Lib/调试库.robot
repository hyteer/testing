*** Settings ***
Library           AppiumLibrary

*** Keywords ***
获取元素
    [Arguments]    ${locator}
    ${el}    Get Elements    ${locator}
    Log    ${el}
