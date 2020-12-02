const getLines = require('./file');
const DATA_FILE = __dirname + '/data/day1.txt';

function equals2020() {
  return [...arguments].reduce((acc, curr) => acc + parseInt(curr, 10), 0) === 2020;
}

function multiply() {
  return [...arguments].reduce((acc, curr) => acc * parseInt(curr, 10), 1);
}

const findTwo = (numbers) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let i2 = i; i2 < numbers.length; i2++) {
      if (equals2020(numbers[i], numbers[i2])) {
        return multiply(numbers[i], numbers[i2]);
      }
    }
  }
}

const findThree = (numbers) => {
  for (let i = 0; i < numbers.length; i++) {
    for (let i2 = i; i2 < numbers.length; i2++) {
      for (let i3 = i2; i3 < numbers.length; i3++) {
        if (equals2020(numbers[i], numbers[i2], numbers[i3])) {
          return multiply(numbers[i], numbers[i2], numbers[i3]);
        }
      }
    }
  }
}

getLines(DATA_FILE).then((expenseReport) => {
  const expenses = expenseReport.map((expense) => parseInt(expense, 10));

  console.log('First answer: ', findTwo(expenses));
  console.log('Second answer: ', findThree(expenses));
});



