n = 0
def add_it_up(a):
    global n;
    if type(a) == int:
         for i in range(a+1):
         n = i + n;
        return n;
    else:
        return 0;
colso=add_it_up(10)
print(result)