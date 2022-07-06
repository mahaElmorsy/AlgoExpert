def isValidSubsequence(array, sequence):
    elementIndex = 0
    for index,value in enumerate(sequence) :
        if index>1:
            if value == sequence[index-1]:
                if len(sequence)>len(array):
                    check=False
                    break
                else: 
                    sequence.remove(value)
                    continue
        if value not in array or array.count(value)<sequence.count(value):
            check= False
            break
        else :
            if value in array and array.index(value) >= elementIndex:
                elementIndex=array.index(value)
                check=True
            else:
                check=False
                break
            
        array.pop(0)
    return check
