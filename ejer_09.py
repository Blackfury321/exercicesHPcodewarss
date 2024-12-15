def tree(times):
    for i in range(1, times + 1):  #
       e = " " * (times - i)
       a = "*" * (2 * i - 1)
       print(e + a)
times = int(input(""))

tree(times)
