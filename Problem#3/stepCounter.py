'''
Name: Nathan Carr
Time: Thursday @ 2pm
'''
def feet_to_steps(user_feet):
   return int(user_feet / 2.5)

if __name__ == '__main__':
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))