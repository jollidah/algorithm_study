# 문자열 / 45m

import sys
input = sys.stdin.readline

def main(a, b):
    # A가 B에 포함된 경우
    if a in b:
        return 0

    # 길이가 같은 경우
    if len(a) == len(b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        return cnt
    
    diff = len(b) - len(a)

    total_cnt = 50

    # diff만큼 앞, 뒤에 붙는 모든 경우
    for i in range(diff + 1):
        front, back = i, diff - i
        cnt = 0
        
        if back == 0:
            new_a = b[:front] + a
        else:
            new_a = b[:front] + a + b[-back:]

        # 차이 카운트
        for idx in range(len(new_a)):
            if new_a[idx] != b[idx]:
                cnt += 1

        if total_cnt > cnt:
            total_cnt = cnt
            
        new_a = ""

    return total_cnt
    
if __name__ == '__main__':
    a, b = input().strip().split()
    print(main(a, b))