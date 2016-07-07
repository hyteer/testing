# encoding: utf-8

from Lib.ApiTest import maisha
from Lib.ApiTest import settings
set = settings.Maisha()
print set.phone
print set.password

############ MaiSha ###########
cm = maisha.MaishaCommon()
user = maisha.MaishaUser()

# user_login
usersession = user.maisha_user_login(set.phone,set.password)

# user_set_tag
tags = ['Badboy','YT','Walker']
user.user_set_tag(usersession,tags)

# genqrcode
cm.maisha_get_qrcode(usersession,'test')

# user_getinfo
user.maisha_user_getinfo(usersession)

# user_public_config
cm.maisha_public_config(usersession)

# user_generate_captcha
cm.maisha_generate_captcha(usersession)

# user_check_up
cm.maisha_check_up('android')

# loading_ad
#cm.maisha_loading_ad(usersession)

# send_vercode
#cm.maisha_send_vercode(usersession)

# upload_file
#cm.upload_file(usersession,'D:\\Res\\test.png')

