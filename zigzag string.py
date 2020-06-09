A = "PAYPALISHIRING"
B = 3

# Corner Case (Only one row) 
if B == 1: 
    print(A)      

# Find length of string 
l = len(A) 

# Create an array of  
# strings for all n rows 
arr=["" for x in range(l)]

# Initialize index for  
# array of strings arr[] 
row = 0
  
# Travers through 
# given string 
for i in range(l): 
      
    # append current character 
    # to current row 
    arr[row] += A[i] 

    # If last row is reached,  
    # change direction to 'up' 
    if row == B - 1: 
        down = False

    # If 1st row is reached, 
    # change direction to 'down' 
    elif row == 0: 
        down = True

    # If direction is down,  
    # increment, else decrement 
    if down: 
        row += 1
    else: 
        row -= 1

# Print concatenation 
# of all rows 
# for i in range(B): 
#     print(arr[i]

print arr

print "".join(arr)

