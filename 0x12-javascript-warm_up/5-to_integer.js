#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parseInt(process.argv[2]));
}