from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(AKnight, Not(And(AKnight, AKnave))),  # A não pode ser cavaleiro e vilão ao mesmo tempo.
    Implication(AKnave, Not(And(AKnight, AKnave)))    # A não pode ser cavaleiro e vilão ao mesmo tempo.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(AKnight, And(AKnave, BKnave)),  # Se A é cavaleiro, então A e B são vilões.
    Implication(AKnave, Not(And(AKnave, BKnave)))  # Se A é vilão, então A e B não podem ser vilões ao mesmo tempo.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(AKnight, Biconditional(AKnight, BKnight)),  # Se A é cavaleiro, então A e B são do mesmo tipo.
    Implication(AKnave, Biconditional(AKnave, BKnave)),  # Se A é vilão, então A e B são do mesmo tipo.
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  # Se B é cavaleiro, então A e B são de tipos diferentes.
    Implication(BKnave, Not(Biconditional(AKnave, BKnave)))  # Se B é vilão, então A e B são de tipos diferentes.
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),  # A diz "Eu sou cavaleiro ou vilão".
    Implication(BKnight, AKnave),  # Se B é cavaleiro, então A é vilão.
    Implication(BKnave, AKnight),  # Se B é vilão, então A é cavaleiro.
    Implication(CKnight, AKnight),  # Se C é cavaleiro, então A é cavaleiro.
    Implication(CKnave, AKnave)  # Se C é vilão, então A é vilão.
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()