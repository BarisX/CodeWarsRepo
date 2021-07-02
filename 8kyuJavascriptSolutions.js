// https://www.codewars.com/kata/515e271a311df0350d00000f
function squareSum(numbers){
  return numbers.map(x => x ** 2).reduce((a,b) => a + b ,0);
}

// https://www.codewars.com/kata/596c6eb85b0f515834000049
var replaceDots = function(str) {
  return str.replace(/\./g, '-');
}

