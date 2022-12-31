pub mod iota;
pub mod to_iota;

#[cfg(test)]
mod tests {
    use programming_with_nothing::lambda::lambda::{Lambda};
    use universality_is_everywhere::ski_calculus::ski::{SKI};
    use universality_is_everywhere::ski_calculus::lambda_to_ski::{ToSKI};
    use super::to_iota::{to_iota};

    #[test]
    fn test_iota_s() {
        let mut expr = to_iota(&SKI::s());
        println!("{}", expr);
        while expr.reducible() {
            println!("{}", expr);
            expr = expr.reduce()
        }
        println!("{}", expr);
        assert_eq!("S", format!("{}", expr));
    }

    #[test]
    fn test_iota_k() {
        let mut expr = to_iota(&SKI::k());
        println!("{}", expr);
        while expr.reducible() {
            println!("{}", expr);
            expr = expr.reduce()
        }
        println!("{}", expr);
        assert_eq!("K", format!("{}", expr));
    }

    #[test]
    fn test_iota_i() {
        let mut expr = to_iota(&SKI::i());
        println!("{}", expr);
        while expr.reducible() {
            println!("{}", expr);
            expr = expr.reduce()
        }
        println!("{}", expr);
        assert_eq!("S[K][K[K]]", format!("{}", expr));
    }

    #[test]
    fn test_iota_verify_i() {
        let identity = SKI::skicall(SKI::skicall(SKI::s(), SKI::k()), SKI::skicall(SKI::k(), SKI::k()));
        let mut expr = SKI::skicall(identity, SKI::skisymbol("x"));
        while expr.reducible() {
            println!("{}", expr);
            expr = expr.reduce()
        }
        println!("{}", expr);
        assert_eq!("x", format!("{}", expr));
    }

    #[test]
    fn test_iota_two() {
        let two = Lambda::lcfun("p", Lambda::lcfun("x", Lambda::lccall(Lambda::lcvar("p"), Lambda::lccall(Lambda::lcvar("p"), Lambda::lcvar("x")))));
        let mut expr = to_iota(&two.to_ski());
        expr = SKI::skicall(SKI::skicall(expr, SKI::skisymbol("inc")), SKI::skisymbol("zero"));
        while expr.reducible() {
            println!("{}", expr);
            expr = expr.reduce()
        }
        println!("{}", expr);
        assert_eq!("inc[inc[zero]]", format!("{}", expr));
    }
}
