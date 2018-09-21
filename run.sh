#!/bin/bash
printf ">> Running N-Y Thing\n"
argv=("$@")
python3 src/main.py ${argv[0]}
printf "\n>> N-Y Thing closed\n"