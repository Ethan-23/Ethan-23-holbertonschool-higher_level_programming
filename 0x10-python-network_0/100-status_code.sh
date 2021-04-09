#!/bin/bash
#comment
curl -sw "%{http_code}\n" "$1" -o /dev/null
