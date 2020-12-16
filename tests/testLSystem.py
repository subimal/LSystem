from LSystem import LSystem

Algae = LSystem(variables = "A B".split(), constants =[], axiom="A", rules={"A": "AB", "B":"A"})
FractalTree = LSystem(variables = "0 1".split(), constants ="[ ]".split(), axiom="0", rules={"1": "11", "0":"1[0]0"})
CantorSet = LSystem(variables="A B".split(), constants=[], axiom = "A", rules={"A":"ABA", "B":"BBB"})
KochCurve = LSystem(variables="F".split(), constants="+ -".split(), axiom = "F", rules={"F":"F+F−F−F+F"})
