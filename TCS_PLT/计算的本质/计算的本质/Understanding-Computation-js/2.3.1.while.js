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

var DoNothing = function () {};

DoNothing.prototype.toString = function () {
  return "do-nothing";
};

DoNothing.prototype.reducible = function () {
  return false;
};

var Assign = function (name, expression) {
  this.name = name;
  this.expression = expression;
};

util.inherits(Assign, Expression);

Assign.prototype.reduce = function (environment) {
  if (this.expression.reducible()) {
    var exp = this.expression.reduce(environment);
    return [new Assign(this.name, exp), environment];
  } else {
    environment[this.name] = this.expression;
    return [new DoNothing(),  environment]; 
  }
};

Assign.prototype.toString = function () {
  return "" + this.name + " = " + this.expression;
};

var If = function (condition, consequence, alternative) {
  this.condition = condition;
  this.consequence = consequence;
  this.alternative = alternative;
};
util.inherits(If, Expression);

If.prototype.toString = function () {
  return "if (" + this.condition + ") { " + this.consequence + " } else { " + this.alternative + " }";
};

If.prototype.reduce = function (environment) {
  if (this.condition.reducible()) {
    return [new If(this.condition.reduce(environment), this.consequence, this.alternative), environment];
  } else {
    if (this.condition.value) {
      return [this.consequence, environment];
    } else {
      return [this.alternative, environment];
    }
  }
};

var Sequence = function (first, second) {
  this.first = first;
  this.second = second;
};
util.inherits(Sequence, Expression);

Sequence.prototype.toString = function () {
  return "" + this.first + "; " + this.second;
};

Sequence.prototype.reduce = function (environment) {
  if (this.first instanceof DoNothing) {
    return [this.second, environment];
  } else {
    var result = this.first.reduce(environment);
    var first = result[0];
    var env = result[1];
    return [new Sequence(first, this.second), env];
  }
};

var While = function (condition, body) {
  this.condition = condition;
  this.body = body;
};
util.inherits(While, Expression);

While.prototype.toString = function () {
  return "while (" + this.condition + ") { " + this.body + " }";
};

While.prototype.reduce = function (environment) {
  return [new If(this.condition, new Sequence(this.body, this), new DoNothing()), environment];
};

var Machine = function (statement, environment) {
  this.statement = statement;
  this.environment = environment;
};

Machine.prototype.step = function () {
  var result = this.statement.reduce(this.environment);
  this.statement = result[0];
  this.environment = result[1];
};

Machine.prototype.run = function () {
  while (this.statement.reducible()) {
    console.log(this.statement.toString(), this.environment);
    this.step();
  }

  console.log(this.statement.toString(), this.environment);
};

new Machine(
  new While(
    new LessThan(new Variable("x"), new TNumber(5)),
    new Assign("x", new Multiply(new Variable("x"), new TNumber(3)))
  ),
  {x: new TNumber(1)}
).run();
