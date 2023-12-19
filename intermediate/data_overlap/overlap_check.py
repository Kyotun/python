file1 = open("intermediate/data_overlap/file1.txt")
file1_texts = file1.readlines()
file1_stripped = [number.strip() for number in file1_texts]
file1.close()

file2 = open("intermediate/data_overlap/file2.txt")
file2_texts = file2.readlines()
file2_stripped = [number.strip() for number in file2_texts]
file2.close()

result = [number for number in file1_stripped if number in file2_stripped]
print(result)