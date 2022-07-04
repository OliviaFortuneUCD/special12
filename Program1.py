#Here, we have created a customized and user-defined function
# that will make use of max() function and will compare the passed element with 0.0 which concludes it to be positive or negative.

#As val is a positive number, it returns 1.0. The variable val1 is a negative number thus it returns 0.0

#Return 0 if the input is negative otherwise return the input as it is.

#ReLU” means rectified linear unit


def ReLu(val):
    return max(0.0,val)
val = 1.0
print(ReLu(val))
val1 = -1.0
print(ReLu(val1))