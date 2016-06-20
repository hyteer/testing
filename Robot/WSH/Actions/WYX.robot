*** Settings ***
Library           Selenium2Library

*** Keywords ***
微营销
    Click Element    xpath=//div[@id='navbar']//ul[@id='headactive']//a[@text='微营销']
    Sleep    1s
