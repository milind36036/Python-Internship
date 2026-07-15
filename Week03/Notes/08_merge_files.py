file1 = open("Week03/Notes/file1.txt", "r")
file2 = open("Week03/Notes/file2.txt", "r")

data1 = file1.read()
data2 = file2.read()

file1.close()
file2.close()

merged_file = open("Week03/Notes/merged.txt", "w")

merged_file.write(data1 + "\n" + data2)

merged_file.close()

print("Files merged successfully!")