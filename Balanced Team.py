def max_balanced_team(n, skills):
    # Sort the skills array
    skills.sort()
    
    max_team_size = 0
    left = 0
    
    # Use a sliding window to find the maximum number of students
    for right in range(n):
        # While the difference between the rightmost and leftmost student in the window is greater than 5, move the left pointer
        while skills[right] - skills[left] > 5:
            left += 1
        # Calculate the size of the current window
        max_team_size = max(max_team_size, right - left + 1)
    
    return max_team_size

# Reading input
n = int(input())
skills = list(map(int, input().split()))

# Compute and print the result
print(max_balanced_team(n, skills))
