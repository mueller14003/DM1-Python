print_fun_list = lambda f,l: list(map(lambda i: print(i),list(map(lambda i: f(i),l))))
print_fun_list(type,[12,12.0,"12",[12],(12,12),{12:12},lambda x:x])