import ytglobal
import ytSet
import ytGet

print "---Use ytSet() to set global---"
ytSet.SetBrowser()
print "#1 Isolate Method, set browser to: " + ytglobal.runEnv.BROWSER


ytSet.SetPlatform()
print "#2 Class Method, set browser to: " +  ytglobal.runEnv.PLATFORM
print "Directly get Browser: " + ytglobal.runEnv.BROWSER
print "---Use ytGet() to get global---"
ytGet.get()

