file = open("Week03/Notes/sample.txt", "r")

lines = file.readlines()

print("Total number of lines:", len(lines))

file.close()