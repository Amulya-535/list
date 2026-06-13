def count_words(sentence):
    return len(sentence.split())


def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    total = 0

    for vowel in vowels:
        total += sentence.count(vowel)

    return total


def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


def reverse_each_word(sentence):
    words = sentence.split()
    return " ".join(word[::-1] for word in words)


def character_frequency(sentence):
    sentence = sentence.lower().replace(" ", "")
    freq = {}

    for ch in sentence:
        freq[ch] = freq.get(ch, 0) + 1

    return freq


# Input
feedback = input("Enter Feedback: ")

print("\nTotal Words :", count_words(feedback))
print("Total Vowels :", count_vowels(feedback))
print("Longest Word :", longest_word(feedback))

print("\nReversed Words :")
print(reverse_each_word(feedback))

print("\nCharacter Frequencies :")

frequencies = character_frequency(feedback)

for char, count in frequencies.items():
    print(char, ":", count)