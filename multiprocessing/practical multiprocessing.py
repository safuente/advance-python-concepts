from multiprocessing import Process, cpu_count, current_process


def print_func(continent='Asia'):
    print(current_process().name)

    print('The name of continent is : ', continent)


if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()
    print("Number of cpus : ", cpu_count())

    # instantiating process with arguments
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
