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
