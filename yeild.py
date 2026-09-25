def fetch_lines(filename):
    with open (filename,'r') as f:
        # lines=[]
        for line in f:
            # lines.append(line)
            yield line

zen= fetch_lines("long-doc.txt")
for line in zen:
    print(line, end="")
