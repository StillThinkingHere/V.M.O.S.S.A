import threading

def run1():import fir_run
def run2():import sec_run
fir=threading.Thread(target=run2).start()
sec=threading.Thread(target=run1).start()