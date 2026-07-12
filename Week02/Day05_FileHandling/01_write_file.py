# Writing Data to a Text File

file = open("student.txt", "w")

file.write("Name: Milind Bhatnagar\n")
file.write("Course: B.Tech AIML\n")
file.write("City: Ghaziabad\n")

file.close()

print("Data written successfully.")