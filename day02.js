const getLines = require('./file');
const DATA_FILE = __dirname + '/data/day2.txt';

const LINE_PATTERN = /(?<first>^[0-9]+)-(?<second>[0-9]+) (?<letter>[a-z]+): (?<password>[a-z]+$)/

function extractValues(line) {
  return line.match(LINE_PATTERN).groups;
}

function isValidByCount({ first: lowest, second: highest, letter, password }) {
  const letterPattern = new RegExp(letter,'g');
  const lettersInPassword = password.match(letterPattern) || [];

  return lettersInPassword.length >= lowest && lettersInPassword.length <= highest;
}

function isValidByPosition({ first, second, letter, password }) {
  const charAtFirst = password.charAt(first - 1);
  const charAtSecond = password.charAt(second - 1);

  return charAtFirst === letter ? charAtSecond !== letter : charAtSecond === letter;
}

getLines(DATA_FILE).then((lines) => {
  const validByCount = lines.filter((line) => isValidByCount(extractValues(line)));
  console.log('Number of passwords valid by count: ', validByCount.length);

  const validByPosition = lines.filter((line) => isValidByPosition(extractValues(line)));
  console.log('Number of passwords valid by position: ', validByPosition.length);
})
