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

Add.prototype.reduce = function () {
  if (this.left.reducible()) {
    return new Add(this.left.reduce(), this.right);
  } else if (this.right.reducible()) {
    return new Add(this.left, this.right.reduce());
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

Multiply.prototype.reduce = function () {
  if (this.left.reducible()) {
    return new Multiply(this.left.reduce(), this.right);
  } else if (this.right.reducible()) {
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

LessThan.prototype.reduce = function () {
  if (this.left.reducible()) {
    return new LessThan(this.left.reduce(), this.right);
  } else if (this.right.reducible()) {
    return new LessThan(this.left, this.right.reduce());
  } else {
    return new TBoolean(this.left.value < this.right.value);
  }
};

LessThan.prototype.toString = function () {
  return "" + this.left + " < " + this.right + "";
};

var Machine = function (expression) {
  this.expression = expression;
};

Machine.prototype.step = function () {
  this.expression = this.expression.reduce();
};

Machine.prototype.run = function () {
  while (this.expression.reducible()) {
    console.log(this.expression.toString());
    this.step();
  }

  console.log(this.expression.toString());
};

new Machine(
  new Add(
    new Multiply(new TNumber(1), new TNumber(2)),
    new Multiply(new TNumber(3), new TNumber(4))
  )
).run();

new Machine(
  new LessThan(new TNumber(5), new Add(new TNumber(2), new TNumber(2)))
).run();
