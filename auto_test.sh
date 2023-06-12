#!/bin/bash

source venv/Scripts/activate
py -m pytest
if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi
