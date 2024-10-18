# def fizzBuzz(n):
#     # Write your code here
#     for i in range (1,n+1):
#         if i%3 ==0:
#             if i%5 == 0:
#                 print("FizzBuzz")
#             else:
#                 print("Fizz")
#         elif i%5 ==0:
#             if i%3 == 0:
#                 break
#             else:
#                 print("Buzz")
#         else:
#             print(i)
# fizzBuzz(16)

# given an array integers, determine the numbers of moves to make all elements equal. each move consist of choosing all
# but 1 element and incrementing their value by 1

# numbers = [3,4,6,6,3]
#
# def countMoves(numbers):
#     moves = 0
#     while max(numbers)!= min(numbers):
#         numbers2 = [max(numbers)]
#         numbers.remove(max(numbers))
#         for i in numbers:
#             a = i+1
#             numbers2.append(a)
#         moves+=1
#         numbers =[]+numbers2
#
#     print(f"Count of moves: {moves}")
#
# countMoves(numbers)


# fc is trying to assemble a team from a roster of available players. thay have a minimum nimbers of players they want to
# sign, and each player needs to have a skill rating within a certain range. given a list of players skill levels with
# desired upper and lower bounds, determine how many teams can be created from list


skills = [12,4,6,13,5,10]
minPlayers = 3
minLevel=4
maxLevel=10

skills2 = []
for i in skills:
    if i >=4 and i <=10:
        skills2.append(i)
print(skills2)

import random
for i in skills2:
    team = random.sample(skills2,k = minPlayers)
print(team)
