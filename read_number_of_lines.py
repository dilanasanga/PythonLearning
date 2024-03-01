filename = input()
f = open(filename,"r")
numberoflines = len(f.readlines())
print ("Number of lines in the file", '"',filename,'"', "=", numberoflines)
