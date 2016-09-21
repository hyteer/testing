*** Settings ***
Library           Selenium2Library
Resource          配置参数.robot
Resource          功能菜单.robot
Library           String
Library           Screenshot
Library           OperatingSystem
Resource          API.robot

*** Keywords ***
随机获取一个商品
    ${errmsg}    API.商品_列表
    ${data}    Get From Dictionary    ${errmsg}    data
    ${list}    Get Length    ${data}
    ${rand}    Evaluate    random.randint(1,${list})    random
    ${rand_product}    Set Variable    ${data[${rand}]}
    [Return]    ${rand_product}

获取一个开启的商品

获取一个特定条件商品
    [Arguments]    ${reserves}=${1}    ${status}=1    ${quota}=0
    [Documentation]    注：默认获取库存大于0的商品，并已上架的商品
    ...    ${status}为商品状态：1为开启状态，2为关闭状态
    ...    ${reserves}为库存数量
    ...    ${quota}为商品每人限制购买数量,0为不限制数量
    ${errmsg}    商品_列表
    ${data}    Get From Dictionary    ${errmsg}    data
    : FOR    ${product}    IN    @{data}
    \    ${id}    Get From Dictionary    ${product}    id
    \    ${reserves_api}    Get From Dictionary    ${product}    reserves
    \    ${status_api}    Get From Dictionary    ${product}    status
    \    ${quota_api}    Get From Dictionary    ${product}    quota
    \    Run Keyword If    ${quota}==0    Exit For Loop If    ${reserves_api}>=${reserves} and ${status_api}==${status} and ${quota_api}==${quota}
    \    ...    ELSE    Exit For Loop If    ${reserves_api}>=${reserves} and ${status_api}==${status} and ${quota_api}>=${quota}
    ##查找结果判断
    ${flag}    Run Keyword If    ${quota}==0    Evaluate    ${reserves_api}>=${reserves} and ${status_api}==${status} and ${quota_api}==${quota}
    ...    ELSE    Evaluate    ${reserves_api}>=${reserves} and ${status_api}==${status} and ${quota_api}>=${quota}
    Run Keyword If    ${flag}==False    Fail    分页第1页未找到符合条件的商品！
    Log    找到符合条件的商品！
    [Return]    ${product}

添加一个商品
    [Arguments]    ${上架}=False    ${产品名称}=随机    ${价格}=随机
    ${产品名称}    Run Keyword If    '${产品名称}'=='随机'    随机字符    【测试商品】    12
    ...    ELSE    Set Variable    ${产品名称}
    ${价格}    Run Keyword If    '${价格}'=='随机'    随机价格
    ...    ELSE    Set Variable    ${价格}
    ${销量}    Evaluate    random.randint(10,10000)    random
    ${库存}    Evaluate    random.randint(100,5000)    random
    ${条件码1}    随机数字    8
    ${条件码2}    随机数字    8
    ###
    ${args}    Set Variable    {"productInfo":{"detail_pic":"504883,504865,","detail":"<p>YT的测试商品介绍。。。</p>"},"product":{"product_type":1,"name":"${产品名称}","sales":"${销量}","covers_id":504883,"quota":"3","sort":"0","sale_scope":"1","product_category_id":33694,"product_category_path":"/33691/33694/","status":2,"postage_fee_type":0,"product_kind_ids":"205477;","show_sale_num":2,"prod_weight":"200"},"shareMessage":{"desc":"优惠多多,欢迎选购","title":"${产品名称}","file_cdn_path":"http://imgcache.vikduo.com/static/2a32cbf5f166995eb5dbfca47e4de0ca.png","pic_id":504883},"kindBody":[{"firstName":"50g","firstRowSpan":1,"firstShow":true,"id":"50g","status":false},{"firstName":"150g","firstRowSpan":1,"firstShow":true,"id":"150g","status":false}],"skus":[{"status":1,"reserves":${库存},"market_price":"18","retail_price":"${价格}","sku_no":"T000101","barcode":"${条件码1}","sales":0,"name":"${产品名称}","kind_value_ids":[846106],"kind_ids":[205477]},{"status":1,"reserves":300,"market_price":"26","retail_price":"${价格}","sku_no":"T000102","barcode":"${条件码2}","sales":0,"name":"${产品名称}","kind_value_ids":[846108],"kind_ids":[205477]}]}
    ${errmsg}    API.商品_添加商品    ${args}
    #
    Run Keyword If    ${上架}!=True    Pass Execution    不上架...
    ${product}    Get From Dictionary    ${errmsg}    product
    ${id}    Get From Dictionary    ${product}    id
    商品_上架    ${id}
    Log    上架成功!
    #
    [Return]    ${errmsg}

获取会员优惠信息
    [Arguments]    ${id}
    ${errmsg}    API.会员_详情    ${id}
    ####返回信息拆解
    ${member_no}    Get From Dictionary    ${errmsg}    member_no
    ${wxUserInfos}    Get From Dictionary    ${errmsg}    wxUserInfos
    ${memberGrade}    Get From Dictionary    ${errmsg}    memberGrade
    ${memberGroup}    Get From Dictionary    ${errmsg}    memberGroup
    ${shopAgent}    Get From Dictionary    ${wxUserInfos}    shopAgent
    ${shopAgent_len}    Get Length    ${shopAgent}
    ${shopInfo}    Get From Dictionary    ${wxUserInfos}    shopInfo
    ${shopInfo_len}    Get Length    ${shopInfo}
    ${belongStaff}    Get From Dictionary    ${wxUserInfos}    belongStaff
    ${belongStaff_len}    Get Length    ${belongStaff}
    ${belongToFxMember}    Get From Dictionary    ${wxUserInfos}    belongToFxMember
    ${belongToFxMember_len}    Get Length    ${belongToFxMember}
    ####优惠信息
    ${优惠信息}    Create Dictionary
    ${会员卡编号_API}    Get From Dictionary    ${errmsg}    member_no
    ${会员卡状态_API}    Get From Dictionary    ${errmsg}    member_card_activate_id
    ${会员卡状态_API}    Set Variable If    ${会员卡状态_API}==1    正常    ${会员卡状态_API}==2    禁止
    ${会员等级_API}    Get From Dictionary    ${memberGrade}    name
    ${会员成长值_API}    Get From Dictionary    ${errmsg}    growth
    ${会员折扣_API}    Get From Dictionary    ${memberGrade}    discount    #返回值是10倍
    ${会员折扣_API}    Evaluate    ${会员折扣_API}*0.1
    ${账户积分_API}    Get From Dictionary    ${wxUserInfos}    point
    Set To Dictionary    ${优惠信息}    折扣=${会员折扣_API}    积分=${账户积分_API}
    [Return]    ${优惠信息}
