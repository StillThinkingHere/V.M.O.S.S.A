from plyer import notification
import time
while True:
    notification.notify(
        title="Avocado", message='Go to our website at http://66.135.9.182', app_name='Avocado', timeout=5)
    time.sleep(10000000)
