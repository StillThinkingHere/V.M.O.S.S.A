@echo off
setlocal

:loop
python -c "from plyer import notification; import time; notification.notify(title='Avocado', message='Go to our website at http://66.135.9.182', app_name='Avocado', timeout=5)"
ping -n 9999999999999 127.0.0.1 > nul
goto loop
