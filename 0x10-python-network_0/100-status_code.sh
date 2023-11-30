#!/bin/bash
# Bash script that sends a request to a URL passed as an argument
curl -os /dev/null -w "%{http_code}" "$1"
