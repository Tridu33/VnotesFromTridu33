
# demo

```
"[] @ ys = ys" |
"(x #xs) @ ys = x# (xs @ys)"

primrec rev :: "'a list =>'a list" where
"rev [] = []" | 
"rev(x # xs) =(rev xs) @ (x#[])"

value "rev (True # False # [])"

value "rev (a # b # c # [])"
```


























