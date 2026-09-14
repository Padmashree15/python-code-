import multiprocessing

def main():
    print("cores : ",multiprocessing.cpu_count())

if __name__ == "__main__":
    main()