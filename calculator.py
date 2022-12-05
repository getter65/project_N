def calculator(user_input):

    compilet_input = compile(user_input, 'string', 'eval')

    return compilet_input


if __name__ == "__main__":

    user_input = input("Введите выражение:/n:")
    print(f"{user_input} = {eval(calculator(user_input))}")


