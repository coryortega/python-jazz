ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# for ninja in ninjas:
#     print(ninja)

# for ninja in ninjas[1:3]:
#     print(ninja)

for ninja in ninjas:
    if ninja == 'yoshi':
        print(f'{ninja} - black belt')
        # breaks out of the loop so ken is never reached
        break
    else:
        print(ninja)