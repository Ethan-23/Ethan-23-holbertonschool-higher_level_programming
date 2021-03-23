#!/usr/bin/node
if (process.argv[2]) {
for (let j = 0; j < parseInt(process.argv[2]); j++) {
  console.log('C is fun');
}
} else {
  console.log('Missing number of occurrences');
}
