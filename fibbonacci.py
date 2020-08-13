
#Function to output the Fibbonacci sequence of a given number
def fibbonacci(given_num):
    a = 0
    b = 1
    sum = 0
    count = 1
    while(count <= given_num):
        print(sum, end = " ")
        count += 1
        a = b
        b = sum
        sum = a + b



#Prompt user for number
n = int(input("Enter the value of n = "))

#Output format
print("Fibbonacci Series: ", end = " ")
fibbonacci(n)

