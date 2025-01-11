# name = input("Please enter your name: ")
# score = int(input("enter your score:"  ))
# # print(type(score))
# if score >= 70 and score <= 100:
#     message = (f"{name}, your score is {score} you get an A")
# elif score >= 60 and score < 70:
#     message = (f"{name}, your score is {score} you get a B")
# elif score >= 50 and score < 60:
#     message = (f"{name}, your score is {score} you get a C")
# elif score >= 40 and score < 50:
#     message = (f"{name}, your score is {score} you get a D")
# elif score >= 30 and score < 40:
#     message = (f"{name}, your score is {score} you  get an E")
# else:
#     message = (f"{name}, your score is {score} you  get an F")
    
# print(message)

# # username = input("Please type in your name")
# # if len(username) > 5 and username.isalpha():
# #     print("username is valid")
# # else:
# #     print("username is not valid")
# #     if username.isalpha():
# #         print("username is valid")
# #     else:
# #         print("username is not valid")
# # else: print("username is not valid")
    
# username = input("enter your username")
# if username.isalpha():
#     password = input("enter your password")
#     if len(password) > 4:
#         print("welcome user")
#     else:
#         print("password must be greater than 4")
# else:
#     print("username must be alphabet")

friends = ["Isa", "John", "George", "Hamza", "Ameer"]
followers = ("Ali", "Mary", "Jane", "Usman", "Suzan")
friends[2]="Esther"
# print(friends)
print(friends.index("Isa"))
# converted_tuple = tuple(friends)
# print(converted_tuple)
# converted_list = list(followers)
# print(converted_list)
# print(type(friends))
# print(type(followers))
# print(dir(followers))