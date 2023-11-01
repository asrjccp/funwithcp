import random

def find_all_possible_sequences(i, j, val, sequence):
    if val == k and sorted(sequence) not in possible_sequences:
        possible_sequences.append(sorted(sequence))
        return 
    if val > k:
        return 
    if not(0 <= i <= len(grid)-1 and 0 <= j <= len(grid[i])-1):
        return
    # move on, don't take
    find_all_possible_sequences(i+1, j, val, sequence)
    find_all_possible_sequences(i, j+1, val, sequence)
    # take and move on
    find_all_possible_sequences(i+1, j, val+grid[i][j], sequence+[chr(ord('A')+j+i*5)])
    find_all_possible_sequences(i, j+1, val+grid[i][j], sequence+[chr(ord('A')+j+i*5)])

grid = [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]
alphabet_grid = [[chr(ord('A')+i+j*5) for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        print(grid[i][j], end=' ')
    print()

start = input('Ready to start the game? (press "y" to continue) ')
if start == 'y':
    points = 0
    print('\n'*40)
    for i in range(5):
        for j in range(5):
            print(alphabet_grid[i][j], end=' ')
        print()
    k = random.randint(10, 99)
    possible_sequences = []
    entered_sequences = []
    correct_sequences = 0
    find_all_possible_sequences(0, 0, 0, [])
    if len(possible_sequences) != 0:
        while start == 'y':
            sequence = input(f'Find a sequence of letters that sums up to {k} (e.g ABCD)/Enter -1 to quit: ')
            if sequence == '-1':
                break
            sorted_sequence = sorted(sequence.upper())
            if sorted_sequence in possible_sequences and sorted_sequence not in entered_sequences:
                points += 1
                correct_sequences += 1
                entered_sequences.append(sorted(sequence.upper()))
            else:
                points -= 1
            if correct_sequences == len(possible_sequences):
                break
    possible_sequences = list(map(lambda x: ''.join(x), possible_sequences))
    print(f'Your got {points} points!')
    if len(possible_sequences) == 0:
        print(f'There are no possible sequences that sums up to {k}.')
    else:
        print(f'These are the possible sequences that sums up to {k}:')
        print(possible_sequences)
        
