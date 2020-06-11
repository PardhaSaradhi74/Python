
text = open("sample.txt", "r")#opening a file in read mode
directory = dict()#creating an empty directory
for line in text:# Loop through each line of the file
    line = line.strip()#negotiating spaces and newline characters
    line = line.lower()#converting to lowercase to avoid mismatch
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        if word in directory: # Check if the word is already in dictionary

            directory[word] = directory[word] + 1# Increment count of word by 1
        else:

            directory[word] = 1 # Add the word to dictionary with count 1
for key in list(directory.keys()): # Print the contents of dictionary
    x=key+ ":" +str(directory[key])
    print(x)
    file=open("sample.txt", "a+")
    file.write("\n")
    file.write(x)

file.close()