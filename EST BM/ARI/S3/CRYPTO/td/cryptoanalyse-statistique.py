def count_occurrences(M):
    # Initialize the list for occurrences with 26 zeros
    occurrences = [0] * 26

    # Loop through the characters in the string M
    for char in M:
        if 'A' <= char <= 'Z':
            # If the character is an uppercase letter, increment the corresponding counter
            occurrences[ord(char) - ord('A')] += 1

    return occurrences


# Test the function
M = "AABBBCDDXYZ"
occurrences = count_occurrences(M)

print("Occurrences of letters in the string:")
for i in range(26):
    print(chr(ord('A') + i) + ": " + str(occurrences[i]), end=' ')
