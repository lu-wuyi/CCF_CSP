S = input()
capital = int(input())
N = int(input())

answer = []
for i in range(N):
    check = input()
    if not capital:
        S = S.casefold()  #使用lower方法应该更好， 将S小写化应该放在循环外
        CHECK = check.casefold()
    else:
        CHECK = check
    if S in CHECK:#对于字符串可以直接用 S in check
        answer.append(check)
        
for i in answer:
    print(i)
