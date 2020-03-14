import multiprocessing as mp

def job(x):
    x%=10
    return x*x
if __name__=="__main__":
    pool=mp.Pool(processes=4)
    res=[pool.apply(job,(i,)) for i in range(100000)]
    print("hh")
    print(res)
    # multi_res=[pool.apply_async(job,(i,)) for i in range(100000)]
    # print("hh")
    # print([res.get() for res in multi_res])
