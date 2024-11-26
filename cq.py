import dei_utils
import time

if __name__ == "__main__":
    print('cq')
    t=10
    t = 2 * 2.5 * 60*60
    print(f'sleep for {t} seconds')
    time.sleep(t)
    # cq = dei_utils.Dei_Conqueror(5, 1, 5)
    cq = dei_utils.Dei_Conqueror(5*60, 10, 5)
    cq.conquer()