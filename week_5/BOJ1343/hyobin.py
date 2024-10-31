board = input()
answer = []
idx = 0

while idx < len(board):
    if board[idx:idx + 4]=='XXXX':
        answer.append('AAAA')
        idx += 4
        
    elif board[idx:idx + 2]=='XX':
        answer.append('BB')
        idx += 2
        
    elif board[idx]=='X':
        answer = ['-1']
        break
    
    else :
        answer.append(board[idx])
        idx += 1

print(''.join(answer))