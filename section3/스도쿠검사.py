# 스도쿠는 매우 간단한 숫자 퍼즐이다.
# 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9 개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다.
#
# 예를 들어 다음을 보자.
#
# 위 그림은 스도쿠를 정확하게 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고,
# 각 3×3짜리 사각형(9개이며, 위에서 색 깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
# 완성된 9×9 크기의 수도쿠가 주어지면 정확하게 풀었으면 "YES", 잘 못 풀었으면 "NO"를 출 력하는 프로그램을 작성하세요.

# ▣ 입력설명
# 첫 번째 줄에 완성된 9×9 스도쿠가 주어집니다.
# ▣ 출력설명
# 첫째 줄에 “YES" 또는 ”NO"를 출력하세요.


import sys

sys.stdin = open("스도쿠검사.txt","rt")

lst = [list(map(int,input().split())) for _ in range(9)]
def sdkCheck():# 내방식
    rec1, rec2, rec3 = None, None, None
    for i in range(9):
        row = set()
        col = set()
        if i % 3 == 0:
            rec1 = set()
            rec2 = set()
            rec3 = set()
        for j in range(9):
            row.add(lst[i][j])
            col.add(lst[j][i])
            if j <= 2:
                rec1.add(lst[i][j])
            elif j >= 3 and j <= 5:
                rec2.add(lst[i][j])
            else:
                rec3.add(lst[i][j])
        if len(row) < 9 or len(col) < 9:
            return False
        if i % 3 == 2:
            if len(rec1) < 9 or len(rec2) < 9 or len(rec3) < 9:
                return False

    return True

def sdkCheck2(): #강의방식
    for i in range(9):
        chk1 = [0]*10
        chk2 = [0]*10
        for j in range(9):
            chk1[lst[i][j]] = 1
            chk2[lst[j][i]] = 1
        if sum(chk1) < 9 or sum(chk2) < 9:
            return False

    for i in range(3):
        for j in range(3):
            chk3 = [0]*10
            for k in range(3):
                for s in range(3):
                    chk3[lst[i*3+k][j*3+s]] = 1
            if sum(chk3) < 9:
                return False

    return True

if sdkCheck2():
    print("YES")
else:
    print("NO")



