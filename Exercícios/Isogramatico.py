msg = 'tesza'

def isogram(msg):
    for char in msg:
        if msg.count(char) > 1:
            return False
    return True

print(isogram(msg))