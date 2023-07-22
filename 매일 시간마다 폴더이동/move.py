import os,sys
import shutil
from time import sleep
from datetime import date, time, datetime, timedelta

print("os.getcwd()               : ",os.getcwd())
sys.path.append(os.getcwd())

#-----------------------------------
import subprocess
import pkg_resources

required  = {'schedule'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
#-----------------------------------

while True:
    if os.path.isdir("ComfyUI/output/"):
        print(shutil.move("ComfyUI/output/","ComfyUI/output3/"+datetime.now().strftime("%y-%m-%d %H-%M-%S")))
    d=date.today()+timedelta(days=1)
    #print(d)
    t=time(5)
    #print(t)
    n1=datetime.now()
    #print(n1)
    n2=datetime.combine(d, t)
    #print(n2)
    n3=n2-n1
    #print(n3)
    #print(n3.seconds)
    sleep(n3.seconds)

#def my():
#    print(shutil.move("ComfyUI/output","ComfyUI/output3"))

#schedule.every().day.at("05:30").do(my)
