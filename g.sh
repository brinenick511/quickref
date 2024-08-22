#!/bin/bash
declare -A gpu_map
gpu_map[" 00000000:02:00.0"]="0"
gpu_map[" 00000000:03:00.0"]="1"
gpu_map[" 00000000:82:00.0"]="2"
gpu_map[" 00000000:83:00.0"]="3"

nvidia_smi_output=$(nvidia-smi --query-compute-apps=pid,used_memory,process_name,gpu_bus_id,gpu_serial --format=csv,noheader)

if [ -z "$nvidia_smi_output" ]; then
    echo "No GPU processes found."
else
    printf "| %-8s|%10s| %-3s | %-20s\n" "USER " " MEMORY   " "GPU" "PROCESS"
    echo "$nvidia_smi_output" | while IFS=, read -r pid used_memory process_name gpu_bus_id gpu_serial
    do
        username=$(ps -o uname= -p $pid)
        gpu_id=${gpu_map[$gpu_bus_id]}
        printf "| %-8s|%-10s|  %-2s |%-20s\n" "$username" "$used_memory" "$gpu_id" "$process_name"
    done
fi