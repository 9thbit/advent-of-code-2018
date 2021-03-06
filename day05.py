
def check_is_opposites(character1, character2):
    return (
        character1 and
        character2 and
        character1 != character2 and
        character1.upper() == character2.upper()
    )


def collapse_opposite_polarity_characters(input_string, characters_to_skip=None):
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
        if characters_to_skip and character in characters_to_skip:
            continue

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

    unique_characters = set(map(str.lower, input_string))
    shortest_collapsed_string_length = min(
        len(
            collapse_opposite_polarity_characters(
                input_string,
                characters_to_skip={character, character.upper()},
            )
        )
        for character in unique_characters
    )
    print(shortest_collapsed_string_length)


if __name__ == "__main__":
    main()
