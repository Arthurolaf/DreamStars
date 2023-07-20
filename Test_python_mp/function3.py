def main():
    def other():
        pass
    def fun():
        import time
        import multiprocessing
        start = time.perf_counter()
        def please_sleep(n):
            print("Sleeping for {} seconds".format(n))
            time.sleep(n)
            print("Done Sleeping for {} seconds".format(n))

        p1 = multiprocessing.Process(target = please_sleep, args = [3])
        p2 = multiprocessing.Process(target = please_sleep, args = [2])
        p1.start()
        p2.start()
        finish = time.perf_counter()
        print("Finished in {} seconds".format(finish-start))
    fun()
    other()
if __name__=="__main__":
    print("Бесполезный ограничитель")