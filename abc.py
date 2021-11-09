def break_into_words(sentence):
    list=[]
    i=0
    a=""
    while i<len(sentence):
        if sentence[i]==" ":
        	list.append(a)
        	a=""
        else:
        	a=a+sentence[i]
        i=i+1
    if a:
    	list.append(a)
    	return list
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
print(break_into_words(sentence))