#!/bin/bash
# display the available methods
curl -sI OPTIONS "$1" | grep 'Allow: ' | cut -b 8-
