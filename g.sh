#!/bin/bash

nvidia_smi_output=$(nvidia-smi --query-compute-apps=pid,used_memory,process_name,gpu_bus_id,gpu_serial --format=csv,noheader)

if [ -z "$nvidia_smi_output" ]; then
    echo "No GPU processes found."
else
    echo "Username, Used Memory, Process Name, GPU ID,"
    # echo "$nvidia_smi_output"
    echo "$nvidia_smi_output" | while IFS=, read -r pid used_memory process_name gpu_bus_id gpu_serial
    do
        username=$(ps -o uname= -p $pid)
        echo "$username , $used_memory , $process_name , $gpu_bus_id"
    done
fi
