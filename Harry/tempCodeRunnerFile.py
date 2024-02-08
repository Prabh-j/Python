    l = [1,5,8,6,4]
    with concurrent.futures.ProcessPoolExecutor() as ex:
        re = ex.map(fun1, l)