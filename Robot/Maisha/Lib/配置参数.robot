*** Variables ***
${QQUSER}         3504007366
${QQPASSWD}       8520123456
${TIMEOUT}        10
${LONGTIME}       15
@{desired_caps_avd}    http://localhost:4723/wd/hub    alias=maisha    platformName=Android    platformVersion=4.4.2    deviceName='emulator-5554'    appPackage=com.maishalei.seller.debug    appActivity=com.maishalei.seller.ui.activity.LauncherActivity
...               unicodeKeyboard=True    resetKeyboard=True

*** Keywords ***
启动参数
    [Arguments]    ${devicename}
