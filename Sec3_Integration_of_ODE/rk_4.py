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
    function = y - (t**2) + 1
    
    return float("{:.10f}".format(function))

###########################################################################################

##Don't change anything below this line##
print("========== RK4 Method ==========")

print("\nk_1 = hf(x_n,y_n)"
      "\nk_2 = hf(x_n + h/2, y_n + k_1/2)"
      "\nk_3 = hf(x_n + h/2, y_n + k_2/2)"
      "\nk_4 = hf(x_n+1, y_n + k_3)"
      "\ny_n+1 = y_n + (k_1 + 2k_2 + 2k_3 + k_4)/6"
      )

print("\nApplying the above equations,")

array = [y_0]
N = (upper_bound - lower_bound)/step_size_h

i = lower_bound
count = 1

while i<upper_bound:
    print("\nIteration %i," %(count))
    i = float("{:.10f}".format(i))
    n = count - 1

    #Calculating k1
    print("k1 = " +
          str(step_size_h) + "*f(" +
          str(i) + "," + str(array[n]) + ")"
          " = " + str(step_size_h) + "*" + str(Dy(i,array[n]))
          )
    k1 = float("{:.10f}".format(step_size_h*Dy(i,array[n])))
    print("k1 = " + str(k1))

    #Calculating k2
    print("\nk2 = " +
          str(step_size_h) + "*f(" +
          str(i) + "+" + str(step_size_h/2) + "," +
          str(array[n]) + "+" + str(k1/2) + ")"
          " = " + str(step_size_h) + "*" + str(Dy(i+(step_size_h/2),array[n]+(k1/2)))
          )
    k2 = float("{:.10f}".format(step_size_h*Dy(i+(step_size_h/2),array[n]+(k1/2))))
    print("k2 = " + str(k2))

    #Calculating k3
    print("\nk3 = " +
          str(step_size_h) + "*f(" +
          str(i) + "+" + str(step_size_h/2) + "," +
          str(array[n]) + "+" + str(k2/2) + ")"
          " = " + str(step_size_h) + "*" + str(Dy(i+(step_size_h/2),array[n]+(k2/2)))
          )
    k3 = float("{:.10f}".format(step_size_h*Dy(i+(step_size_h/2),array[n]+(k2/2))))
    print("k3 = " + str(k3))

    #Calculating k4
    print("\nk4 = " +
          str(step_size_h) + "*f(" +
          str(i + step_size_h) + "," +
          str(array[n]) + "+" + str(k3) + ")"
          " = " + str(step_size_h) + "*" + str(Dy(i+step_size_h,array[n]+k3))
          )
    k4 = float("{:.10f}".format(step_size_h*Dy(i+step_size_h,array[n]+k3)))
    print("k4 = " + str(k4))
    
    print("\ny_" + str(n+1) + " = " +
          str(array[n]) + " + (" + str(k1) +
          " + " + str(2*k2) + " + " + str(2*k3) + " + " + str(k4) + ")/6"
          )

    y_next = float("{:.10f}".format(array[n] + ((k1+(2*k2)+(2*k3)+k4)/6)))
    print("y_" + str(n+1) + " = " + str(y_next) + "\n")

    array.append(y_next)
    i += step_size_h
    count += 1
    

    
    
