
# # # simple Lamda
# val1 = 5

# add = (lambda x: x * x)  # fmt: off

# print(add(val1))

# # Get square root of all elements in list

# c = lambda nums: [element*element for element in nums]  # fmt: off
# print(c(range(1, 11)))


# # # Filter out even elements from list
# num_list = list(range(1, 11))

# #filtered_list = list(filter(lambda x: x % 2 != 0, num_list))  #kinda verbose
# filtered_list = [x for x in num_list if x % 2 != 0]  # kinda better?

# print(filtered_list)

# # # Only take words that start with b
# words = ["apple", "banana", "berry", "cherry", "blueberry", "kiwi"]

# words_only_b = [x for x in words if x.startswith("b")]

# print(words_only_b)

# # # two conditionsW
# nums = list(range(1, 21))
# nums_filtered = [x for x in nums if x % 3 == 0 and x % 2 != 0]

# print(nums_filtered)

# # # Keeps only the odd numbers & Squares each of those odd numbers

# nums = list(range(1, 21))

# nums_filteres = [x * x for x in nums if x % 2 != 0]

# print(nums_filteres)

# # # Only include strings longer than 3 characters
# # # Convert those strings to uppercase

# words = ["hi", "apple", "no", "banana", "cat", "doge"]
# words_filtered = [x.upper()
# for x in words
# if len(x) >= 3]

# print(words_filtered)


# # # Keep only words that contain the letter: a
# # # Return them in reversed lowercase form

words = ['HI', 'APPLE', 'NO', 'BANANA', 'CAT', 'DOGE']
# # # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
words_filtered = [
    x[::-1].lower()
    for x in words
    if "A" in x]  # shouldnt a be lowercase???


print(words_filtered)

# # # Using only lambda functions, filter(), map(), and sorted(),
# # # do the following:

# # # Filter the list to keep only people who:

# # # Have "art" as one of their hobbies
# # # AND are at least 25 years old

# # # Map the result into a list of names, but:

# # # In UPPERCASE
# # # AND reversed

# # # Sort the final names by length, longest to shortest.


# people = [
#     {"name": "Alice", "age": 30, "hobbies": ["chess", "art"]},
#     {"name": "Bob", "age": 25, "hobbies": ["football", "coding", "art"]},
#     {"name": "Charlie", "age": 35, "hobbies": ["reading"]},
#     {"name": "Diana", "age": 28, "hobbies": ["art", "reading", "chess"]},
#     {"name": "Eve", "age": 22, "hobbies": ["coding", "chess"]}
# ]

# people_filtered = [
#     # {x["name"][::-1].upper(): x["hobbies"][1]}
#     x["name"][::-1].upper()
#     for x in people
#     if x["age"] >= 25 and "art" in x["hobbies"]]

# print(people_filtered)