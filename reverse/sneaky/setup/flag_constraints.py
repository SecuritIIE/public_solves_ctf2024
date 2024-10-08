from collections import defaultdict

# Given string
string = "FSIIECTF{6d211d61d642be9f891db55710ef0ade}"

# Step 1: Character frequency and positions
char_freq = defaultdict(int)
char_positions = defaultdict(list)

for i, char in enumerate(string):
    char_freq[char] += 1
    char_positions[char].append(i)

# Print character frequencies and positions
print("Character Frequencies and Positions:")
for char, freq in char_freq.items():
    print(f"Character '{char}' occurs {freq} times at positions {char_positions[char]}")

# Step 2: Find the largest repeating pattern
def find_largest_pattern(s):
    n = len(s)
    largest_pattern = ""
    max_count = 0

    for length in range(1, n // 2 + 1):  # Length of the pattern
        for i in range(n - length + 1):  # Start of the pattern
            pattern = s[i:i + length]
            count = s.count(pattern)

            if count > 1 and len(pattern) > len(largest_pattern):
                largest_pattern = pattern
                max_count = count

    return largest_pattern, max_count

largest_pattern, pattern_count = find_largest_pattern(string)

# Print the largest repeating pattern
print(f"Largest Repeating Pattern: '{largest_pattern}' occurs {pattern_count} times")

# Count characters in the largest pattern
pattern_char_freq = defaultdict(int)
for char in largest_pattern:
    pattern_char_freq[char] += 1

print("Character Frequencies in the Largest Pattern:")
for char, freq in pattern_char_freq.items():
    print(f"Character '{char}' occurs {freq} times in the largest pattern")
