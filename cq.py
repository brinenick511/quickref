import dei_utils as dei
import time

def py_exit(s='test'):
    # input_file = '~/utils/quickref/gpu_list.txt'
    input_file = '/new_data/yanghq/utils/quickref/gpu_list.txt'
    with open(input_file, "w") as f:
        f.write(s)
    print(f'RESULT:{s}')
    exit(0)

if __name__ == "__main__":
    # for i in range(2):
    #     time.sleep(2)
    # py_exit('0 1 2 3')
    
    print('cq')
    t = 2
    # t = 1.5 * 60*60
    
    t = int(t)
    print(f'sleep for {t} seconds')
    time.sleep(t)
    while True:
        # cq = dei.Conqueror(
        #     interval_sec = 5*60,
        #     mercy = 5,
        #     max_num = 8,
        #     sleep_sec = 5,
        # )
        cq = dei.Conqueror(5*60, 0, 9, 5, )
        tmp = cq.conquer()
        if tmp is None or tmp == '0':
            pass
        else:
            py_exit(tmp)
    