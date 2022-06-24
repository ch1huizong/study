var constantize = (obj) => {
  Object.freeze(obj);
  Object.keys(obj).forEach((key, i) => {
    if (typeof obj[key] === 'object') {
    constantize(obj[key]);
    //arguments.callee(obj[key]); // ?
    }
  });
};

var person = {
  name: 'che',
  age: 30,
  school: ['YanShan', 'HeBei']
}

constantize(person);
person.school = 'cc';
console.log(person.school);
