# LambdaLisp

https://woodrush.github.io/blog/lambdalisp.html
https://github.com/woodrush/lambdalisp/pulls

LambdaLisp is a Lisp interpreter written as an untyped lambda calculus term. The input and output text is encoded into closed lambda terms using the [Mogensen-Scott encoding](https://en.wikipedia.org/wiki/Mogensen%E2%80%93Scott_encoding), so the entire computation process solely consists of the beta-reduction of lambda calculus terms.

When run on a lambda calculus interpreter that runs on the terminal, it presents a REPL where you can interactively define and evaluate Lisp expressions. Supported interpreters are:

- The [521-byte lambda calculus interpreter](https://justine.lol/lambda/) SectorLambda written by Justine Tunney
- The [IOCCC](https://www.ioccc.org/) 2012 [“Most functional”](https://www.ioccc.org/2012/tromp/hint.html) interpreter written by John Tromp (the [source](https://www.ioccc.org/2012/tromp/tromp.c) is in the shape of a λ)
- Universal Lambda interpreter [clamb](https://github.com/irori/clamb) and Lazy K interpreter [lazyk](https://github.com/irori/lazyk) written by Kunihiko Sakamoto