overhang_with_n_blocks = L/2 + L/4 + L/6 + ... + L/(2n)       # in cm

In words: with 0 blocks the overhang is 0, and block number k adds L / (2 × k) cm to the overhang. 



print ("Length:", L)
print ("stock:", stock)
print ("largest_allowed_overhang:", largest_allowed_overhang)

############################

# ACT-04 Leaning Tower of Lire: ACT04_tower.py
# CMSC 202 Principles of Programming, A.Y. 2026-2027
#
# Name:
# Student number:
#
# WHAT THIS PROGRAM DOES
#   It asks for your student number and the overhang you want (in cm),
#   keeps asking until the overhang is allowed, then stacks blocks ONE AT A
#   TIME, printing the overhang after each block, until the overhang is
#   reached or the blocks run out. At the end it reports how many blocks
#   are needed.
#
#   This is YOUR program. It follows YOUR pseudocode (ACT04_design.md).
#
# RULES
#   You MAY use: while, for with range(), if / elif / else, comparison
#   operators, logical operators (and, or, not), arithmetic, assignment,
#   and the built-ins input(), int(), float(), round(), print(), range().
#   Do NOT use: def, class, lambda, lists, sets, dictionaries,
#   comprehensions, "x if c else y" one-line conditionals, the word "in" to
#   test membership (the "in" of "for k in range(...)" is fine),
#   try / except / raise, import (no math module), or any other built-in
#   such as sum(), min(), max(), abs(), len().
#
# HOW TO COMPLETE THIS FILE
#   1. Replace every "# TODO" with your own code. Add comments that explain
#      what each part does (documentation is graded).
#   2. Run the two samples from your design and check that the printed
#      lines match your hand trace.
#   3. You may assume every number typed is a valid number. The overhang may
#      still be negative or too large; your program must ask again.
#
# The file already runs. It prints only zeros until you fill it in.

# ---------------------------------------------------------------------
# 1. STUDENT NUMBER AND PERSONAL VALUES
# ---------------------------------------------------------------------
student_number = input("Enter your student number (for example 2026-12345): ")
t = int(student_number[-4:])   # last 4 digits, for example 2026-12345 gives 2345

L = 10 + t % 11         # DONE block length in cm (see the handout)
stock = 10 + t % 21     # DONE number of blocks available (see the handout)
largest_allowed_overhang = 3 * L   # DONE largest allowed overhang in cm (see the handout)
largest_allowed_overhang_checker = True

print("Block length:", L, "cm | Blocks available:", stock)

# ---------------------------------------------------------------------
# 2. TARGET OVERHANG (keep asking until it is allowed)
# ---------------------------------------------------------------------
while (largest_allowed_overhang_checker):
    target = float(input("Enter overhang length (cm): "))
    if 0 <= target <= largest_allowed_overhang:
        largest_allowed_overhang_checker = False
    else:
        print("Invalid overhang length. Please enter a value between 0 and", largest_allowed_overhang, "cm.")

# ---------------------------------------------------------------------
# 3. SIMULATION (one block per pass)
# ---------------------------------------------------------------------
blocks = 0
overhang = 0.0
print("With 0 blocks, the overhang is 0 cm")




for k in range(1, stock + 1):
    overhang += L / (2 * k)
    blocks += 1
    print("With", blocks, "blocks, the overhang is", overhang, "cm")
    if overhang >= target:
        break




# ---------------------------------------------------------------------
# 4. RESULT
# ---------------------------------------------------------------------
# TODO: print the number of blocks needed, or explain that the blocks ran
#       out and how many blocks would be needed.