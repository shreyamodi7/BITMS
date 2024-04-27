d={'A':1,'B':2,'C':3}
key=input("Enter key to check")
if key in d.keys():
    print("key is present\n value of the key is:",d[key])
    #print(d[key])
else:
    print("key isnt present")