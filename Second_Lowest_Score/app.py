if __name__ == '__main__':
    
    lis=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis.append([name,score])
    
    scores=sorted(set([student[1] for student in lis]))
    second_lowest=scores[1]
    names=[student[0] for student in lis if student[1]==second_lowest]
    
    for name in sorted(names):
        print(name)
