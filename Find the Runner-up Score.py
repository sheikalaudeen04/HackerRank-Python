if __name__ == '__main__':
    n = int(input())
    arr =map(int, input().split())
    new=sorted(list(set(arr)))
    print(new[-2])
        
    
