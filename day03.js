const getLines = require('./file');
const DATA_FILE = __dirname + '/data/day3.txt';

function findTrees(lines, xIncrements, yIncrements) {
  let x = 0;
  let trees = 0;
  lines.forEach((line, index) => {
    if (index % yIncrements !== 0) {
      return;
    }
    if (line.charAt(x) === '#') {
      trees++;
    }
    x += xIncrements;
    x = x % line.length;
  })
  return trees;
}

getLines(DATA_FILE).then((lines) => {
  const trees = findTrees(lines, 3, 1);

  console.log('trees: ', trees);

  const traverses = [
    findTrees(lines, 1, 1),
    findTrees(lines, 3, 1),
    findTrees(lines, 5, 1),
    findTrees(lines, 7, 1),
    findTrees(lines, 1, 2),
  ]

  console.log('multiplied trees: ', traverses.reduce((acc, curr) => acc * curr, 1));
})
