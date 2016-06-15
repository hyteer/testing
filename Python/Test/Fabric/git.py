# encoding: utf-8
from fabric.api import local

def setting_ci():
    local("cd d:/Temp")
    local("git clone https://github.com/hyteer/Microblog.git")
    local("dir")