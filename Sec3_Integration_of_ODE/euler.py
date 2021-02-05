##Bounds of the independent variable##

lower_bound = 0 
upper_bound = 2

##Initial Value##
y_0 = 0.5

##Step size or 'h' value##

step_size_h = 0.2

##Function of y'(t,y) ##

def Dy(t,y):
    ##Enter the function of y'(t,y) here
    return y - (t**2) + 1


##Don't change anything below this line##
print("========== Euler's Method ==========")
array = [y_0]
N = (upper_bound - lower_bound)/step_size_h

i = lower_bound
count = 1

while i<=upper_bound:
    i = float("{:.10f}".format(i))
    n = count - 1
    print("\ny_%i = y_%i + hf(t_%i,y_%i)" %(n+1,n,n,n))

    print("y_" + str(n+1) + " = " +
          str(array[n]) + " + " +
          str(step_size_h) + "*f(" +
          str(i) + "," + str(array[0]) + ")"
          )

    y_next = float("{:.10f}".format(array[n] + (step_size_h*Dy(i,array[n]))))
    print("y_" + str(n+1) + " = " +
          str(array[n]) + " + " +
          str(step_size_h) + "*" + str(Dy(i,array[n])) +
          " = " + str(y_next)
          )

    array.append(y_next)
    i += step_size_h
    count += 1
    

    
    
