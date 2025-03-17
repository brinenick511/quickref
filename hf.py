import os
import subprocess
import sys
import time
import glob

hf_token=""
hf_token+="hf_GwiXRPS"
hf_token+="cbwISYfe"
hf_token+="JSGzarur"
hf_token+="ZGaVOqeZSqQ"

def end(s=""):
    print(f'\n{s}\nexit(0)')
    exit(0)
    
def is_download_complete(download_path):
    safetensors_files = glob.glob(os.path.join(download_path, "*.safetensors"))
    if len(safetensors_files)<=0:
        return False
    if 'd' in safetensors_files[0][-17:-12]:
        num=1
    else:
        num = int(safetensors_files[0][-17:-12])
    return len(safetensors_files)==num

def download_huggingface(name, type="model", download_path=None, debugging=False):
    # 处理 type 参数的简写形式
    type = type.lower()
    if type in ("m", "model", "models"):
        type = "model"
    elif type in ("d","dataset", "datasets"):
        type = "dataset"
    
    if type not in ("model", "dataset"):
        print(f"Error type: {type}")
        show_help()
        sys.exit(1)
    
    # 生成默认下载路径
    if download_path is None:
        download_path = os.path.join(os.path.expanduser("~"), f"{type}s", name, "")
    else:
        download_path = os.path.abspath(os.path.expanduser(download_path))
    
    # 显示参数
    print(f"---\nNAME = {name}, TYPE = {type}, OUTPUT_DIR = {download_path}\n---")
    
    # 构建命令
    cmd = [
        "huggingface-cli",
        "download",
        "--local-dir-use-symlinks", "False",
        "--resume-download",
        name,
        "--local-dir", download_path,
        "--token", hf_token
    ]
    if type == "dataset":
        cmd.insert(2, "--repo-type")
        cmd.insert(3, "dataset")
    
    print("[INFO]".join(cmd))
    
    # 用户确认
    while debugging:
        answer = input("Do you want to continue? [y/n]: ").strip().lower()
        if answer == "y":
            break
        elif answer == "n":
            print("Exiting program.")
            sys.exit(0)
        else:
            print("无效输入，请输入 y 或 n。")
    
    flag=1
    while True:
        # 检查是否已经下载完成
        if is_download_complete(download_path):
            print(f"\n下载完成: {name} ({type})\n存储于: {download_path}")
            flag = 0
        # 启动下载进程
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if flag==0:
            process.terminate()
            break
        print("下载进行中 (60s 超时)...")

        # 等待 60 秒
        time.sleep(60)

        # 终止进程
        process.terminate()
        print("已下载60秒, 重启下载进程...")
    
    print(f"\nDone, {name}, {type}, {download_path}")

def show_help():
    help_text = """
用法: download_huggingface(name, type="model", download_path=None)

参数:
    name (str): 要下载的模型或数据集名称（必需）
    type (str): 类型，可选，默认为 'model'，支持 'model'/'m'/'models' 或 'dataset'/'d'/'datasets'
    download_path (str): 下载路径，可选，默认为 ~/{type}s/{name}/
"""
    print(help_text)

if __name__ == "__main__":
    
    # import argparse
    # parser = argparse.ArgumentParser(description="下载Hugging Face模型或数据集", add_help=False)
    # parser.add_argument("name", help="模型或数据集名称")
    # parser.add_argument("type", nargs='?', default="model", help="类型（model/dataset 或其简写）")
    # parser.add_argument("download_path", nargs='?', default=None, help="下载路径")
    # parser.add_argument("--help", action="store_true", help="显示帮助信息")
    # args = parser.parse_args()
    # if args.help:
    #     show_help()
    #     sys.exit(0)
    # download_huggingface(args.name, args.type, args.download_path)
    l=[
        'Qwen/Qwen2.5-14B-Instruct-AWQ',
        'Qwen/Qwen2.5-14B-Instruct-GPTQ-Int8',
        'Qwen/Qwen2.5-14B-Instruct-GPTQ-Int4',
        'Qwen/Qwen2.5-14B-Instruct',
        'unsloth/Qwen2.5-14B-Instruct-bnb-4bit',
        'unsloth/Qwen2.5-14B-Instruct-unsloth-bnb-4bit',
    ]
    l=[
        'Qwen/Qwen2.5-0.5B-Instruct-AWQ',
        'Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int8',
        'Qwen/Qwen2.5-0.5B-Instruct-GPTQ-Int4',
        'Qwen/Qwen2.5-0.5B-Instruct',
        'unsloth/Qwen2.5-0.5B-Instruct-bnb-4bit',
        'unsloth/Qwen2.5-0.5B-Instruct-unsloth-bnb-4bit',
    ]
    # l=['Qwen/Qwen2.5-0.5B',]
    for model_name in l:
        download_huggingface(model_name)
    