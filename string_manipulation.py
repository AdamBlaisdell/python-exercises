# methods that deal with manipulating strings


# reverse a string using a loop
def reverse_string(word):
    output = ""
    for ch in word:
        output = ch + output
    return output


# reverse a string using slicing
def reverse_string_two(word):
    word = word[::-1]
    return word


# reverse a string using .join
def reverse_string_three(word):
    output = "".join(reversed(word))
    return output


if __name__ == '__main__':
    print(reverse_string("myword"))
    print(reverse_string_two("myword2"))
    print(reverse_string_three("myword3"))
