def balaji():
    return "This is my bank balance"

test_dict={"fname":balaji,"age":50,"address":"salen"}

print("The original dictionary is"+str(test_dict))

res=test_dict['fname']()

print("The required call result:"+str(res))
