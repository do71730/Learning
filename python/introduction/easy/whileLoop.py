if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    
    i = 0
    while i < n:
        arr.append(i)
        i += 1
        
    i = 0
    while i < n:
        print((arr[i] * arr[i]))
        i += 1
