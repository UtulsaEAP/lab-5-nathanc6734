'''
Name: Nathan Carr
Time: Thursday @ 2pm
'''
def swap_values(user_val1, user_val2, user_val3, user_val4):   
   val1 = user_val1
   val3 = user_val3
   
   user_val1 = user_val2
   user_val2 = val1
   user_val3 = user_val4
   user_val4 = val3
   
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   values = swap_values(user_input1, user_input2, user_input3, user_input4)
   print(values)

 