
import re

str = """vars.put("orderDetails[0][comment_status]",comment_status);
vars.put("orderDetails[0][postage_fee_type]",postage_fee_type);
vars.put("orderDetails[0][created]",created);
vars.put("orderDetails[0][modified]",modified);
vars.put("orderDetails[0][policy_type]",policy_type);
vars.put("orderDetails[0][policy_value]",policy_value);
vars.put("orderDetails[0][brokerage]",brokerage);
vars.put("orderDetails[0][policy_level_id]",policy_level_id);
vars.put("orderDetails[0][productImg][id]",img_id);
vars.put("orderDetails[0][productImg][name]",img_name);
vars.put("orderDetails[0][productImg][desc]",img_desc);
vars.put("orderDetails[0][productImg][category_id]",img_category_id);
vars.put("orderDetails[0][productImg][tag_id]",img_tag_id);
vars.put("orderDetails[0][productImg][file_cdn_path]",file_cdn_path);
vars.put("orderDetails[0][productImg][file_type]",file_type);
vars.put("orderDetails[0][productImg][shop_id]",img_shop_id);
vars.put("orderDetails[0][productImg][shop_sub_id]",img_shop_sub_id);
vars.put("orderDetails[0][productImg][shop_sub_id]",img_created);
vars.put("orderDetails[0][productImg][shop_sub_id]",img_modified);
vars.put("orderDetails[0][productImg][shop_sub_id]",img_deleted);
vars.put("orderDetails[0][can_use_member_discount]",can_use_member_discount);"""

str2 = re.sub(r'(?<=vars.put\(").+(?=",\w)','',str)

str3 = re.search(r'(?<=",).+(?=\);)',str)




