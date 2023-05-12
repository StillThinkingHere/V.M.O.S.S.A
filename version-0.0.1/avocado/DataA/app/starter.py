import threading

def run1():
    import fir_run
def run2():
    import sec_run

fir = threading.Thread(target=run2)
sec = threading.Thread(target=run1)

fir.start()
sec.start()