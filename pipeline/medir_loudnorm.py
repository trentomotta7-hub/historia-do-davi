#!/usr/bin/env python3
"""Extrai o JSON do print_format=summary/json do loudnorm e imprime atribuicoes shell."""
import json
import re
import sys

txt = open(sys.argv[1], encoding="utf-8", errors="ignore").read()
blocos = re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", txt, re.S)
if not blocos:
    print('I="-14.0" TP="-1.0" LRA="11" THR="-25" OFF="0"')
    sys.exit(0)
d = json.loads(blocos[-1])
print(f'I="{d["input_i"]}" TP="{d["input_tp"]}" LRA="{d["input_lra"]}" '
      f'THR="{d["input_thresh"]}" OFF="{d.get("target_offset", 0)}"')
