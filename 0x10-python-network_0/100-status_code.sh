#/bin/bash
#comment
curl -o /dev/null --silent --head "%{http_code}\n" "$1"
