def solve(s):
    li=[]
    name=s.split(" ")
    for i in name:
        i=i.capitalize()
        li.append(i)
    return ' '.join(li)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
