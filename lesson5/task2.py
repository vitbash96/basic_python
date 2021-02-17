filename = 'textfile.txt'
# try:
with open(filename,  encoding='utf-8') as myfile:
    lines =  myfile.readlines()
    print(f'File consists of: {len(lines)} lines')
    for line in lines:
        print(f'Line {line[:7]}... has {len(line.split())} words')
