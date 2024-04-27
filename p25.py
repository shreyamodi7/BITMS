def balaji(a,b):
    print("Bank balance is=",a+b)

test_dict={"fname":balaji,"age":50,"address":"salen"}

print("The original dictionary is"+str(test_dict))

res=test_dict['fname'](10,20)

#print("The required call result:"+str(res))

