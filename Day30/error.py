# fruits = ["apple", "banana", "cherry"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(f"{fruit} pie")
#
# make_pie(2)

facebook_posts = [
    {"likes": 21, "comments": 5, "shares": 2},
    {"likes": 13, "shares": 1},
    {"comments": 12, "shares": 7},
    {"likes": 5},
    {"comments": 3},
    {"likes": 34, "comments": 8},
    {"shares": 4},
]

likes = 0

for post in facebook_posts:
    try:
        likes += post["likes"]
    except KeyError:
        pass

print(likes)