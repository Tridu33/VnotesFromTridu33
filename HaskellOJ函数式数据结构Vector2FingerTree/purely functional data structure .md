# purely functional data structure 








https://github.com/bdkoepke/pfds  Examples and exercises from Purely Functional Data Structures by Okasaki.




(Purely Functional Data Structures_okasaki)[file:///C:/Users/admin/Downloads/Documents/Purely%20Functional%20Data%20Structures_okasaki.pdf]



https://cstheory.stackexchange.com/questions/1539/whats-new-in-purely-functional-data-structures-since-okasaki

Since Chris Okasaki's 1998 book "Purely functional data structures", I haven't seen too many new exciting purely functional data structures appear; I can name just a few:

-   [IntMap](http://hackage.haskell.org/packages/archive/containers/0.1.0.1/doc/html/Data-IntMap.html) (also invented by Okasaki in 1998, but not present in that book)
-   [Finger trees](http://apfelmus.nfshost.com/articles/monoid-fingertree.html) (and their generalization over monoids)

There are also some interesting ways of implementing already known datastructures, such as using "nested types" or "generalized algebraic datatypes" to ensure tree invariants.

Which other new ideas have appeared since 1998 in this area?