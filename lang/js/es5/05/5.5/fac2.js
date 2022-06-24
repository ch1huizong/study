// 阶乘，version2
function fac(num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * arguments.callee(num - 1); // 调用函数自身
  }
}

var trueFac = fac;
fac = function() {
  return 0;
}

console.log(trueFac(5));
console.log(fac(5));
