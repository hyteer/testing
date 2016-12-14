from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

print path.dirname(path.dirname(path.abspath(__file__)))

from demolib import DemoModule

dm = DemoModule()

print dm.dm_test("test1")
