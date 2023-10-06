#!/bin/bash
# send a json file over the
curl -s -d @"$2" "$1" ; echo ''