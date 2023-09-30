pin = '1d3455'

def VerificarPin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if str.isdigit(char) == False:
                return False
        return True
    else:
        return False

print(VerificarPin(pin))