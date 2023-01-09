# Code

# Initialize the current directory to the root directory
current_dir = ''

# Create an empty dictionary to store the directory tree
dir_tree = {}

def process_line(line, current_dir, path_components, f):
# Check if the line starts with a '$' character, indicating that it contains a command
    if line[0] == '$':
        # Split the line by spaces to extract the command and its arguments
        command = line.split()[1]     
        # Check the command and process it accordingly
        if command == 'cd':
            # Extract the argument of the 'cd' command
            argument = line.split()[2]
            
            # Split the current directory into a list of path components
            
            # If the argument is '..', remove the last path component from the list
            if argument == '..':
                path_components.pop()
            # Otherwise, append the argument to the list of path components
            else:
                path_components.append(argument)
            # Update the current directory to the new path
            current_dir = '/' + '/'.join(path_components)
            if argument == '/':
                current_dir = '/'
            
        # If the command is 'ls', process the file sizes and subdirectories listed in the file
        elif command == 'ls':
            # Initialize the size to 0
            size = 0
            # Read the file until we encounter the next command or reach the end of the file
            for line in f:
                l = line.rstrip().split()
                if len(path_components) > 1:
                    current_dir = '/' + '/'.join(path_components)
                # If the line starts with a digit, it contains a file size, so add it to the tree
                if l[0].isdigit():
                    filename = l[1]
                    # generate the sub tree
                    d = dir_tree
                    for i in path_components:
                        d = d[i]
                    d[filename] = {'size':int(l[0])}
                # If the line starts with a '$' character, it contains the next command, so break the loop
                elif l[0] == '$':
                    # process the line after 'ls' displayed everything
                    process_line(line, current_dir, path_components, f)
                # Otherwise, the line contains the name of a subdirectory, so add it to the directory tree
                elif l[0] == 'dir':
                    dir_name = l[1]
                    # generate the sub tree
                    d = dir_tree
                    for i in path_components:
                        d = d[i]
                    d[dir_name] = {'dir': dir_name}

max_size = []
def dir_size(tree, max_size):
    s = 0
    for key in tree:
        # file
        if 'size' in tree[key]:
            s += tree[key]['size']
        # directory
        else:
            if 'dir' in tree[key]:
                s += dir_size(tree[key], max_size)
    if s <= 100000:
        max_size.append(s)
        print(tree,s)
    return s
        
# Open the file containing the representation of the directory tree
with open("input7.txt") as f:
    # Read the file line by line
    for line in f:
        process_line(line, current_dir, [], f)
                        

# Initialize the total size of all files smaller than or equal to 100,000 bytes to 0
total_size = 0
full = dir_size(dir_tree, max_size)
print(sum(max_size))
# Iterate over the entries in the directory tree
for item in dir_tree.items():
    # If the value of the entry is a tuple, it represents a directory with a file size
    s = item[1]
    dir = item[0]
    if ('size' in s and s['size']<=100000) :
        total_size += s['size']

# Print the total size of all files that
print(total_size)