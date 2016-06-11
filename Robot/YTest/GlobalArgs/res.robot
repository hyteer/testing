*** Settings ***
Library           Selenium2Library

*** Variables ***
${HOME}           http://172.25.2.20:3000/    # redmine home
${LOGIN}          http://172.25.2.20:3000/login
${USERNAME}       tony
${PASSWORD}       111111
@{LOGIN_INFO}     admin    admin
${WAIT}           2s
${LOCALUSER}      huyt
${LOCALPASS}      111
${INFO}           This is a test.

*** Keywords ***
Open Login Page
    Open Browser    ${LOGIN}
    Page Should Contain Element    login-form

Local Login
    Input Text    username    ${LOCALUSER}
    Input Password    password    ${LOCALPASS}
    Click Button    login

Input ID
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Pass
    [Arguments]    ${password}
    Input Text    password    ${password}
