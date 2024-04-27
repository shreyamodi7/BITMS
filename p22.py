file_parh="balaji.txt"
try:
    with open(fil_path,'r')as file:
        content=file.read()
        print(content)
        

except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("An error occured:{e}")
finally:
    print("closing the file")