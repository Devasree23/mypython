def dec_fun(fn):
    def inn_fun(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inn_fun

@dec_fun
def sub(n1,n2):
    return n1-n2  

print(sub(10,20))