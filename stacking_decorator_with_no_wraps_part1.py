import time
import logging
def cal_time(orig_func):

    def  wrapper(*args,**kwargs):
        t1=time.time()
        result=orig_func(*args,**kwargs)
        t2=time.time()-t1
        print(f"time taken for {orig_func.__name__} is {t2} ")
    return wrapper

def decorator_func(orig_func):
    logging.basicConfig(filename= f'{orig_func.__name__}_b.log', level=logging.INFO)
    def wrapper(*args,**kwargs):
        logging.info(f"{orig_func.__name__} ran with args:{args} and kwargs:{kwargs}")
        return orig_func(*args,**kwargs)
    return wrapper


@cal_time
@decorator_func
def display_info(name,age,**kwargs):
    time.sleep(10)
    print (f'this guy ({name},{age},{kwargs})')
display_info("ramesh",24,pay=100000)
