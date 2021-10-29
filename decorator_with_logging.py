import logging
def outs_func(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}_a.log",level=logging.INFO)
    def wrapper(*args,**kwargs):
        result=orig_func(*args,**kwargs)
        logging.info(f"the original function is {orig_func.__name__} with {args}")
        return result
    return wrapper

@outs_func
def add(x,y):
    print(f"the sum of {x} and {y} is {x+y}")
    return("testing")
a=add(4,5)
#print(a)
