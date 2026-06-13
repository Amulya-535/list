def count_words(sentence):
    words = sentence.split()
    return len(words)


def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in sentence:
        if ch in vowels:
            count += 1

    return count


def longest_word(sentence):
    words = sentence.split()

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def reverse_each_word(sentence):
    words = sentence.split()

    reversed_words = []

    for word in words:
        reversed_words.append(word[::-1])

    return " ".join(reversed_words)


def character_frequency(sentence):
    freq = {}

    for ch in sentence.lower():

        if ch == " ":
            continue

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq


# Input
feedback = input("Enter Feedback: ")

# Output
print("\nTotal Words :", count_words(feedback))
print("Total Vowels :", count_vowels(feedback))
print("Longest Word :", longest_word(feedback))

print("\nReversed Words :")
print(reverse_each_word(feedback))

print("\nCharacter Frequencies :")

frequencies = character_frequency(feedback)

for key in frequencies:
    print(key, ":", frequencies[key])