import ytglobal as glb

def get():
    glb.getBrowser()
    print "Browser is: " + glb.runEnv.BROWSER
    print "Platform is: " + glb.runEnv.PLATFORM
