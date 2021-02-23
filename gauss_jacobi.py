'''
10x1 – x2  + 2x3 = 6
–x1 + 11x2  –  x3  + 3x4 = 25
2x1 – x2  + 10x3  – x4 = –11
3x2  – x3  + 8x4 = 15
'''

def find_solution(A,b,new_x,n):
    converge = True
    old_x = []
    while converge:
        old_x = new_x[:]
        for i in range(n):
            sm = 0.0
            for j in range(n):
                if i!=j:
                    sm = sm + A[i][j]*old_x[j]
            new_x[i] = (b[i] - sm)/A[i][i]
        print('%0.4f\t%0.4f\t%0.4f\t%0.4f'%(new_x[0],new_x[1],new_x[2],new_x[3]))
        if new_x[0]>999999 or new_x[0]<-999999:
            print("diverging.....")
            break
        for i in range(n):
            converge = converge and (abs(new_x[i]-old_x[i])>0.0001)


if __name__=="__main__":
    A = [[10, -1, 2, 0],[-1, 11, -1, 3],[2, -1, 10, -1],[0, 3, -1, 8]]
    b = [6, 25, -11, 15]
    X = [0.0, 0.0, 0.0, 0.0]
    X = find_solution(A,b,X,len(A))
