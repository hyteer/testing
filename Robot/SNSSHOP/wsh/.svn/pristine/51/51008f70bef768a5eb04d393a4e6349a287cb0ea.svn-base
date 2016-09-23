*** Settings ***
Library           Selenium2Library

*** Variables ***
${BETA_USERNAME}    20151228
${BETA_PASSWORD}    123456
${BETA_SHOP_ID}    97320
${BETA_URL}       http://betanewwsh.snsshop.net
${BETA_URL_API}    http://betanewwsh.snsshop.net/
${BETA_WX_URL}    http://weishanghuzhushou.betanewwx.snsshop.net
${BETA_URL_BASEAPI}    http://betanewapi.snsshop.net/v1
${BETA_WX_USER}    13723232
@{G订单类型}          普通订单    秒杀    预售    pos收银    pos订单    拍码打折    扫码订单
...               拼团    积分订单
${CI_URL}         http://testnewwsh.snsshop.net/
${CI_WX_URL}      http://scliveapp2015.wx335.newwsh.snsshop.net
${CI_USER_ID}     137240011
${BETA_USER_ID}    13723232
${CI_WX_USER}     137240011
${CI_URL_API}     http://shanghutest.cxm/
${DEV_WX_USER}    ${EMPTY}
${CI_USERNAME}    7638800811
${CI_PASSWORD}    518000
${CI_SHOP_ID}     514

*** Keywords ***
Get_Env
    [Documentation]    获取运行环境
    ${flag_env}    Run Keyword And Return Status    Log    env:${env}
    ${GLOBAL_ENV}    Set Variable If    ${flag_env}==True    ${env}    beta    #默认beta
    Set Global Variable    ${GLOBAL_ENV}

Get_Headers
    [Arguments]    ${type}=json
    [Documentation]    说明：设置头文件模板，默认参数为json模板，其它任意参数为webform模板
    ####
    ${headers_json}    Create Dictionary    Accept-Language=zh-CN,zh;q=0.8    Accept-Encoding=gzip, deflate, sdch    Accept=application/json, text/plain, */*    Content-Type=application/json;charset=UTF-8    YT=debuging
    ${headers_form}    Create Dictionary    Accept-Language=zh-CN,zh;q=0.8    Accept-Encoding=gzip, deflate, sdch    Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8    Content-Type=application/x-www-form-urlencoded
    ${headers}    Set Variable If    '${type}'=='json'    ${headers_json}    ${headers_form}
    [Return]    ${headers}

环境配置
    [Arguments]    ${env}
    &{AUTO}    Create Dictionary    url=http://betanewwsh.snsshop.net/    username=20160912    password=123456    shop_id=98185    user_id=13764541
    ...    wx_url=${BETA_WX_URL}    wx_acc=wkdianshang    wx_user=${BETA_WX_USER}
    &{BETA}    Create Dictionary    url=http://betanewwsh.snsshop.net/    username=${BETA_USERNAME}    password=${BETA_PASSWORD}    shop_id=${BETA_SHOP_ID}    user_id=${BETA_USER_ID}
    ...    wx_url=${BETA_WX_URL}    wx_acc=weishanghuzhushou    wx_user=${BETA_WX_USER}
    &{CI}    Create Dictionary    url=http://shanghutest.cxm/    username=${CI_USERNAME}    password=${CI_PASSWORD}    shop_id=${CI_SHOP_ID}    user_id=${CI_USER_ID}
    ...    wx_url=${CI_WX_URL}    wx_acc=scliveapp2015    wx_user=${CI_WX_USER}
    &{DEV}    Create Dictionary    url=http://335.newwsh.snsshop.net/    username=${CI_USERNAME}    password=${CI_PASSWORD}    shop_id=${CI_SHOP_ID}    user_id=${CI_USER_ID}
    ...    wx_url=${CI_WX_URL}    wx_acc=scliveapp2015    wx_user=${CI_WX_USER}
    &{ENV_DICT}    Create Dictionary    beta=&{BETA}    ci=&{CI}    dev=&{DEV}    auto=&{AUTO}
    ###
    [Return]    &{ENV_DICT.${env}}

初始化
    Get Env
    ${GLOBAL_CONFIG}    环境配置    ${GLOBAL_ENV}
    Set Global Variable    ${GLOBAL_CONFIG}
    Log    测试环境：${GLOBAL_ENV}
