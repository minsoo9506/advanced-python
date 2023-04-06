"""
- multiprocessing
    - Join, is_alive
"""

from multiprocessing import Process
import time
import logging

def proc_func(name):
      print(f"Sub-Process {name}: start!")
      time.sleep(3)
      print(f"Sub-Process {name}: finish!")

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    p = Process(target=proc_func, args=('first',))

    logging.info("main-process: before creating process")
    
    p.start()
    
    logging.info("main-process: During Process")

    logging.info("main-process: Joining Process")
    p.join()

    print(f"Process p is alive: {p.is_alive()}")  # p 끝났으니 false 나옴

"""결과
22:48:04: main-process: before creating process
22:48:04: main-process: During Process
22:48:04: main-process: Joining Process
Sub-Process first: start!
Sub-Process first: finish!
Process p is alive: False
"""