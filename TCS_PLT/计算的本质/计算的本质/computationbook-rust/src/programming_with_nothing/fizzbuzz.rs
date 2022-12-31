#[macro_use]
extern crate computationbook;

use computationbook::programming_with_nothing::pol::pol::{Pol, Rp};
use computationbook::programming_with_nothing::pol::helper::*;
use std::rc::Rc;
use std::vec::Vec;

fn main() {
    // ************************************
    // Non-Negative Number

    // number
    // |_p| {|x| { x } } or |p| { |x| { p(p(...p(x)...) } }
    let zero  = r!(|_p| r!(|x| x));
    let one   = r!(|p: Rp| r!(move |x| p.call(x)));
    let two   = r!(|p: Rp| r!(move |x| p.call(p.call(x))));
    let three = r!(|p: Rp| r!(move |x| p.call(p.call(p.call(x)))));
    let five  = r!(|p: Rp| r!(move |x| p.call(p.call(p.call(p.call(p.call(x)))))));
    let fifteen  = r!(|p: Rp| r!(move |x| p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(x)))))))))))))))));
    let hundred  = r!(|p: Rp| r!(move |x| p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(
                                        p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(p.call(x
    ))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))));

    println!("NUMBER 0:{} 1:{} 2:{} 3:{} 5:{} 15:{} 100:{}",
             to_integer(&zero), to_integer(&one), to_integer(&two),
             to_integer(&three), to_integer(&five), to_integer(&fifteen),
             to_integer(&hundred));

    // ************************************
    // Boolean

    // true
    // |x| { |y| { x }}
    let _true  = r!(move |x| r!(move |_y| x.clone()));
    // false
    // |x| { |y| { y }}
    let _false = r!(move |_x| r!(move |y| y.clone()));
    // if
    // |b| { b }
    let _if = r!(|b: Rp| b.clone());

    println!("BOOLEAN true:{} false:{}",
             to_boolean(&_true), to_boolean(&_false));
    println!("BOOLEAN (true)?1:0 :{}", to_integer(&_true.call(one.clone()).call(zero.clone())));

    // ************************************
    // Pair

    // pair
    // |x| { |y| { |f| { f(x)(y) }}}
    let pair = r!(move |x: Rp| {
        r!(move |y: Rp| {
            let x = x.clone();
            let y = y.clone();
            r!(move |f: Rp| { f.call(x.clone()).call(y.clone()) })
        })
    });

    // left
    // |p| { p(|x| { |y| { x }} ) }
    let left = {
        let _true  = _true.clone();
        r!(move |p: Rp| {
            p.call(_true.clone())
        })
    };
    // right
    // |p| { p(|x| { |y| { y }} ) }
    let right = {
        let _false  = _false.clone();
        r!(move |p: Rp| {
            p.call(_false.clone())
        })
    };

    let pairtest = pair.call(three.clone()).call(five.clone());
    println!("PAIR (3,5) left:{} three:{}",
             to_integer(&left.call(pairtest.clone())),
             to_integer(&right.call(pairtest.clone())));

    // ************************************
    // Numeric operation

    // increment
    // |n| { |p| { |x| { p(n(p)(x)) }  } }
    let incr = r!(|n: Rp| {
        r!(move |p: Rp| {
            let n = n.clone();
            let p = p.clone();
            r!(move |x: Rp| p.call(n.call(p.clone()).call(x)))
        })
    });

    // slide
    // |p| { pair(right(p))(incr(right(p))) }
    let slide = {
        let pair = pair.clone();
        let right = right.clone();
        let incr = incr.clone();
        r!(move |p: Rp| {
            pair.call(right.call(p.clone()))
                .call(incr.call(right.call(p.clone())))
        })
    };

    // decrement
    // |n| { left(n(slide)(pair(zero)(zero))) }
    let decr = {
        let left = left.clone();
        let slide = slide.clone();
        let pair = pair.clone();
        let zero = zero.clone();
        r!(move |n: Rp| {
            left.call(n.call(slide.clone())
                       .call(pair.call(zero.clone()).call(zero.clone())))
        })
    };

    // add
    // |m| { |n| { n(incr)(m) } }
    let add = {
        let incr = incr.clone();
        r!(move |m: Rp| {
            let incr = incr.clone();
            let m = m.clone();
            r!(move |n: Rp| {
                n.call(incr.clone()).call(m.clone())
            })
        })
    };

    // subtract
    // |m| { |n| { n(decr)(m) } }
    let subtract = {
        let decr = decr.clone();
        r!(move |m: Rp| {
            let decr = decr.clone();
            r!(move |n: Rp| {
                n.call(decr.clone()).call(m.clone())
            })
        })
    };

    // multiply
    // |m| { |n| { n(add(m))(zero) } }
    let multiply = {
        let add = add.clone();
        let zero = zero.clone();
        r!(move |m: Rp| {
            let add = add.clone();
            let zero = zero.clone();
            r!(move |n: Rp| {
                n.call(add.call(m.clone())).call(zero.clone())
            })
        })
    };

    // power
    // |m| { |n| { n(multiply(m))(one) } }
    let power = {
        let multiply = multiply.clone();
        let one = one.clone();
        r!(move |m: Rp| {
            let multiply = multiply.clone();
            let one = one.clone();
            r!(move |n: Rp| {
                n.call(multiply.call(m.clone()).call(one.clone()))
            })
        })
    };

    println!("DECREMENT decr(5):{} decr(0):{} decr(100):{}",
             to_integer(&decr.call(five.clone())),
             to_integer(&decr.call(zero.clone())),
             to_integer(&decr.call(hundred.clone())));

    println!("ARITHMETIC 3+5:{} 5-3:{} 3*5:{} 3**5:{}",
             to_integer(&add.call(three.clone()).call(five.clone())),
             to_integer(&subtract.call(five.clone()).call(three.clone())),
             to_integer(&multiply.call(three.clone()).call(five.clone())),
             to_integer(&power.call(three.clone()).call(five.clone())));

    // ************************************
    // Predicate

    // is_zero
    // |n| { n( |x| {FALSE})(TRUE) }
    let is_zero = {
        let _false = _false.clone();
        let _true  = _true.clone();
        let ret_false = r!(move |_x: Rp| _false.clone());
        r!(move |n: Rp| {
            n.call(ret_false.clone()).call(_true.clone())
        })
    };

    // is_le (less or equal)
    // |m| { |n| { is_zero(subtract(m)(n)) } }
    let is_le = {
        let is_zero = is_zero.clone();
        let subtract = subtract.clone();
        r!(move |m: Rp| {
            let is_zero = is_zero.clone();
            let subtract = subtract.clone();
            r!(move |n: Rp| {
                is_zero.call(subtract.call(m.clone()).call(n.clone()))
            })
        })
    };

    println!("IS_ZERO zero:{} three:{}",
             to_boolean(&is_zero.call(zero.clone())),
             to_boolean(&is_zero.call(three.clone())));
    println!("IS_LESS_OR_EQUAL 1<=2:{} 2<=2:{} 3<=2:{}",
             to_boolean(&is_le.call(one.clone()).call(two.clone())),
             to_boolean(&is_le.call(two.clone()).call(two.clone())),
             to_boolean(&is_le.call(three.clone()).call(two.clone())));

    // ************************************
    // Mod

    // Z combinator
    let z = {
        r!(move |f: Rp| {
            let fcopy = f.clone();
            r!(move |x: Rp| {
                let f = fcopy.clone();
                f.call(r!(move |y: Rp| {
                    x.call(x.clone()).call(y.clone())
                }))
            }).call(r!(move |x: Rp| {
                f.clone().call(r!(move |y: Rp| {
                    x.call(x.clone()).call(y.clone())
                }))
            }))
        })
    };
    // module
    // z ( |m| { |n| { if(is_le(n)(m))( |x| {f(subtract(m)(n))(n)(x)} )(m)} } )
    let module = {
        let _if = _if.clone();
        let is_le = is_le.clone();
        let subtract = subtract.clone();
        z.call(
            r!(move |f: Rp| {
                let _if = _if.clone();
                let is_le = is_le.clone();
                let subtract = subtract.clone();
                r!(move |m: Rp| {
                    let _if = _if.clone();
                    let is_le = is_le.clone();
                    let subtract = subtract.clone();
                    let f = f.clone();
                    r!(move |n: Rp| {
                        let subtract = subtract.clone();
                        let f = f.clone();
                        let mcopy = m.clone();
                        _if.call(is_le.call(n.clone()).call(m.clone()))
                           .call(r!(move |x: Rp| {
                               f.call(subtract.call(mcopy.clone()).call(n.clone()))
                                .call(n.clone())
                                .call(x.clone())
                           }))
                           .call(m.clone())
                    })
                })
            })
        )
    };

    println!("MOD 3%2:{} 5%3:{}",
             to_integer(&module.call(three.clone()).call(two.clone())),
             to_integer(&module.call(five.clone()).call(three.clone())));

    // ************************************
    // List

    // empty
    // pair(true)(true)
    let empty = pair.call(_true.clone()).call(_true.clone());

    // unshift
    // |l| { |x| { pair(false)(pair(x)(l)) } }
    let unshift = {
        let _false = _false.clone();
        let pair = pair.clone();
        r!(move |l: Rp| {
            let _false = _false.clone();
            let pair = pair.clone();
            r!(move |x: Rp| {
                pair.call(_false.clone()).call(pair.call(x).call(l.clone()))
            })
        })
    };

    // is_empty, left equivalent
    let is_empty = left.clone();

    // first
    // |l| { left(right(l)) }
    let first = {
        let left = left.clone();
        let right = right.clone();
        r!(move |l: Rp| {
            left.call(right.call(l.clone()))
        })
    };

    // rest
    // |l| { right(right(l)) }
    let rest = {
        let right = right.clone();
        r!(move |l: Rp| {
            right.call(right.clone().call(l.clone()))
        })
    };

    // to_array
    // since it require lot of closure, put it here
    let to_array = |p: &mut Rp| -> Vec<Rp> {
        let mut out: Vec<Rp> = vec![];
        while !to_boolean(&is_empty.call(p.clone())) {
            out.push(first.call(p.clone()));
            *p = rest.call(p.clone());
        }
        out
    };

    let testlist = unshift.call(unshift.call(unshift.call(empty.clone()).call(three.clone())).call(two.clone())).call(one.clone());
    println!("LIST [1, 2, 3]:[{}, {}, {}] list_is_empty:{}, empty_is_empty:{}",
             to_integer(&first.call(testlist.clone())),
             to_integer(&first.call(rest.call(testlist.clone()))),
             to_integer(&first.call(rest.call(rest.call(testlist.clone())))),
             to_boolean(&is_empty.call(testlist.clone())),
             to_boolean(&is_empty.call(empty.clone())));

    let array = to_array(&mut testlist.clone())
        .iter()
        .map(|x| to_integer(&x).to_string())
        .collect::<Vec<String>>();
    println!("LIST TO_ARRAY: [{}]", array.join(", "));

    // ************************************
    // Range

    // range
    // z ( |f| { |m| { |n| {
    //   if(is_le(m)(n))(|x| { unshift(f(incr(m))(n))(m)(x) })(empty)
    // } } } )
    let range = {
        let _if = _if.clone();
        let is_le = is_le.clone();
        let unshift = unshift.clone();
        let incr = incr.clone();
        let empty = empty.clone();
        z.call(
            r!(move |f: Rp| {
                let _if = _if.clone();
                let is_le = is_le.clone();
                let unshift = unshift.clone();
                let incr = incr.clone();
                let empty = empty.clone();
                r!(move |m: Rp| {
                    let _if = _if.clone();
                    let is_le = is_le.clone();
                    let unshift = unshift.clone();
                    let incr = incr.clone();
                    let empty = empty.clone();
                    let f = f.clone();
                    r!(move |n: Rp| {
                        let unshift = unshift.clone();
                        let incr = incr.clone();
                        let mcopy = m.clone();
                        let f = f.clone();
                        let empty = empty.clone();
                        _if.call(is_le.call(m.clone()).call(n.clone()))
                           .call(r!(move |x: Rp| {
                               unshift
                                   .call(f.call(incr.call(mcopy.clone()))
                                          .call(n.clone()))
                                   .call(mcopy.clone())
                                   .call(x.clone())
                           }))
                           .call(empty)
                    })
                })
            })
        )
    };

    let one_to_five = range.call(one.clone()).call(five.clone());
    let array = to_array(&mut one_to_five.clone())
        .iter()
        .map(|x| to_integer(&x).to_string())
        .collect::<Vec<String>>();
    println!("RANGE(1-5): [{}]", array.join(", "));

    // fold
    // z ( |f| { |l| { |x| { |g| {
    //   if(is_empty(l))(x)( |y| { g(f(rest(l))(x)(g))(first(l))(y) } )
    // } } } } )
    let fold = {
        let _if = _if.clone();
        let is_empty = is_empty.clone();
        let rest = rest.clone();
        let first = first.clone();
        z.call(
            r!(move |f: Rp| {
                let _if = _if.clone();
                let is_empty = is_empty.clone();
                let rest = rest.clone();
                let first = first.clone();
                r!(move |l: Rp| {
                    let _if = _if.clone();
                    let is_empty = is_empty.clone();
                    let rest = rest.clone();
                    let first = first.clone();
                    let f = f.clone();
                    r!(move |x: Rp| {
                        let _if = _if.clone();
                        let is_empty = is_empty.clone();
                        let first = first.clone();
                        let rest = rest.clone();
                        let f = f.clone();
                        let l = l.clone();
                        r!(move |g: Rp| {
                            let first = first.clone();
                            let rest = rest.clone();
                            let f = f.clone();
                            let l = l.clone();
                            let x = x.clone();
                            _if.call(is_empty.call(l.clone()))
                               .call(x.clone())
                               .call(r!(move |y| {
                                   g.call(f.call(rest.call(l.clone()))
                                           .call(x.clone())
                                           .call(g.clone()))
                                    .call(first.call(l.clone()))
                                    .call(y)
                               }))
                        })
                    })
                })
            })
        )
    };

    println!("FOLD [1-5] with ADD base 0: {}",
             to_integer(&fold
                .call(one_to_five.clone())
                .call(zero.clone())
                .call(add.clone())));

    // map
    // |k| { |f| { fold(k)(empty)( |l| { |x| { unshift(l)(f(x)) }  } )
    // } }
    let map = {
        let fold = fold.clone();
        let unshift = unshift.clone();
        let empty = empty.clone();
        r!(move |k: Rp| {
            let fold = fold.clone();
            let unshift = unshift.clone();
            let empty = empty.clone();
            r!(move |f: Rp| {
                let unshift = unshift.clone();
                fold.call(k.clone())
                    .call(empty.clone())
                    .call(r!(move |l: Rp| {
                        let unshift = unshift.clone();
                        let f = f.clone();
                        r!(move |x: Rp| {
                            unshift.call(l.clone()).call(f.call(x))
                        })
                    }))
            })
        })
    };

    let two_to_six = map.call(one_to_five.clone()).call(incr.clone());
    let array = to_array(&mut two_to_six.clone())
        .iter()
        .map(|x| to_integer(&x).to_string())
        .collect::<Vec<String>>();
    println!("map(incr, [1-5]): [{}]", array.join(", "));

    let ten   = multiply.call(five.clone()).call(two.clone());
    let charb = ten.clone();
    let charf = incr.call(charb.clone());
    let chari = incr.call(charf.clone());
    let charu = incr.call(chari.clone());
    let charz = incr.call(charu.clone());
    let zz = unshift.call(unshift.call(
            empty.clone()).call(charz.clone())).call(charz.clone());
    let fizz = unshift.call(unshift.call(
            zz.clone()).call(chari.clone())).call(charf.clone());
    let buzz = unshift.call(unshift.call(
            zz.clone()).call(charu.clone())).call(charb.clone());
    let fizzbuzz = unshift.call(unshift.call(unshift.call(unshift.call(
                    buzz.clone()).call(charz.clone())).call(charz.clone())).call(chari.clone())).call(charf.clone());

    // helper to_string
    let to_string = |l: &Rp| -> String {
        let out = to_array(&mut l.clone()).iter().map(|x| to_char(&x)).collect::<String>();
        out
    };

    println!("Fizz:{}, Buzz:{}, FizzBuzz:{}",
             to_string(&fizz.clone()),
             to_string(&buzz.clone()),
             to_string(&fizzbuzz.clone()));

    // div
    // z ( |f| { |m| { |n| {
    //   if(is_le(n)(m))( |x| {incr(f(subtract(m)(n))(n))(x)} )(zero)
    // } } } )
    let div = {
        let _if = _if.clone();
        let is_le = is_le.clone();
        let incr = incr.clone();
        let subtract = subtract.clone();
        let zero = zero.clone();
        z.call(
            r!(move |f: Rp| {
                let _if = _if.clone();
                let is_le = is_le.clone();
                let incr = incr.clone();
                let subtract = subtract.clone();
                let zero = zero.clone();
                r!(move |m: Rp| {
                    let _if = _if.clone();
                    let is_le = is_le.clone();
                    let incr = incr.clone();
                    let subtract = subtract.clone();
                    let zero = zero.clone();
                    let f = f.clone();
                    r!(move |n: Rp| {
                        let incr = incr.clone();
                        let subtract = subtract.clone();
                        let f = f.clone();
                        let m = m.clone();
                        _if.call(is_le.call(n.clone()).call(m.clone()))
                           .call(r!(move |x: Rp| {
                               incr.call(f.call(subtract
                                                .call(m.clone())
                                                .call(n.clone()))
                                          .call(n.clone()))
                                   .call(x.clone())
                           }))
                           .call(zero.clone())
                    })
                })
            })
        )
    };

    // push
    // |l| { |x| { fold(l)(unshift(empty)(x))(unshift) } }
    let push = {
        let empty = empty.clone();
        let unshift = unshift.clone();
        let fold = fold.clone();
        r!(move |l: Rp| {
            let empty = empty.clone();
            let unshift = unshift.clone();
            let fold = fold.clone();
            r!(move |x: Rp| {
                let empty = empty.clone();
                fold.call(l.clone())
                    .call(unshift.call(empty).call(x))
                    .call(unshift.clone())
            })
        })
    };

    // to_digits
    // z ( |f| { |n| {
    //   push(
    //      if(is_le(n)(decr(ten)))(empty)( |x| { f(div(n)(ten))(x) } )
    //   )(
    //      mod(n)(ten)
    //   )
    // } } )
    let to_digits = {
        let _if = _if.clone();
        let is_le = is_le.clone();
        let decr = decr.clone();
        let empty = empty.clone();
        let ten = ten.clone();
        let push = push.clone();
        let div = div.clone();
        let module = module.clone();
        z.call(
            r!(move |f: Rp| {
                let _if = _if.clone();
                let is_le = is_le.clone();
                let decr = decr.clone();
                let empty = empty.clone();
                let ten = ten.clone();
                let push = push.clone();
                let div = div.clone();
                let module = module.clone();
                r!(move |n: Rp| {
                    let f = f.clone();
                    let div = div.clone();
                    let tencopy = ten.clone();
                    let ncopy = n.clone();
                    push.call(
                        _if.call(is_le.call(n.clone()).call(decr.call(ten.clone())))
                           .call(empty.clone())
                           .call(r!(move |x: Rp| {
                               f.call(div.call(ncopy.clone()).call(tencopy.clone())).call(x.clone())
                           }))
                    ).call(
                        module.call(n.clone()).call(ten.clone())
                    )
                })
            })
        )
    };

    let array = to_array(&mut to_digits.call(five.clone()))
        .iter()
        .map(|x| to_integer(&x).to_string())
        .collect::<Vec<String>>();
    println!("digits 5:[{}]", array.join(", "));

    let array = to_array(&mut to_digits.call(power.call(five.clone()).call(two.clone())))
        .iter()
        .map(|x| to_integer(&x).to_string())
        .collect::<Vec<String>>();
    println!("digits 5:[{}]", array.join(", "));

    // finally fizzbuzz
    let solution = {
        map.call(range.call(one.clone()).call(hundred.clone()))
           .call(r!(move |n:Rp| {
               _if.call(is_zero.call(module.call(n.clone()).call(fifteen.clone())))
                  .call(fizzbuzz.clone())
                  .call(
                      _if.call(is_zero.call(module.call(n.clone()).call(three.clone())))
                         .call(fizz.clone())
                         .call(
                             _if.call(is_zero.call(module.call(n.clone()).call(five.clone())))
                                .call(buzz.clone())
                                .call(to_digits.call(n.clone()))
                         )
                  )
           }))
    };

    let array = to_array(&mut solution.clone())
        .iter()
        .map(|x| to_string(x))
        .collect::<Vec<String>>();
    println!("fizzbuzz :[{}]", array.join(", "));
}
