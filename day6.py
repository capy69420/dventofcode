# Initialize the four most recently received characters
latest_characters = []

#Solution

# Read input from file
with open('input6.txt') as f:
    data = f.read()
    
# Part 1
# Initialize variables
marker_length = 4
marker_count = 0

# Iterate over each character in the data
for i in range(len(data)):
    # Check if the length of the marker is equal to the length of the window
    if marker_length == len(data[i-marker_length:i]):
        # Check if all characters are distinct
        if len(set(data[i-marker_length:i])) == marker_length:
            marker_count = i
            break

# Print the answer
print("Part 1: The first start-of-packet marker is detected after {} characters.".format(marker_count))

# Part 2
# Initialize variables
marker_length = 14
marker_count = 0

# Iterate over each character in the data
for i in range(len(data)):
    # Check if the length of the marker is equal to the length of the window
    if marker_length == len(data[i-marker_length:i]):
        # Check if all characters are distinct
        if len(set(data[i-marker_length:i])) == marker_length:
            marker_count = i
            break

# Print the answer
print("Part 2: The first start-of-message marker is detected after {} characters.".format(marker_count))