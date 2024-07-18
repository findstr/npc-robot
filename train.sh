#!/bin/sh
python3 ./tools/nlu.py
rasa train --domain=./domains
