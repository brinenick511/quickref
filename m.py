import pynvml
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys

pynvml.nvmlInit()

gpu_count = pynvml.nvmlDeviceGetCount()

memory_threshold = 3700 # MB
sleep_seconds = 60 # seconds

def get_time():
    return str(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time())))

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
    except smtplib.SMTPException as e:
        print('邮件发送失败:', str(e))

def check_gpu_memory():
    mem=[0.]*gpu_count
    flag=False
    print(f'\n------\n{get_time()}\n------\n')
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        used_memory_mb = memory_info.used / 1024 / 1024  # MB
        total_memory_mb = memory_info.total / 1024 / 1024
        mem[i]=used_memory_mb/1024
        mem[i]=int(mem[i]*100)/100
        
        print(f"GPU {i}: {used_memory_mb:.2f} MB used / {total_memory_mb:.2f} MB total")
        
        if used_memory_mb < memory_threshold:
            flag=False
            print(f"Alert: GPU {i} memory usage is below threshold: {used_memory_mb:.2f} MB")
    if flag:
    # if True:
        s='|'
        for i in range(gpu_count):
            s+=f' {i}, {mem[i]}GB |'
        send_qq_email(body=s)
        sys.exit(0)
        
if __name__ == "__main__":
    while True:
        check_gpu_memory()
        print(f'\nQuery again in {sleep_seconds} seconds...')
        time.sleep(60)  # seconds
