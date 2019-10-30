# Open a text file and convert the row content to float.
for line in open('input_data.txt'):
    # Ignore lines starting with a # (they are comments).
    if not line.startswith('#'):
        # Got a valid data line.
        row = [float(item) for item in line.split()]
        # Print the data (in real life you would actually use them).
        print(row)
    
