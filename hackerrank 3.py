if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
second_highest = sorted(set([score for name, score in l]))[1]
print('\n'.join(sorted([name for name, score in l if score == second_highest])))
        
