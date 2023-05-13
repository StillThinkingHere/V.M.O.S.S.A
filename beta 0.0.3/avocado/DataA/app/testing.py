from subprocess import Popen
p = Popen("setup.bat")
stdout, stderr = p.communicate()
