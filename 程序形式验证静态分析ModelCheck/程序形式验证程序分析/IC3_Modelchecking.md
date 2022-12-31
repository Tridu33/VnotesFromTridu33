
[Infinite-state invariant checking with IC3 and predicate abstraction](https://link.springer.com/article/10.1007/s10703-016-0257-4)


https://github.com/Z3Prover/z3/blob/master/examples/python/mini_ic3.py




https://github.com/pddenhar/Z3-IC3-PDR


Implementation of the IC3 / Property Directed Reachability algorithm using the the Z3 SMT solver. Peter Den Hartog, 2016.





















# 1. kind2能求解IC3

kind2 


https://kind.cs.uiowa.edu/kind2_user_doc/1_techniques/4_ic3.html









# 2. IC3_Modelchecking



https://www.cnblogs.com/bacmive/p/14125519.html
IC3简析


IncrementalConstruction ofInductive Clauses for Indubitable Correctness
http://www.cs.tau.ac.il/~msagiv/courses/asv/IC3.pdf





如何理解model checking中的IC3技术？ - rainoftime的回答 - 知乎
https://www.zhihu.com/question/59299573/answer/163801149

IC3最初来自基于SAT的硬件模型检查，“ 发在VMCAI'11 sat-based model checking without unrolling, 。后来很多人难以理解其中的思想，作者又写了一篇Understanding IC3，发在SAT'12 （Understanding IC3）”。。后来推广到SMT（支持某些first order theory），很多地方也有叫PDR（property guided reachability），有各种实现方法。。

下面是一个简单的实现，供参考。。（ 个人觉得，如果有时间兴趣和精力，了解下symbolic model checking一系列发展后如bmc, k-induction, predicate abstraction, CEGAR, interpolation guided refinement等后能有更深刻的理解，，当然这不是必须的。。。）


```python

#coding: utf-8

# IC3-PDR algorithm for symbolic model checking
# 
from z3 import *

#This helper class specifies a cube and a frame
#in which it is reachable.
class Cube(object):
    def __init__(self, model, variable_lookup, i = None):
        self.values = [simplify(variable_lookup[str(v)] == model[v]) for v in model if str(v) in variable_lookup]
        self.i = i

    @property
    def cube(self):
        return And(*self.values)

    @property
    def not_cube(self):
        return Or(*[Not(value) for value in self.values])

    def __repr__(self):
        return "{" + ("" if self.i == None else str(self.i) + ": ") + str(self.values) + "}"

class StackFrame(object):
    def __init__(self, *cubes):
        self.cubes = list(cubes)
        self.expression = And(*cubes)
    def add_cube(self, cube):
        self.cubes.append(cube)
        self.expression = And(*self.cubes)

class PDR(object):
    def __init__(self, variables, primes, init, trans, post):
        self.variables = variables
        self.variable_dict = {str(v): v for v in self.variables}
        self.primes = primes
        self.vTOp = zip(variables, primes)
        self.init = init
        self.trans = trans
        self.post = post

        self.stack_frames = [StackFrame(init)]
        self.stack_trace = []

    #Finds a cube in ~post and the latest frame
    def getBadCube(self):
        s = Solver()
        s.add(And(Not(self.post), self.stack_frames[self.N].expression))
        if s.check() == sat:
            return Cube(s.model(), self.variable_dict, self.N)
        return None

    def newFrame(self):
        print self.N,
        sys.stdout.flush()
        self.stack_frames.append(StackFrame())

    #Checks whether a cube has been entirely blocked
    #in the given frame, only for performance
    def isBlocked(self, cube, i):
        s = Solver()
        s.add(And(self.stack_frames[i].expression, cube))
        return s.check() == unsat

    #Tries to find a cube in the previous frame that would
    #reach the given cube
    def solveRelative(self, cube):
        cubePrime = substitute(cube.cube, self.vTOp)
        s = Solver()
        s.add(self.stack_frames[cube.i - 1].expression)
        s.add(self.trans)
        s.add(cubePrime)
        if s.check() == unsat:
            return None
        return s.model()

    #Checks whether the we have found an inductive invariant
    def induct(self):
        for i, frame in enumerate(self.stack_frames[:-1]):
            check_frame = frame.expression
            s = Solver()
            s.add(And(self.trans, check_frame,
                Not(substitute(check_frame, self.vTOp))))
            invariant = s.check() == unsat
            if invariant:
                return check_frame
        return None

    #Attemps to block a cube recursively
    #Returns None if the cube was able to be blocked
    #Returns a stack trace if the cube cannot be blocked
    def blockCube(self, cube):
        #If solution is for frame 0, we have found a stack trace reaching ~post
        if cube.i == 0:
            return [cube]
        while True:
            assert(not self.isBlocked(cube.cube, cube.i))
            solution = self.solveRelative(cube)
            #The cube is found to be unreachable by the previous frame
            if solution == None:
                #Block it in the frame it is found in and all previous frames
                for i in range(1, cube.i + 1):
                    if not self.isBlocked(cube.cube, i):
                        self.stack_frames[i].add_cube(simplify(cube.not_cube))
                return None
            #The cube is found to be reachable by the previous frame
            else:
                candidate = {v: solution[v] for v in solution if str(v) in self.variable_dict}
                candidateCube = Cube(candidate, self.variable_dict, cube.i - 1)
                #Attempt to block this new candidate as well
                trace = self.blockCube(candidateCube)
                if trace:
                    return trace + [cube]
        return None

    #Main entry point of PDR
    def run(self):
        print "Current frame",
        self.newFrame()
        while True:
            cube = self.getBadCube()
            if cube:
                trace = self.blockCube(cube)
                if trace != None:
                    return False, trace
            else:
                invarient = self.induct()
                if invarient:
                    return True, invarient
                self.newFrame()

    @property
    def N(self):
        return len(self.stack_frames) - 1
```




1. SAT-Based Model Checking without Unrolling
2. IC3 - Flipping the E in ICE
3. Understanding IC3   https://dl.acm.org/doi/10.1007/978-3-642-31612-8_1
4. Eﬃcient implementation of property directed reachability







