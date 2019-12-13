from pprint import pprint
# List
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]

zeros = [0]*5
print(zeros)

combined = zeros + letters  # concatenation
print(combined)

numbers = list(range(20))
print(numbers)

chars = list("Hello World")
print(chars)

print("------------------")
print(letters[0:3])
print(letters[:3])
print(letters[:])
print(letters[::2])  # every two items
print(letters[::-1])  # reverse order

# List unpacking
# the variables need to be the same as the list length
first, second, third = letters
print(first)

first_1, *other = letters
print(first_1)
print(other)

new_numbers = [1, 2, 3, 4, 5, 6, 7]
new_1, *others, last = new_numbers

print(new_1, last)
print(others)
print("*************************** Looping List ***********************")
new_letters = ["e", "t", "h"]
for letter in new_letters:
    print(letter)

# enumerate --> it creates a tuple
for index, letter in enumerate(new_letters):
    print(index, letter)


print("**** ADDING OR REMOVING ****************")
# append to the end of the list
# insert at a desired position
# remove at the end --> pop
# remove at certain position --> pop(1)
# remove("b") ==> it will remove the 1st occurrence of "b"
del letters[0:3]
letters.clear
print(letters)


print("**** FINDING AN INDEX ***")
print(new_letters.index("t"))

if "d" in new_letters:
    print(new_letters.index("d"))

print("\r\n")
print("***** SORTING *******")
# new_letters.sort()

print(sorted(new_letters))
print(new_letters)

items = [
    ("Product1", 12),
    ("Product2", 3),
    ("Product3", 1),
    ("Product4", 15)
]
print(items)


def sort_item(item):
    return item[1]


prices = list(map(lambda item: item[1], items))
# items.sort(key=sort_item)
#items.sort(key=lambda d: d[1])
print(prices)

print("\r\n")
print("******* FILTER*********")
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

sentence = "This is a common interview question"
new_sentence = sentence.lower()
print(new_sentence)

result = {}
for i in new_sentence:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
pprint(result, width=1)

sorted_result = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_result[0])
