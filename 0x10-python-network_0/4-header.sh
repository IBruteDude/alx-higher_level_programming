#!/bin/bash
# send a get request with a custom header
curl -s -H 'X-School-User-Id: 98' "$1"
