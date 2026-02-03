import os
os.environ['CUDA_VISIBLE_DEVICES']='9'
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

model_path='/data/yanghq/models/deepseek-ai/DeepSeek-V2-Lite'
model_path='/new_data/yanghq/models/allenai/OLMoE-1B-7B-0125-Instruct'
model_path='/new_data/yanghq/models/Qwen/Qwen3-30B-A3B-Instruct-2507-FP8'
model_path='/new_data/yanghq/models/yuhuili/EAGLE-LLaMA3.1-Instruct-8B'
tokenizer_path='/new_data/yanghq/models/meta-llama/Llama-3.1-8B-Instruct'

model = AutoModelForCausalLM.from_pretrained(
    model_path,device_map='auto',trust_remote_code=True,
    torch_dtype=torch.float32,
    # attn_implementation='flash_attention_2',
    ).eval()

model_test = AutoModelForCausalLM.from_pretrained(
    tokenizer_path,device_map='auto',trust_remote_code=True,
    torch_dtype=torch.float32,
).eval()

with torch.no_grad():
    model.model.layers[0].input_layernorm.weight.copy_(model_test.model.layers[0].input_layernorm.weight.data)
    model.model.lm_head.weight.copy_(model_test.model.lm_head.weight.data)
    model.model.norm.weight.copy_(model_test.model.norm.weight.data)

# tokenizer = AutoTokenizer.from_pretrained(model_path,trust_remote_code=True,)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path,trust_remote_code=True,)

def gen(model,tokenizer,device='cuda:0'):
    input_text = "Once upon a time, "
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], max_new_tokens = 20, num_return_sequences=1, do_sample=False,)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print('\n',generated_text,'\n')

gen(model,tokenizer)
