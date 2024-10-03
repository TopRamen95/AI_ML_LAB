def minimum_edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a matrix to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Deleting all characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Inserting all characters to str1

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # Deletion
                    dp[i][j - 1] + 1,    # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )

    return dp[m][n]

# Example usage with multiple test cases
test_cases = [
    ("kitten", "sitting"),
    ("flaw", "lawn"),
    ("intention", "execution"),
    ("horse", "ros"),
    ("", "ABC"),
    ("ABC", "ABC"),
    ("ABC", "")
]

for str1, str2 in test_cases:
    distance = minimum_edit_distance(str1, str2)
    print(f"The minimum edit distance between '{str1}' and '{str2}' is: {distance}")
