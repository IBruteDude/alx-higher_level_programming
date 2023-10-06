#!/bin/bash
# print the size of the response body
curl -s -w '%{size_download}' -o /dev/null "$1" ; echo ''
