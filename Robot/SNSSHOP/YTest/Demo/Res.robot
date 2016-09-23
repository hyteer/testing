*** Variables ***
&{RES_URL}        beta=http://betanewwsh.snsshop.net/    ci=http://shanghutest.cxm/    dev=http://335.newwsh.snsshop.net/

*** Keywords ***
环境配置
    [Arguments]    ${env}
    ${USERNAME}    Set Variable    20151228
    ${PASSWORD}    Set Variable    123456
    &{BETA}    Create Dictionary    url=http://betanewwsh.snsshop.net/    username=${USERNAME}    password=${PASSWORD}
    &{CI}    Create Dictionary    url=http://shanghutest.cxm/    username=7638800811    password=518000
    &{DEV}    Create Dictionary    url=http://335.newwsh.snsshop.net/    username=7638800811    password=518000
    &{ENV_DICT}    Create Dictionary    beta=&{BETA}    ci=&{CI}    dev=&{DEV}
    ###
    #
    [Return]    &{ENV_DICT.${env}}
