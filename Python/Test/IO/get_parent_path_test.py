import os

curpath = os.path.dirname(__file__)

def yt_get_parent_path(curdir,subdir=None):
        # Get a dir's path
        path = None
        if subdir == None:
            newpath = os.path.abspath(os.path.join(curdir, os.pardir))
        else:
            newpath = os.path.abspath(os.path.join(curdir, os.pardir, subdir))
        return newpath

parpath1 = yt_get_parent_path(curpath)  # Test
parpath2 = yt_get_parent_path(parpath1) # Python
robot_path = yt_get_parent_path(parpath2,"Robot") # Testing/Robot

#print "org path:",curpath
print "new path:",robot_path




