try:
    with open('texts.txt', 'r') as reader:
        reader.readlines()
except:
    print("not open")
finally:
    print("cleaning all resources")
