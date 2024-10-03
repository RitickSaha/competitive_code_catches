score=[100,4,5,2,9]
books=[0,2,4,1,4]
sorte=sorted(books,key=lambda kv:(score[kv]),reverse=True)
print(sorte)