#!/bin/bash

# 帮助信息函数
show_help() {
cat << EOF
用法: ${0##*/} 参数1 参数2 参数3

    NAME=${1}
    TYPE=${2:-"model"}
    OUTPUT_DIR=${3:-"${HOME}/${TYPE}s/${NAME}/"}

EOF
}

prompt_continue() {
    while true; do
        read -p "Do you want to continue? [y/n]: " input
        case $input in
            [Yy]* ) break;;
            [Nn]* ) echo "Exiting program."; exit;;
            * ) echo "Invalid input. Please enter y or n.";;
        esac
    done
}

for arg in "$@"; do
    if [[ "$arg" == "--help" ]]; then
        show_help
        exit 1
    fi
done

NAME=${1}
TYPE=${2:-"model"}

if [ "$TYPE" = "m" ]; then
    TYPE="model"
elif [ "$TYPE" = "models" ]; then
    TYPE="model"
elif [ "$TYPE" = "d" ]; then
    TYPE="dataset"
elif [ "$TYPE" = "datasets" ]; then
    TYPE="dataset"
fi

OUTPUT_DIR=${3:-"${HOME}/${TYPE}s/${NAME}/"}

if [ $# -lt 1 ] || [ $# -gt 3 ]; then
    echo "传递给脚本的参数个数：$#"
    show_help
    exit 1
fi

show_param() {
    echo "NAME = ${NAME}, TYPE = ${TYPE}, OUTPUT_DIR = ${OUTPUT_DIR}"
}

if [ "$TYPE" = "model" ]; then
    show_param
    echo "hf download $NAME --local-dir $OUTPUT_DIR"
    prompt_continue
    hf download $NAME --local-dir $OUTPUT_DIR --token ${HF_TOKEN}
elif [ "$TYPE" = "dataset" ]; then
    show_param
    echo "hf download --repo-type dataset $NAME --local-dir $OUTPUT_DIR"
    prompt_continue
    hf download --repo-type dataset $NAME --local-dir $OUTPUT_DIR --token ${HF_TOKEN}
else
    echo "下载类型错误：$#"
    show_help
    exit 1
fi

echo ""
echo "Done, ${NAME}, ${TYPE}, ${OUTPUT_DIR}"