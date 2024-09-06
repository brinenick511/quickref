#!/bin/bash
declare -A gpu_map
gpu_map[" 00000000:02:00.0"]="0"
gpu_map[" 00000000:03:00.0"]="1"
gpu_map[" 00000000:82:00.0"]="2"
gpu_map[" 00000000:83:00.0"]="3"

gpu_map[" 00000000:1A:00.0"]="0"
gpu_map[" 00000000:1B:00.0"]="1"
gpu_map[" 00000000:1C:00.0"]="2"
gpu_map[" 00000000:1D:00.0"]="3"
gpu_map[" 00000000:1E:00.0"]="4"
gpu_map[" 00000000:3D:00.0"]="5"
gpu_map[" 00000000:3E:00.0"]="6"
gpu_map[" 00000000:3F:00.0"]="7"
gpu_map[" 00000000:40:00.0"]="8"
gpu_map[" 00000000:41:00.0"]="9"

nvidia_smi_output=$(nvidia-smi --query-compute-apps=pid,used_memory,process_name,gpu_bus_id,gpu_serial --format=csv,noheader)

if [ -z "$nvidia_smi_output" ]; then
    echo "No GPU processes found."
else
    printf "| %-8s| %-3s |%10s | %-15s\n" "USER " "GPU" " MEMORY   " "PROCESS"
    echo "$nvidia_smi_output" | while IFS=, read -r pid used_memory process_name gpu_bus_id gpu_serial
    do
        username=$(ps -o uname= -p $pid)
        gpu_id=${gpu_map[$gpu_bus_id]}
        if [[ $process_name == *"envs"* ]]; then
            process="${process_name##*envs}"
            process=" ...$process"
        else
            process="$process_name"
fi
        printf "| %-8s|  %-2s |%-10s |%-15s\n" "$username" "$gpu_id" "$used_memory" "$process"
    done
fi
