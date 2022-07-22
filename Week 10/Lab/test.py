game = [0]
answer = input('Do you want to go first? (Yes/No) ')
if answer.title() == 'Yes':
    while True:
        num_input = int(input('How many number you prefer to add '))
        if num_input >= 4 or num_input <= 0:
            print('Error')
        else:
            i = 1
            while i <= num_input:
                a = int(input('Enter the value '))
                game.append(a)
                i += 1
            if game[-1] == 30:
				print('CONGRATULATION YOU ARE WIN')
                break
            else:
                # try to dominate 3n+2
                if game[-1] % 4 == 2:
                    game.append(game[-1] + 1)
                else:
                    while game[-1] % 4 != 2:
                        game.append(game[-1] + 1)
                print('After computer move')
                print(game)
                if game[-1] == 30:
					print('You are loser')
					break

else:
    print(1)