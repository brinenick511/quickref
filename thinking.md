# overall

svd-llm + ft

soft count

reproduction: prune, merge

lme (vllm): lite&chat, qwen, moonlight, mixtral, phi,

---

# datasets & models

paper, model, test, cali, ft,

| Paper | Model | Test-set | Cali-set | FT-set |
| --- | --- | --- | --- | --- |
| NAEE | mx7,mx7i | ARC-c ARC-e BoolQ HellaSwag MMLU OBQA RTE WinoGrande, GSM8K, MATH | C4(128*2048) | MetaMathQA |
| SEER-MoE | mx7 | MMLU, SST5 |     |     |
| DEK | mx7,mx22, ds1,q2, | MMLU, BoolQ, OBQA, RTE | C4  |     |
| HC-SMoE | mx7,q1, | ARC-c ARC-e BoolQ HellaSwag MMLU OBQA RTE Winogrande | C4  |     |
| MoE-I2 | mx7, ds2,q1, | ARC-c ARC-e BoolQ HellaSwag OBQA RTE WinoGrande | C4  | Alpaca |

arc_challenge,arc_easy,boolq,hellaswag,openbookqa,rte,winogrande,

mmlu,

