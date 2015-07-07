import multiprocessing
import time
import sys

def daemon():
    time.sleep(2)
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name

def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)

    d.start()
    time.sleep(1)
    d.join()
    n.start()




    n.join()
