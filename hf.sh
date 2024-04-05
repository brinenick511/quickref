#!/bin/bash

# 帮助信息函数
show_help() {
cat << EOF
用法: ${0##*/} 参数1 参数2 参数3

    NAME=${1}
    TYPE=${2:-"model"}
    OUTPUT_DIR=${3:-"/data/yanghq/${TYPE}s/${NAME}/"}

EOF
}

NAME=${1}
TYPE=${2:-"model"}
OUTPUT_DIR=${3:-"/data/yanghq/${TYPE}s/${NAME}/"}
if [ $# -lt 1 ] || [ $# -gt 3 ]; then
    echo "传递给脚本的参数个数：$#"
    show_help
    exit 1
fi

if [ "$TYPE" = "model" ]; then
    echo "huggingface-cli download --local-dir-use-symlinks False --resume-download $NAME --local-dir $OUTPUT_DIR"
    huggingface-cli download --local-dir-use-symlinks False --resume-download $NAME --local-dir $OUTPUT_DIR --token "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"
elif [ "$TYPE" = "dataset" ]; then
    echo "huggingface-cli download --local-dir-use-symlinks False --repo-type dataset --resume-download $NAME --local-dir $OUTPUT_DIR"
    huggingface-cli download --local-dir-use-symlinks False --repo-type dataset --resume-download $NAME --local-dir $OUTPUT_DIR --token "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"
else
    echo "传递给脚本的参数个数：$#"
    show_help
    exit 1
fi

echo ""
echo "Done, ${NAME}, ${TYPE}, ${OUTPUT_DIR}"