
def check_is_opposites(character1, character2):
    return (
        character1 and
        character2 and
        character1 != character2 and
        character1.upper() == character2.upper()
    )


def collapse_opposite_polarity_characters(input_string):
    remaining_characters = []

    def collapse_previous_characters():
        while remaining_characters:
            character1 = remaining_characters.pop() if remaining_characters else None
            character2 = remaining_characters.pop() if remaining_characters else None

            if not check_is_opposites(character1, character2):
                if character2:
                    remaining_characters.append(character2)
                if character1:
                    remaining_characters.append(character1)
                break

    for character in input_string:
        remaining_characters.append(character)
        collapse_previous_characters()

    return ''.join(remaining_characters)


def main():
    # input_string = 'dabAcCaCBAcCcaDA'  # test string

    filename = 'input/day05.txt'
    with open(filename, 'rt') as input_file:
        input_string = input_file.readline().strip()

    collapsed_string = collapse_opposite_polarity_characters(input_string)
    print(len(collapsed_string))


if __name__ == "__main__":
    main()
