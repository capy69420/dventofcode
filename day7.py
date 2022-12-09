# Code

# Initialize the current directory to the root directory
current_dir = ''

# Create an empty dictionary to store the directory tree
dir_tree = {}

def process_line(line, current_dir,f):
# Check if the line starts with a '$' character, indicating that it contains a command
    if line[0] == '$':
        # Split the line by spaces to extract the command and its arguments
        command = line.split()[1]     
        # Check the command and process it accordingly
        if command == 'cd':
            # Extract the argument of the 'cd' command
            argument = line.split()[2]
            
            # Split the current directory into a list of path components
            path_components = current_dir.split('/')
            if argument == '/':
                current_dir = '/'
            # If the argument is '..', remove the last path component from the list
            if argument == '..':
                path_components.pop()
            # Otherwise, append the argument to the list of path components
            else:
                if argument != '/':
                    path_components.append(argument)
            # Update the current directory to the new path
            current_dir = '/'.join(path_components)
            print(path_components)
            # Add the current directory to the directory tree
            dir_tree[current_dir] = {'dir':current_dir}
        # If the command is 'ls', process the file sizes and subdirectories listed in the file
        elif command == 'ls':
            # Initialize the size to 0
            size = 0
            # Read the file until we encounter the next command or reach the end of the file
            for line in f:
                # If the line starts with a digit, it contains a file size, so add it to the tree
                if line[0].isdigit():
                    filename = line.split()[1]
                    dir_tree[current_dir + filename] = {'dir': current_dir + '/' + filename,'size':int(line.split()[0])}
                # If the line starts with a '$' character, it contains the next command, so break the loop
                elif line[0] == '$':
                    # process the line after 'ls' displayed everything
                    process_line(line, current_dir,f)
                # Otherwise, the line contains the name of a subdirectory, so add it to the directory tree
                else:
                    dir_name = line.split()[1]
                    dir_tree[current_dir + '/' + dir_name] = {'dir': current_dir + '/' + dir_name}

# Open the file containing the representation of the directory tree
with open("input7.txt") as f:
    # Read the file line by line
    for line in f:
        process_line(line, current_dir,f)
                        

# Initialize the total size of all files smaller than or equal to 100,000 bytes to 0
total_size = 0

# Iterate over the entries in the directory tree
for item in dir_tree.items():
    # If the value of the entry is a tuple, it represents a directory with a file size
    s = item[1]
    if ('size' in s and s['size']<=100000) :
        print(s["size"])
        total_size += s['size']

# Print the total size of all files that
print(total_size)