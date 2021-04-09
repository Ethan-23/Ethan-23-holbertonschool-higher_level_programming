#!/bin/bash
#comment
curl "$1" -sw '%{size_download}\n' -o /dev/null
