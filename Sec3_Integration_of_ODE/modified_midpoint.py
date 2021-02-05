from tabulate import tabulate
##Bounds of the independent variable##

lower_bound = 0 
upper_bound = 2

##Initial Value##
y_0 = 0.5

##Step size or 'h' value##

step_size_h = 0.2
sub_steps = 2        ##Number of sub-steps

##Function of y'(t,y) ##

def Dy(t,y):
    ##Enter the function of y'(t,y) here
    function = y - (t**2) + 1
    
    return float("{:.10f}".format(function))

###########################################################################################

##Don't change anything below this line##
print("========== Modified Midpoint Method ==========")

print("\nw_0 = y_k"
      "\nw_1 = w_0 + h_n*f(x_k,w_0)"
      "\nw_(m+1) = w_(m-1) + 2h_n*f(x_k+mh_n, w_m)"
      "\ny_(k+1) = (w_n + w_(n-1) + h_n*f(x_k + h, w_n))/2"
      )

print("\nApplying the above equations,")

h_n = step_size_h/sub_steps
array = [y_0]
N = (upper_bound - lower_bound)/step_size_h

i = lower_bound
count = 1

while i<upper_bound:
    i = float("{:.10f}".format(i))
    print("\n======== Iteration %i ========" %(count))

    k = count - 1
    
    #calculating w_0
    w_0 = array[-1]
    print("\nw_0 = y_" + str(k) + " = " + str(w_0))

    #calculating w_1
    w_1 = float("{:.10f}".format(w_0 + (h_n*Dy(i, w_0))))
    print("\nw_1 = " + str(w_0) + " + " + str(h_n) + "*f(" + str(i) + "," + str(w_0) + ")")
    print("w_1 = " + str(w_0) + " + " + str(h_n) + "*" + str(Dy(i, w_0)) + " = " + str(w_1)
          + "\n")

    sub_arr = [w_0, w_1]
    
    #calculating w_m
    for m in range(1,sub_steps):
        w_m1 = float("{:.10f}".format(sub_arr[-2] + (2*h_n*Dy(i+(m*h_n), sub_arr[-1]))))
        print(tabulate([["w_" + str(m+1), "=", str(sub_arr[-2]) +
              " + 2*" + str(h_n) + "*f(" +
              str(i) + "+(" + str(m) + "*" + str(h_n) + ")," + str(sub_arr[-1]) + ")","=", w_m1]],
                       tablefmt='plain'
                       ))
        sub_arr.append(w_m1)

    #calculating y_(k+1)
    yk_1 = float("{:.10f}".format((sub_arr[-1] + sub_arr[-2] + (h_n*Dy(i + step_size_h, sub_arr[-1])))/2))
    print(tabulate([["y_" + str(k+1),"=","(" + str(sub_arr[-1]) +
                    "+" + str(sub_arr[-2]) + "+" +
                    str(h_n) + "*" + str(Dy(i + step_size_h, sub_arr[-1])) + ")/2", "=", yk_1
        ]],tablefmt='plain'))

    array.append(yk_1)
    count += 1
    i += step_size_h
        
            
              
    

    
    
