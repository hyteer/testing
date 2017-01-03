import ytglobal as GlobalVar

def SetBrowser():
    GlobalVar.setBrowser('chrome')
def SetPlatform():
    # Create an instance of class runEnv
    env = GlobalVar.runEnv()
    env.setPlatform('WINDOWS')  # Set global
    env.PLATFORM = "Linux"  # Set local
    #print "Platform: " + env.PLATFORM





