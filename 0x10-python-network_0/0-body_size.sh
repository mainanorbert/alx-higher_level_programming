#!/bin/bash
# Bash script that takes in a URL, sends 
curl -s "$1" | wc -c
