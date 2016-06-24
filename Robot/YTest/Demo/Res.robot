*** Keywords ***
testif
    [Arguments]    ${n}=1    ${device}=medium    ${interval}=500
    @{list}    Run Keyword If    '${device}'=='small'    Set Variable    240    580    240
    ...    240
    ...    ELSE IF    '${device}'=='medium'    Set Variable    350    950    350
    ...    400
    ...    ELSE    '${device}'=='big'    Set Variable    500    1400    500
    ...    400
    :FOR    ${i}    IN RANGE    ${n}
    \    Log    Test Loop
    \    Sleep    0.5
    \    Log    --The End--
    ${str}    Set Variable    起始坐标：'@{list}[0]','@{list}[1]' 结束坐标：'@{list}[2]','@{list}[3]'
    Log    ${str}
