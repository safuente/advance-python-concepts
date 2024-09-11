from multiprocessing import Pool


def f(x):
    return x*x


if __name__ == '__main__':
    """
    Pool offers a convenient means of parallelizing 
    the execution of a function across multiple 
    input values, distributing the input data across processes
    """
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
