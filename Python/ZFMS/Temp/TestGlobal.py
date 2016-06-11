
from args import globalArgs

g = globalArgs

g.setBrowser('Opera')
g.setPlatform('Unix')
desired_caps = {
        'platform': g.runEnv.PLATFORM,
        'browserName': g.runEnv.BROWSER
        # 'platform': "WINDOWS",
        #'browserName': "firefox"

    }


print "Browser is: " + g.getBrowser()
print "Platform is: " + g.getPlatform()
print "Br is: " + g.runEnv.BROWSER
print "desired_caps is: " + str(desired_caps)

