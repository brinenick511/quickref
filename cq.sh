#!/bin/bash

output=$(python3 /new_data/yanghq/utils/quickref/cq.py | grep "^RESULT:" | cut -d':' -f2)

input_file='${HOME}/utils/quickref/gpu_list.txt'
input_file='/new_data/yanghq/utils/quickref/gpu_list.txt'
if [ -f "$input_file" ]; then
    input_string=$(cat "$input_file")
else
    echo "输入文件不存在。" > "$output_file"
    exit 1
fi

bash /new_data/yanghq/kivi/scripts/run_all.sh "$input_string"
