import string
import itertools
import time

full = string.ascii_lowercase + string.digits
strlength = 0

def listByLength(length: int, letterOnly = False):
    if letterOnly == True:
        chars = string.ascii_lowercase
    else:
        chars = full
    combinations = []
    for i in range(length):
        combinations.extend(
                [
                    ''.join(x) for x in itertools.permutations(
                        chars, i+1
                    )
                ]
        )
    filtered = list(filter(lambda x: len(x) == length, combinations))
    return filtered

def get_input(prompt: str, answer_type, options: list) -> str | int:
    """
    Retries an input statement until the user correctly types an answer,
    returns the answer in the correct type which has been passed in.
    """

    correct_answer = False
    answer = None
    while not correct_answer:
        print("{ ", prompt, " }")
        answer = input()
        if answer in [None, ""] or answer.isspace() \
            or options != [] and answer.upper() not in options:
            continue

        try:
            answer = answer_type(answer)
            correct_answer = True
        except(ValueError, TypeError):
            continue
        except KeyboardInterrupt:
            exit()
    return str(answer)

def charGen(strlength: int, filename: str):
    usernames = listByLength(strlength)
    with open(filename, "w") as f:
        f.write(" ".join(usernames))
        f.write("\n")
    return usernames

def repeater(strlength: int, filename: str):
    usernames = []
    for i in string.ascii_lowercase:
        usernames.append(i*strlength)
    with open(filename, "w") as f:
        f.write(" ".join(usernames))
        f.write("\n")
    return usernames

def letterOnly(strlength: int, filename: str):
    usernames = listByLength(strlength, True)
    with open(filename, "w") as f:
        f.write(" ".join(usernames))
        f.write("\n")
    return usernames

def wordlistMenu():
    global strlength
    _type = [["Repeating", repeater], ["Letters only", letterOnly], ["Letters + digits", charGen]]
    i = 0
    for option in _type:
        print((" " * 8), ("×" * len(option[0])), (" " * 2), "\n")
        print("[ ", str(i), " - ", option[0], " ]")
        i += 1
    print("\n")
    chosentype = int(get_input("What\'s the type of the usernames?", int, []))
    strlength = int(get_input("How many letters should the usernames have?", int, []))
    filename = get_input("Where should I save the usernames?", str, [])
    print(("×" * len("Okay, starting!")), "\n")
    print("Okay, starting!")
    atStart = time.time()
    usernames = _type[chosentype][1](strlength, filename)
    delta = time.time() - atStart
    print(("×" * len(f"Done! Generated {len(usernames)} username combinations in {delta} seconds!")), "\n")
    print(f"Done! Generated {len(usernames)} username combinations in {delta} seconds!")

def main():
    options = [["Create wordlist", wordlistMenu], ["Exit", exit]]

    i = 0
    for option in options:
        print((" " * 8), ("×" * len(option[0])), (" " * 2), "\n")
        print("[ ", str(i), " - ", option[0], " ]")
        i += 1
    print("\n")
    opt = int(get_input("What\'s your option?", int, []))
    options[opt][1]()

if __name__ == "__main__":
    main()
