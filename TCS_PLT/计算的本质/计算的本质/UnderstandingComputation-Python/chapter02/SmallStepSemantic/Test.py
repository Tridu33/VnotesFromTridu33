from chapter02.SmallStepSemantic.Add import Add
from chapter02.SmallStepSemantic.Assign import Assign
from chapter02.SmallStepSemantic.Machine import Machine
from chapter02.SmallStepSemantic.Number import Number
from chapter02.SmallStepSemantic.Variable import Variable

Machine(
    Assign('x', Add(Variable('x'), Number(1))),
    {'x': Number(2)}
).run()

print('')
