def combi(index, combination, length):
    global count
    if len(combination) == length:
        print(combination)
        count+=1
        return
    if index>=len(data):
        return
    combi(index,combination+[data[index]],length)
    combi(index+1,combination,length)

count = 0
combination = []
data = [1,2,3,4,5]
combi(0,[],3)
print(count)

