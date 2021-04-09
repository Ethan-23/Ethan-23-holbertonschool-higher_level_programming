#!/bin/bash
#comment
curl -o /dev/null -sw "%{http_code}\n" "$1"
