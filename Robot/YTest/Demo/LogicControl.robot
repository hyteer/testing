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
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed

sample
    ${sign}    Set Variable    None
    ${sign2}    Set Variable    no
    Log    Sign:${sign}
    Run Keyword If    ${sign}!=None    Log    sign is not none.
    ...    ELSE    Log    sign is none
