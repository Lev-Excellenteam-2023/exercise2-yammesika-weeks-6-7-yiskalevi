# Yiska Levi

def group_by(func, iterable):
    ans=map(func, iterable)
    keys=set(ans)
    my_dict = {key: [el for el in iterable if func(el)==key] for key in keys}
    return my_dict

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))