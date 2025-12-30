s = input("Enter string: ")

words = s.split()
sorted_words = [''.join(sorted(word)) for word in words]
result = ' '.join(sorted_words)

print(result)
