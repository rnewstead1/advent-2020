const getLines = require('./file');
const DATA_FILE = __dirname + '/data/day4.txt';

function betweenInclusive(val, min, max) {
  const asInt = parseInt(val, 10);
  return asInt && asInt >= min && asInt <= max;
}

function numOfChars(val, num) {
  return val.length === num;
}

const heightValidations = {
  cm: (val) => betweenInclusive(val, 150, 193),
  in: (val) => betweenInclusive(val, 59, 76),
}

const fieldValidations = {
  byr: (val) => numOfChars(val, 4) && betweenInclusive(val, 1920, 2002),
  iyr: (val) => numOfChars(val, 4) && betweenInclusive(val, 2010, 2020),
  eyr: (val) => numOfChars(val, 4) && betweenInclusive(val, 2020, 2030),
  hgt: (val) => {
    const matches = val && val.match(/(?<num>[0-9]+)(?<unit>cm|in)/);
    return matches && heightValidations[matches.groups.unit](matches.groups.num);
  },
  hcl: (val) => val.match(/#[a-f|0-9]{6}/),
  ecl: (val) => val.match(/amb|blu|brn|gry|grn|hzl|oth/),
  pid: (val) => val.match(/^[0-9]{9}$/),
};

function passesFieldValidation(fields) {
  return (fieldKey) => fields.hasOwnProperty(fieldKey) && fieldValidations[fieldKey](fields[fieldKey]);
}

function containsRequiredField(fields) {
  return (fieldKey) => fields.hasOwnProperty(fieldKey);
}

function getAllPassports(lines) {
  const passports = [];

  function group(lines, startIndex) {
    const blankLineIndex = lines.indexOf('', startIndex);
    const endIndex = blankLineIndex >= 0 ? blankLineIndex : lines.length;
    passports.push(lines.slice(startIndex, endIndex));
    return endIndex + 1;
  }

  let i = 0;
  while (i < lines.length) {
    i = group(lines, i);
  }
  return passports;
}

function getValidPassports(allPassports, isValidFn) {
  const validPassports = [];
  allPassports.forEach((passport) => {
    const passportFields = passport.reduce((fields, line) => {
      line.split(' ').map(fieldValPair => fieldValPair.split(':')).forEach(([field, value]) => {
        fields[field] = value;
      })
      return fields;
    }, {});

    if (Object.keys(fieldValidations).every(isValidFn(passportFields))) {
      validPassports.push(passport);
    }
  });
  return validPassports;
}

getLines(DATA_FILE).then((lines) => {
  const passports = getAllPassports(lines);

  const passportsContainingAllRequiredFields = getValidPassports(passports, containsRequiredField);
  console.log('Number of passports containing all required fields: ', passportsContainingAllRequiredFields.length);

  const passportsPassingAllValidations = getValidPassports(passports, passesFieldValidation);
  console.log('Number of passports passing all validations: ', passportsPassingAllValidations.length);
});
