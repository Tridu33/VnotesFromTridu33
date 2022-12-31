// 《计算的本质》2.3.1章，小步语义的演算过程。
// 为了避免与JS中已有类型Number，Boolean的冲突，加T为前缀。

var util = require('util');

var Type = function (value) {
  this.value = value;
};

Type.prototype.toString = function () {
  return "" + this.value + "";
};

Type.prototype.reducible = function () {
  return false;
};

var TNumber = function (value) {
  Type.call(this, value);
};
util.inherits(TNumber, Type);

var TBoolean = function (value) {
  Type.call(this, value);
};
util.inherits(TBoolean, Type);

var Expression = function (left, right) {
  this.left = left;
  this.right = right;
};

Expression.prototype.reducible = function () {
  return true;
};

var Add = function (left, right) {
  Expression.call(this, left, right);
};
util.inherits(Add, Expression);

Add.prototype.reduce = function (environment) {
  if (this.left.reducible()) {
    return new Add(this.left.reduce(environment), this.right);
  } else if (this.right.reducible()) {
    return new Add(this.left, this.right.reduce(environment));
  } else {
    return new TNumber(this.left.value + this.right.value);
  }
};

Add.prototype.toString = function () {
  return "" + this.left + " + " + this.right + "";
};

var Multiply = function (left, right) {
  Expression.call(this, left, right);
};
util.inherits(Multiply, Expression);

Multiply.prototype.reduce = function (environment) {
  if (this.left.reducible()) {
    return new Multiply(this.left.reduce(environment), this.right);
  } else if (this.right.reducible(environment)) {
    return new Multiply(this.left, this.right.reduce());
  } else {
    return new TNumber(this.left.value * this.right.value);
  }
};

Multiply.prototype.toString = function () {
  return "" + this.left + " * " + this.right + "";
};

var LessThan = function (left, right) {
  Expression.call(this, left, right);
};
util.inherits(LessThan, Expression);

LessThan.prototype.reduce = function (environment) {
  if (this.left.reducible()) {
    return new LessThan(this.left.reduce(environment), this.right);
  } else if (this.right.reducible()) {
    return new LessThan(this.left, this.right.reduce(environment));
  } else {
    return new TBoolean(this.left.value < this.right.value);
  }
};

LessThan.prototype.toString = function () {
  return "" + this.left + " < " + this.right + "";
};

var Variable = function (name) {
  this.name = name;
};

util.inherits(Variable, Expression);

Variable.prototype.reduce = function (environment) {
  return environment[this.name];
};

Variable.prototype.toString = function () {
  return "" + this.name + "";
};

var Machine = function (expression, environment) {
  this.expression = expression;
  this.environment = environment;
};

Machine.prototype.step = function () {
  this.expression = this.expression.reduce(this.environment);
};

Machine.prototype.run = function () {
  while (this.expression.reducible()) {
    console.log(this.expression.toString());
    this.step();
  }

  console.log(this.expression.toString());
};

new Machine(
  new Add(new Variable("x"), new Variable("y")),
  {
    "x": new TNumber(3),
    "y": new TNumber(4)
  }
).run();
