# lean文档















[社区文档](https://leanprover-community.github.io/)


https://leanprover.github.io/programming_in_lean/#01_Introduction.html  写着代码学lean

[run lean online](https://leanprover-community.github.io/lean-web-editor/#code=import%20data.nat.prime%0Aopen%20nat%0A%0Atheorem%20sqrt_two_irrational%20%7Ba%20b%20%3A%20ℕ%7D%20(co%20%3A%20gcd%20a%20b%20%3D%201)%20%3A%0A%20%20a%5E2%20≠%202%20*%20b%5E2%20%3A%3D%0Aassume%20h%20%3A%20a%5E2%20%3D%202%20*%20b%5E2%2C%0Ahave%202%20∣%20a%5E2%2C%0A%20%20by%20simp%20%5Bh%5D%2C%0Ahave%202%20∣%20a%2C%0A%20%20from%20prime.dvd_of_dvd_pow%20prime_two%20this%2C%0Aexists.elim%20this%20%24%0Aassume%20(c%20%3A%20nat)%20(aeq%20%3A%20a%20%3D%202%20*%20c)%2C%0Ahave%202%20*%20(2%20*%20c%5E2)%20%3D%202%20*%20b%5E2%2C%0A%20%20by%20simp%20%5Beq.symm%20h%2C%20aeq%5D%3B%0A%20%20%20%20simp%20%5Bnat.pow_succ%2C%20mul_comm%2C%20mul_assoc%2C%20mul_left_comm%5D%2C%0Ahave%202%20*%20c%5E2%20%3D%20b%5E2%2C%0A%20%20from%20eq_of_mul_eq_mul_left%20dec_trivial%20this%2C%0Ahave%202%20∣%20b%5E2%2C%0A%20%20by%20simp%20%5Beq.symm%20this%5D%2C%0Ahave%202%20∣%20b%2C%0A%20%20from%20prime.dvd_of_dvd_pow%20prime_two%20this%2C%0Ahave%202%20∣%20gcd%20a%20b%2C%0A%20%20from%20dvd_gcd%20‹2%20∣%20a›%20‹2%20∣%20b›%2C%0Ahave%202%20∣%20(1%20%3A%20ℕ)%2C%0A%20%20by%20simp%20*%20at%20*%2C%0Ashow%20false%2C%20from%20absurd%20‹2%20∣%201›%20dec_trivial)



https://leanprover.github.io/logic_and_proof/introduction.html


```
pip install mathlibtools
```
https://leanprover-community.github.io/leanproject.html

* Intro Categories*
http://ncatlab.org/nlab/show/geometry+of+physics+--+categories+and+toposes

*Intro Topology* 
http://ncatlab.org/nlab/show/Introduction+to+Topology

*Intro Homotopy*
http://ncatlab.org/nlab/show/Introduction+to+Homotopy+Theory

*Intro Stable Homotopy*
http://ncatlab.org/nlab/show/Introduction+to+Stable+Homotopy+Theory

* Intro Cobordism*
http://ncatlab.org/nlab/show/Introduction+to+Cobordism+and+Complex+Oriented+Cohomology

*Intro QFT*
http://ncatlab.org/nlab/show/geometry+of+physics+--+perturbative+quantum+field+theory













