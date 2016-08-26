*** Settings ***
Library           RequestsLibrary
Library           String
Library           Collections
Library           json
Resource          配置参数.robot

*** Keywords ***
API登录
    Create Session    wsh    ${URL_BETA}
    &{data}=    Create Dictionary    username=20151228    password=123456    captcha=1111
    &{headers}=    Create Dictionary    Content-Type=application/x-www-form-urlencoded
    ${resp}    Post Request    wsh    /login/login-ajax    data=${data}    headers=${headers}

获取店铺支付方式
    Create Session    baseapi    http://betanewapi.snsshop.net/v1
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Set Variable    {"shop_id":${SHOP_ID}}
    ${resp}    Post Request    baseapi    /payment/find-paytype-list    data=${jsonstr}
    Log    Response:${resp.content}
    ${resp_content}    Set Variable    ${resp.content}
    ${js}    loads    ${resp.content}
    ${errcode}    Get From Dictionary    ${js}    errcode
    Log    errcode:${errcode}
    [Return]    ${resp.content}

添加普通订单

工作台数据
    API登录
    ${resp}    Post Request    wsh    /data-center/workbench-count-data-ajax
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Log    errcode is:${errcode}
    Log    Resp:${resp.content}
    #Log    scan_limit_amount:${scan_limit}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    [Return]    ${errmsg}

工作台公告
    API登录
    ${resp}    Post Request    wsh    /data-center/workbench-notice-ajax
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Log    errcode is:${errcode}
    Log    Resp:${resp.content}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    [Return]    ${errmsg}

工作台广告
    API登录
    ${resp}    Post Request    wsh    /data-center/workbench-ad-ajax
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Log    errcode is:${errcode}
    Log    Resp:${resp.content}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    [Return]    ${errmsg}

商家信息
    API登录
    ${resp}    Post Request    wsh    /shop/get-ajax
    Log    Response:${resp.content}
    ${len}    Get Length    ${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    Log    Res2:${str}
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Log    errcode is:${errcode}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    [Return]    ${errmsg}

会员_标签列表
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"name":""}
    ${resp}    Post Request    wsh    /members/find-tag-ajax    data=${jsonstr}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ###
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

-----1-----

客户_列表
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"nickname":"","group_id":null,"shop_sub_id":"","agent_id":"","is_search":false,"belong_to_staff_id":"","createStart":"","createEnd":"","group_ids":[],"yestoday":false,"user_platform":0,"tags":[]}
    ${resp}    Post Request    wsh    /member/list-ajax    data=${jsonstr}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    接口返回异常！
    [Return]    ${errmsg}

客户_详情
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"id":${id}}
    ${resp}    Post Request    wsh    /member/member-detail-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

客户_统计
    API登录
    ${resp}    Post Request    wsh    /member/count-wx-member
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    Log    errcode is:${errcode}
    Log    Resp:${resp.content}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

客户_积分统计
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"user_id":${id}}
    ${resp}    Post Request    wsh    /data/user-point-count-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

客户_积分列表
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"type_id":1,"id":"${id}"}
    ${resp}    Post Request    wsh    /member/point-list-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

-----2-----

会员_列表
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":0,"_page_size":1,"is_get_card":1}
    ${resp}    Post Request    wsh    /members/list-ajax    data=${jsonstr}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员_统计
    API登录
    ${resp}    Post Request    wsh    /members/last-count-ajax
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    Log    errcode is:${errcode}
    Log    Resp:${resp.content}
    Run Keyword If    ${errcode}==0    Log    Success
    ...    ELSE    Log    Failed
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员_详情
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"id":${id}}
    ${resp}    Post Request    wsh    /members/detail-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员_分组列表
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"name":""}    # 分页参数：{"_page":1,"_page_size":20,"name":""}
    ${resp}    Post Request    wsh    /members/find-group-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员_成长明细
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"member_id":${id}}
    ${resp}    Post Request    wsh    /member/member-growth-detail    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

客户_消费记录
    [Arguments]    ${id}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"uid":"${id}"}
    ${resp}    Post Request    wsh    /members/find-member-order-list-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

全部客户_消费记录
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"real_name":"","bind_mobile":"","order_no":"","createStart":"","createEnd":"","total_price_min":"","total_price_max":"","shop_sub_id":[],"order_type":[]}
    ${resp}    Post Request    wsh    /members/find-member-order-list-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员列表_条件查询
    [Arguments]    ${name}=${EMPTY}    ${start}=${EMPTY}    ${end}=${EMPTY}    ${mobile}=${EMPTY}    ${status}=[]    ${source}=[]
    ...    ${level}=[]    ${group_id}=[]    ${tags}=[]    ${sex}=[]
    [Documentation]    查询参数：
    ...    {"_page":1,"_page_size":20,"keyword":"","real_name":"","create_start":1467611419,"create_end":1472104227,"bind_mobile":"","status":[],"source":[],"level":[],"member_group_id":[],"tags":[],"sex":[],"city_id":[],"city":[],"shop_sub_id":""}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"keyword":"","real_name":"${name}","create_start":"${start}","create_end":"${end}","bind_mobile":"${mobile}","status":${status},"source":${source},"level":${level},"member_group_id":${group_id},"tags":${tags},"sex":${sex},"city_id":[],"city":[],"shop_sub_id":""}
    ${resp}    Post Request    wsh    /members/list-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员列表_条件查询2
    [Arguments]    ${args}
    [Documentation]    查询参数：
    ...    {"_page":1,"_page_size":20,"keyword":"","real_name":"","create_start":1467611419,"create_end":1472104227,"bind_mobile":"","status":[],"source":[],"level":[],"member_group_id":[],"tags":[],"sex":[],"city_id":[],"city":[],"shop_sub_id":""}
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    ${args}
    ${resp}    Post Request    wsh    /members/list-ajax    data=${jsonstr}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

会员_获取全部分组
    API登录
    &{headers}    Create Dictionary    Accept=application/json    Content-Type=application/json
    ${jsonstr}    Convert To String    {"_page":1,"_page_size":20,"name":""}    # 分页参数：{"_page":1,"_page_size":20,"name":""}
    ${resp}    Post Request    wsh    /members/find-all-group-ajax    \    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    [Return]    ${errmsg}

微信_获取二维码详情
    API登录
    &{headers}    Get_Headers
    &{data}=    Create Dictionary    model=member_card    model_id=1    shop_sub_id=0
    ${resp}    Post Request    wsh    /members/find-all-group-ajax    data=${data}    headers=${headers}
    Log    Response:${resp.content}
    ${str}    Get Substring    ${resp.content}    3
    ${js}    loads    ${str}
    ${errcode}    Get From Dictionary    ${js}    errcode
    ${errmsg}    Get From Dictionary    ${js}    errmsg
    Run Keyword If    ${errcode}!=0    Fail    接口返回异常！
    ##
    [Return]    ${errmsg}
