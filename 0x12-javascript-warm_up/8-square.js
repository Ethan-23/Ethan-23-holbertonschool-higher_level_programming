#!/usr/bin/node
if (process.argv[2]) {
for (let j = 0; j < parseInt(process.argv[2]); j++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
}
} else {
  console.log('Missing size');
}
