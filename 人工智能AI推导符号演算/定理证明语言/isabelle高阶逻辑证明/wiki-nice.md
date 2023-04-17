
# wiki-nice
zh.wikipedia.org/wiki/Isabelle

Isabelle 支持两种不同风格的的证明书写方式：[过程式](https://zh.wikipedia.org/wiki/%E8%BF%87%E7%A8%8B%E5%BC%8F%E7%BC%96%E7%A8%8B "过程式编程")和[声明式](https://zh.wikipedia.org/wiki/%E5%AE%A3%E5%91%8A%E5%BC%8F%E7%B7%A8%E7%A8%8B "宣告式编程")。 过程式风格的证明主要由一系列证明策略（tactics）或过程的依次运用组成；它能够较好地反映数学家思考证明的过程，但通常较难阅读，因为它无法直接体现每步推演的结果。 声明式风格的证明（由 Isabelle 内置的证明语言 Isar 支持）则与之相反，它以直接的方式描述了每一步确切的数学推演，因此较容易被阅读和人工检查。

在较新版本的 Isabelle 中，过程式风格的证明已不建议再使用。形式化证明存档（Archive of Formal Proofs）亦推荐使用声明式风格来书写证明。


```
theorem sqrt2_not_rational:
  "sqrt (real 2) ∉ ℚ"
proof
  let ?x = "sqrt (real 2)"
  assume "?x ∈ ℚ"
  then obtain m n :: nat where
    sqrt_rat: "¦?x¦ = real m / real n" and lowest_terms: "coprime m n"
    by (rule Rats_abs_nat_div_natE)
  hence "real (m^2) = ?x^2 * real (n^2)" by (auto simp add: power2_eq_square)
  hence eq: "m^2 = 2 * n^2" using of_nat_eq_iff power2_eq_square by fastforce
  hence "2 dvd m^2" by simp
  hence "2 dvd m" by simp
  have "2 dvd n" proof -
    from ‹2 dvd m› obtain k where "m = 2 * k" ..
    with eq have "2 * n^2 = 2^2 * k^2" by simp
    hence "2 dvd n^2" by simp
    thus "2 dvd n" by simp
  qed
  with ‹2 dvd m› have "2 dvd gcd m n" by (rule gcd_greatest)
  with lowest_terms have "2 dvd 1" by simp
  thus False using odd_one by blast
qed
```



































































