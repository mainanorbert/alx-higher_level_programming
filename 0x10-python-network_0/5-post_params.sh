#!/bin/bash
# email set to test@gmail.com
# subject set to 'I will always be here for PLD'
curl -sX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
