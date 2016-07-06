*** Settings ***
Library           AppiumLibraryYT

*** Keywords ***
启动App
    Open Application    http://10.20.100.82:4731/wd/hub    platformName=iOS    platformVersion=9.3    udid=2bc289b87f8fdadd6add2ad0b55a26c6081d2d77

关闭App
    Close All Applications

向上滑动
    Swipe    190    500    190    180

向下滑动

向左滑动

向右滑动
