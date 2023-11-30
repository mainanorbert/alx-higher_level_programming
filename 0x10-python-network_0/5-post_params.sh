#!/bin/bash
# email set to test@gmail.com subject set to'
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
