# Yiska Levi

import time

def timer(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

#check that is wark
def my_func(*args):
    # Function code here
    time.sleep(2)  # Example delay of 2 seconds
if __name__ == '__main__':
    print("Time taken:", timer("Hi {name}".format, name="Bug"), "seconds")
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer(my_func))
