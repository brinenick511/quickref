实时MT+pause
置信度

# 跑实验
看论文、看代码、改代码


# 以下是找论文

是否可以认为LLM做MT一定要经历一个很大的pretrain？都是基于一个已经pretrain好的模型（LLama之类）再做pretrain+finetune，所以连alma的第一阶段mono-oscar都写的finetune。
那么不需要纠结"standard-pretrain"有没有影响了，因为一定是这样的。
唯一的区别是，"pretrain"好的模型非常大，alma是7b/13b版本，如果我从头train的话可以选小模型

ALMA: PT,Mono,FT,CPO:
自己跑=Standard{PT}, Pause{Mono,FT,CPO}，但空间很大
跑源码=Standard{PT, Mono}, Pause{FT,CPO}，但模型很大

// 但其实似乎不需要太过纠结于"不使用<pause>的PreTrain"？
反正只是一个尝试和探索，而不是真正地复现原论文。如果效果不好那就是pretrain的锅


解决方案：
```
0. 问导师
1. 换别的论文和代码，都不需要找模型小的(7B完全可以)(因为要换)，只需要找数据集不是特别大的(尤其是PT)
1.1. 先看导给的及其相关的
2. 自己跑ALMA，"切"or"换" 数据集
3. 
```

现行思路：
```
1.找论文：
新(含2023)、开源、LLM做机器翻译
代码好跑好看懂(stars多)、
数据集不要太大(最大128G)、
模型大小不重要(最大13B)、decoder-only架构(好像全是)

```