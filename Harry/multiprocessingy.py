import multiprocessing #same as multithread just for bigger scale
import time
import concurrent.futures

def fun1(s):
    time.sleep(s)
    print(f'waited for {s} seconds')
    return s

i = 0

pn = []

# if __name__ == '__main__':
#     for _ in range(5):
#         p = multiprocessing.Process(target = fun1, args=[i])
#         p.start()
#         pn.append(p)
#         i += 1

#     for j in pn:
#         j.join()

if __name__ == '__main__':
    l = [1,5,8,6,4]
    with concurrent.futures.ProcessPoolExecutor() as ex:
        re = ex.map(fun1, l)








