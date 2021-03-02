

# Learn QNP formal definition from examples plans for Automated Planning

As we all know, a Qualitative numeric Planning Problem is similar to a generalized plan where the numbers of objects may be unknown and unbounded during planning. There are two knowledge acquisition problems in Automated Planning: a)Learning planning action models automatically, define this problem with formal language;b)make a solver this problem(the method Top-Down or Bottom-Up).

What we interesting in here is the first step. How can we learn planning action models automatically? Equivalently, learning the abstract structure which describes the same problem in the real world. Traditionally, we use a tuple **QNP = <F,V,I,G,O>** to express such an abstract Structure(an AOE network).Each node is a global state  $s=F+V$( fluents and variables),  and every action is edge linking **pre-state** with **effect-state**. Non-deterministic action can link one **pre-state** with so many **effect-states.**

Along with intuition, the input is so many concrete structures $S_n^\#$(example problems) and the corresponding policies solved in a classical planner like FF planner. With the fancy work by Srivastava(2011a), we can learn an abstract structure S, which can describe concrete structure $S_n^\#$ above.

For such an abstract structure S, we can enumerate nodes differently in their fluents and variables, and then we get the definition of **F** and **V.** Then states can be distinguished by **F** and **V.** **I** and **G** are just two S specific nodes. Similarly, enumerate edges as all possible actions, then we get **O. **For now, we already have found a definition of this problem with formal language using a tuple QNP = $<F,V,I,G,O>$.
