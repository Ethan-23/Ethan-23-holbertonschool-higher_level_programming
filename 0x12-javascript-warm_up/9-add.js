#!/usr/bin/node
if (process.argv[2] && process.argv[3]) {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
} else {
  console.log('NaN');
}
