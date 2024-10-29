def sum_seq(n, l):
    for i in range(l, 101):
        total_sum = (i*(i-1))//2 # 연속된 정수들의 합
        if (n-total_sum)%i == 0:
            x = (n-total_sum)//i
            if x>=0:
                result = [x+j for j in range(i)]
                print(' '.join(map(str, result)))
                return
    print(-1)


def main():
    N, L = map(int, input().split())
    sum_seq(N, L)

if __name__=="__main__":
    main()
