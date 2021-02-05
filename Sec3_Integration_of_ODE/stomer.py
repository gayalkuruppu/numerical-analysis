from tabulate import tabulate
##Bounds of the independent variable##

lower_bound = 0 
upper_bound = 2

##Initial Value##
y_0 = 0.5
y_dash_0 = 0.5

##Step size or 'h' value##

step_size_h = 0.2

##Function of y''(t,y) ##

def Dy(t,y):
    ##Enter the function of y''(t,y) here
    function = y - (t**2) + 1
    
    return float("{:.10f}".format(function))

###########################################################################################

##Don't change anything below this line##
print("========== RK4 Method ==========")

print("\ny_1 = y_0 + h[y'_0 + f(x0,y0)/2]"
      "\ny_(k+1) - 2y_k + y_(k-1) = h^2*f(x0+kh,y_k)")

print("\nApplying the above equations,")

#calculating y_1
y_1 = float("{:.10f}".format(y_0 + (step_size_h*(y_dash_0 + (Dy(lower_bound,y_0)/2)))))
print(tabulate([["y_1","=",
                str(y_0) + " + " + str(step_size_h) +
                "*[" + str(y_dash_0)+ " + (f" +
                str(lower_bound) + "," + str(y_0) + ")/2]","=", str(y_1)]],tablefmt='plain'))
print("")
array = [y_0, y_1]
N = round((upper_bound - lower_bound)/step_size_h)
ans= []
for k in range(1,N):
    yk_1 = float("{:.10f}".format(
        (2*array[-1])-array[-2] + ((step_size_h**2)*Dy(lower_bound + (k*step_size_h),
                                                       array[-1]))))
    ans.append(["y_" + str(k+1) + "-2*" + str(array[-1]) +
                     "+" + str(array[-2]), "=", str(float("{:.10f}".format(step_size_h**2))) + "f(" +
                     str(lower_bound) + "+" + str(float("{:.10f}".format(k*step_size_h))) +
                     "," + str(array[-1]) + "),", "y" + str(k+1) + " = " + str(yk_1)])
    
    ans.append([None, None, None, None])
    array.append(yk_1)

print(tabulate(ans,tablefmt='plain'))
    

    
    
