from chapter03.RegularExpression.Choose import Choose
from chapter03.RegularExpression.Concatenate import Concatenate
from chapter03.RegularExpression.Empty import Empty
from chapter03.RegularExpression.Literal import Literal
from chapter03.RegularExpression.Repeat import Repeat

pattern = Repeat(
    Choose(
        Concatenate(Literal('a'), Literal('b')),
        Literal('a')
    )
)
print(pattern)

print('\n')

nfa_design = Empty.to_nfa_design()
print(nfa_design.accepts(''))
print(nfa_design.accepts('a'))

print('\n')

nfa_design = Literal('a').to_nfa_design()
print(nfa_design.accepts(''))
print(nfa_design.accepts('a'))
print(nfa_design.accepts('b'))

print('\n')

print(Empty().matches('a'))
print(Literal('a').matches('a'))

print('\n')

pattern = Concatenate(Literal('a'), Literal('b'))
print(pattern)
print(pattern.matches('a'))
print(pattern.matches('ab'))
print(pattern.matches('abc'))

print('\n')
pattern = Choose(Literal('a'), Literal('b'))
print(pattern)
print(pattern.matches('a'))
print(pattern.matches('b'))
print(pattern.matches('c'))