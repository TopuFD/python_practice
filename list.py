myList = ["apple","banana","cherry","nut",10,True]
print( "index '4' Item: ",myList[4],"\nmyList Length:",len(myList))
print("index 1 to index 3 item:",myList[:2])


color = ["red","green","yellow","blue","orange","green"]
newColor = ["violet","black"]

color.append("white")
color.extend(newColor)
color.insert(0,"blue")

print(color),

color = ["red","green","yellow","blue","orange","green"]
color.remove["red"] #remove certain item
color.pop(0), # remove index wise item
color.pop() #remove the last item
del color[0] #delete index wise item
del color #to delete the List
color.clear() # remove whole data of list





