#!/bin/bash
# send a post request with specified parameters
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
