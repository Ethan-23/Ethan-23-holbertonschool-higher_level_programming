#!/bin/bash
#comment
curl -sw "%{http_code}" "$1" -o /dev/null
