    matrix = []    
    for line in f:
        # store line in a list
        rows = line.split()
        rows = [int(h) for h in rows]
        print(line)
        
        for number in rows:
            digits = [int(n) for n in str(number)]
            matrix.append(digits)
