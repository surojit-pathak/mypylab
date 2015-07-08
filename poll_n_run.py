#
# Functionality:
#     - Poll a given directory 
#     - Load/reload modules from the directory
#     - run particular function from the module loaded
#
# Note: At present it using directory=$PWD, periodicity=5s, 
#          invoked functions 'foo'
# 
# Room for improvement:
#     - More error check
#     - More parameter driven
#
"""
Sample Usage:
[suro@surveyorslayers tmp]$ pwd
/home/suro/tmp
[suro@surveyorslayers tmp]$ cat a.py
def foo():
    print 'In mod A, function foo'
[suro@surveyorslayers tmp]$ cat b.py
def foo():
    print 'In mod b, function foo'
[suro@surveyorslayers tmp]$ python ~/github-surojit-pathak/mypylab/poll_n_run.py 
Iteration -  1
In mod A, function foo
In mod b, function foo
"""

import sys
import subprocess
import time

cmd = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE)
for path in cmd.stdout:   
    path = path.rstrip()
    break

sys.path.append(path)

def find_files():
    files = []
    cmd = subprocess.Popen('ls *.py', shell=True, stdout=subprocess.PIPE)
    for line in cmd.stdout:
        files.append(line)
    return files

def import_modules():
    files = find_files()
    modnames = []
    modules = []
    for f in files:
        mod = f.rstrip().split('.')[0]
        modnames.append(mod)
    for mod in modnames:
        module = __import__(mod)
        reload(module)
        modules.append(module)    

    return modules

count = 0
while True:
    time.sleep(5)
    count = count + 1
    print "Iteration - ", count
    modules = import_modules()
    for mod in modules:
        mod.foo()
    
