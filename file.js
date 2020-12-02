const { readFile } = require('fs').promises

const getLines =  (filename) =>
  readFile(filename, { encoding: 'utf8' })
    .then((contents) => contents.toString().trim().split('\n'));

module.exports = getLines;
