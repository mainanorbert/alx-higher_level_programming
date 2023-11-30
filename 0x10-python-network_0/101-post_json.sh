#!/bin/bash
# Sending a json post request using curl
curl -s -H "content-Type: application/json" -d "$(cat "$2")" "$1"
