input_val = int(input("Input number: "))
binary = []
new_val = input_val
iteration = 0

# To Find Max count for Binary position
while True: 
    exponent = iteration
    if 2 ** exponent <= new_val and 2 ** ( exponent + 1) > new_val:
        break

    iteration += 1    

counter = iteration


# To put 1 and 0's
while True:
    exponent = counter  
    
    if 2 ** exponent <= new_val and 2 ** ( exponent + 1) > new_val:
        binary.append('1')
        new_val = abs(new_val - (2 ** exponent))

    else: 
        binary.append('0')


    counter -= 1

    if counter < 0:
        break

print("".join(binary))
