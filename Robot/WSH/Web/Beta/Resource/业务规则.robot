*** Test Cases ***

*** Keywords ***
向下取整
    [Arguments]    ${num}
    [Documentation]    按小数点2位向下取整，例如：79.339取整后为79.33
    ${match}    Evaluate    re.findall(r'\\d*\\d\\.\\d{2}','${num}')    re
    ${price}    Evaluate    float(${match[0]})
    [Return]    ${price}
