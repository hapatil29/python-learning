######## FOR LOOP ###############



# numbers = [5, 2, 5, 2, 2]
#
# for num in numbers:
#     output = ''
#     for times in range(num):
#         output = output + 'x'
#     print(output)

# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total += item
# print(f"Total sum is {total}")

# for item in ['SUmanth','Hemanth','Netra']:
#     print(item)

# for item in 'Python':
#     print(item)

######## WHILE LOOP ###############


### Car game

# user_input = ""
# started = False
#
# print("""start - to start the car
# stop - to end the car
# quit - to exit""")
#
# while True:
#     user_input = input('> ').lower()
#
#     if user_input == 'start':
#         if started:
#             print('Car is running...')
#         else:
#             started = True
#             print('Car start... Ready to go!')
#     elif user_input == 'stop':
#         if not started:
#             print('Car is already stopped...')
#         else:
#             started = False
#             print('Car stopped')
#     elif user_input == 'help':
#         print("""start - to start the car
# stop - to end the car
# quit - to exit""")
#     elif user_input == 'quit':
#         break
#     else:
#         print("I don't understand that...")



### Guess game
# secret_number = 9
# guess_number = 0
# guess_limit = 3
#
# while guess_number < guess_limit:
#  guess = int(input('Guess: '))
#  guess_number += 1
#  if guess == secret_number:
#      print('You win!!!')
#      break
# else:
#  print('You lost')

