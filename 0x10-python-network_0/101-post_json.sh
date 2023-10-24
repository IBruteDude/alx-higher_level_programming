#!/bin/bash
# send a json file over the
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1" ; echo ''
