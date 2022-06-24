// 阶乘，version1
function fac(num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * fac(num - 1);
  }
}

var trueFac = fac;
fac = function() {
  return 0;
}

console.log(trueFac(5));
console.log(fac(5));
