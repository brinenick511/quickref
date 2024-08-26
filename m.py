import pynvml
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
import argparse
from tqdm import tqdm

pynvml.nvmlInit()

gpu_count = pynvml.nvmlDeviceGetCount()

memory_threshold = 3700 # MB
sleep_seconds = 60 # seconds

def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', action='store_true', help="send email")
    return parser.parse_args(args)

def get_time():
    return str(time.strftime('%m/%d %H:%M:%S',time.localtime(time.time())))

def send_qq_email(subject='### GPU提醒 ###', body='<=GPU提醒=>'):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '2057807259@qq.com'
    msg['To'] = '2747350438@qq.com'

    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    sender_email = '2057807259@qq.com'
    password = 'pobnlymirwhmciba'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, [msg['To']], msg.as_string())
        print('邮件发送成功')
        sys.exit(0)
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))
def draw_memory():
    mem=[0.]*gpu_count
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        used_memory_mb = memory_info.used / 1024 / 1024  # MB
        total_memory_mb = memory_info.total / 1024 / 1024
        mem[i]=used_memory_mb / total_memory_mb
        mem[i]=int(round(mem[i]*100))
    for i in range(gpu_count):
        with tqdm(total=100,desc=f"# GPU {i}") as pbar:
            for i in range(mem[i]):
                # pbar.set_postfix_str('',)
                pbar.update(1)
    
def check_gpu_memory(send_email):
    if not send_email:
        return draw_memory()
    mem=[0.]*gpu_count
    flag=False
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        used_memory_mb = memory_info.used / 1024 / 1024  # MB
        total_memory_mb = memory_info.total / 1024 / 1024
        mem[i]=used_memory_mb/1024
        mem[i]=int(mem[i]*100)/100
        
        print(f"GPU {i}: {used_memory_mb/1024:.2f} / {total_memory_mb/1024:.2f} | {used_memory_mb/total_memory_mb*100:.2f}%")
        
        if used_memory_mb < memory_threshold:
            flag=False
            print(f"Alert: GPU {i} memory usage is below threshold: {used_memory_mb/1024:.2f} GB")
    if flag:
    # if True:
        s='|'
        for i in range(gpu_count):
            s+=f' {i}, {mem[i]}GB |'
        send_qq_email(body=s)
        
if __name__ == "__main__":
    args = parse_args()
    if args.e:
        init_time = get_time()
        cnt=0
        while True:
            print(f'\n------\n| {init_time} | {get_time()} | count={cnt}\n------\n')
            check_gpu_memory(args.e)
            print(f'\nQuery again in {sleep_seconds} seconds...')
            cnt+=1
            time.sleep(sleep_seconds)  # seconds
    else:
        init_time = get_time()
        # print(f'\n------\n| {init_time} | {get_time()}\n------\n')
        check_gpu_memory(args.e)
