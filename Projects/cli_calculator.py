input_nums = []
list_symbols = ['+', '-', '/' , 'x' ,'=']
input_syms = []
flag = False
cur_result = 0
prev_result = 0
result_history = []

while True:

    if flag == False:
        input_nums.append(float(input("Input number: "))) 
        print("""
            + ( addition )
            - ( difference )
            / ( quotient )
            x ( multiplication )
            = ( result )
        """)
        input_syms.append(str(input("Input Symbol: ")))
        prev_result = input_nums[0]

    if flag: 
        input_syms.append(str(input("Input Symbol: ")))

        if "=" not in input_syms and flag:
            input_nums.append(float(input("Input number: ")))


    if "=" in input_syms: 
        for x in range(len(input_syms)):
            if input_syms[x] == '+' and flag == False:
                cur_result = prev_result + input_nums[x + 1 ]  
            if input_syms[x] == '+' and flag == True:
                cur_result = prev_result + input_nums[x]    


            prev_result = cur_result
            result_history.append(prev_result)  
            x += 1

        input_nums = []
        input_syms = []
        flag = True
        print(result_history[-1])

        






