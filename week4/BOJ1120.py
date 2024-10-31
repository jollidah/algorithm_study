def same_chr(x, y):
    a = len(x)
    b = len(y)
    
    min_num = float('inf') # 이거 수정..한거
    
    for i in range(b-a+1): # 시작하는 인덱스 i
        cnt = 0
        for j in range(a): # element가 같은지 확인
            if y[i+j] != x[j]:
                cnt += 1
        if cnt < min_num:
            min_num = cnt
        
    return min_num
    

def main():
    A, B = input().split()
    
    print(same_chr(A, B))
    
if __name__=="__main__":
    main()
