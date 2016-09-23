*** Settings ***
Resource          Res.robot

*** Test Cases ***
if
    testif    3    medium    300

for
    ${n}    Set Variable    4
    : FOR    ${i}    IN RANGE    ${n}
    \    Log    ${i}

if-num
    ${x}    Set Variable    1
    Run Keyword If    ${x}>=2    Log    Success
    ...    ELSE    Log    Failed
    Run Keyword If    ${x}!=1    Log    yes
    ...    ELSE    Log    no

sample
    ${sign}    Set Variable    None
    ${sign2}    Set Variable    no
    Log    Sign:${sign}
    Run Keyword If    ${sign}!=None    Log    sign is not none.
    ...    ELSE    Log    sign is none

if-multi
    ${x}    Set Variable    11
    Run Keyword If    ${x}>=2    Log    yes
    ...    ELSE    Log    no
    Run Keyword If    ${x}!=1    Log    yes
    ...    ELSE    Log    no
    Run Keyword If    ${x}>2 and ${x}<10    Log    Multi:yes
    ...    ELSE    Log    Multi:no

run_keyword_if
    ${积分抵扣开关}    Evaluate    2
    ${积分抵扣金额}    Run Keyword If    ${积分抵扣开关}==1    Evaluate    11

*** Keywords ***
testif
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}    Run Keyword If    '${device}'=='small'    Set Variable    240    580    240
    ...    240
    ...    ELSE IF    '${device}'=='medium'    Set Variable    350    950    350
    ...    400
    ...    ELSE    '${device}'=='big'    Set Variable    500    1400    500
    ...    400
    : FOR    ${i}    IN RANGE    ${n}
    \    Log    Test Loop
    \    Sleep    0.5
    \    Log    --The End--
    ${str}    Set Variable    起始坐标：'@{list}[0]','@{list}[1]' 结束坐标：'@{list}[2]','@{list}[3]'
    Log    ${str}
