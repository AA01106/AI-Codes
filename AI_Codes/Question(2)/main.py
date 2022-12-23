# Here we import everything from logic.py
from logic import *   

def my_tr_table_fn();
# We must create all the variables we need in the same call of the vars function
A, B, Smoke, Fire= vars('A', 'B', 'Smoke', 'Fire')

# Formula c in question 1 
formula_1c = ((A&B)&~((A>>B)&(B>>A)))

print("Formula 1-C is: \n")
print(formula_1c, "\n")

print("The Truth table for formula 1-C is: \n")
formula_1c.print_truth_table()

print("Is contradiction proved: \n")
print(formula_1c.is_contradiction())

print("Is tautology proved: \n")
print(formula_1c.is_tautology())
print("-----------------------------------------------------------------------")
# # Formula a in question 2

# formula_2a = (Smoke>>Smoke)

# print("Formula 2-A is: \n")
# print(formula_2a, "\n")

# print("The Truth table for formula 2-A is: \n")
# formula_2a.print_truth_table()

# print("Is tautology proved: \n")
# print(formula_2a.is_tautology())
# print("-----------------------------------------------------------------------")

# # Formula b in question 2

# formula_2b = (Smoke>>Fire)

# print("Formula 2-B is: \n")
# print(formula_2b, "\n")

# print("The Truth table for formula 2-B is: \n")
# formula_2b.print_truth_table()

# print("Is tautology proved: \n")
# print(formula_2b.is_tautology())
# print("Is contradiction proved: \n")
# print(formula_2b.is_contradiction())
# print("-----------------------------------------------------------------------")
