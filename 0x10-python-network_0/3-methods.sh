#!/bin/bash
# dislaying http methods a server accepts
curl -sI "$1" | grep Allow | cut -d " " -f 2-
