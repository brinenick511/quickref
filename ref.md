huggingface-cli download --local-dir-use-symlinks False --resume-download GPT --local-dir ./
huggingface-cli download --local-dir-use-symlinks False --repo-type dataset --resume-download WIKI --local-dir ./

pip install torch==1.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
pip install transformers==4.28 accelerate==0.19.0 numpy==1.22.4 deepspeed==0.9.0 scikit-learn flash-attn==2.0.1

screen -r [session]
screen -R [session]
screen -ls
Ctrl + D