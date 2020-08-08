import random
game = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
game_choices = list(game.keys())
commands = ["!exit", "!rating"]


def read_file():
    rating_file = open("rating.txt", "r")
    text = rating_file.read()
    rating_file.close()
    return text


def write_file(text):
    rating_file = open("rating.txt", "w")
    for line in text:
        rating_file.write(str(line) + "\n")
    rating_file.close()


def check_profile(user_name):
    text = read_file()
    if text.__contains__(user_name):
        return True
    else:
        return False


def get_score(user_name):
    rating_file = open("rating.txt", "r")
    result = 0
    for line in rating_file:
        result = line.split(" ")
        if result[0] == user_name:
            result = result[1]
            rating_file.close()
            return result
    rating_file.close()


def print_score(result):
    print("Your rating: {}".format(result))


def prepare_file(user_name, key):
    if key == "draw":
        add(user_name, 50)
    elif key == "win":
        add(user_name, 100)


def add(user_name, add_value):
    text = read_file().split("\n")
    for i in range(len(text)):
        line = text[i].split(" ")
        if line[0] == user_name:
            score = int(line[1])
            line[1] = str(score + add_value)
            text[i] = line[0] + " " + line[1]
            break
    write_file(text)


def create_profile(user_name):
    text = read_file().split("\n")
    text.append("{} 0".format(user_name))
    write_file(text)


def run(user_name):
    while True:
        user_choice = input()
        if not check_profile(user_name):
            create_profile(user_name)
        if game_choices.__contains__(user_choice) or commands.__contains__(user_choice):
            computer_choice = game_choices[random.randint(0, 2)]
            if user_choice == "!exit":
                print("Bye!")
                break
            elif user_choice == "!rating":
                print_score(get_score(user_name))
            elif user_choice == computer_choice:
                print("There is a draw ({})".format(user_choice))
                prepare_file(user_name, "draw")
            elif computer_choice == game.get(user_choice):
                print("Well done. Computer chose {} and failed".format(computer_choice))
                prepare_file(user_name, "win")
            else:
                print("Sorry, but computer chose {}".format(computer_choice))
        else:
            print("Invalid input")


name = input("Enter your name:")
print("Hello, {}".format(name))
run(name)
