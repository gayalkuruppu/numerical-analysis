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
    
    return function

###########################################################################################

##Don't change anything below this line##
from sympy import symbols, Eq, solve
print("========== Finding w0, w1 using RK4 Method ==========")

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

print("w_0 = " + str(y_0))
i = float("{:.10f}".format(i))

#Calculating k1
print("k1 = " +
      str(step_size_h) + "*f(" +
      str(i) + "," + str(array[-1]) + ")"
      " = " + str(step_size_h) + "*" + "{:.10f}".format(Dy(i,array[-1]))
      )
k1 = float("{:.10f}".format(step_size_h*Dy(i,array[-1])))
print("k1 = " + str(k1))

#Calculating k2
print("\nk2 = " +
      str(step_size_h) + "*f(" +
      str(i) + "+" + str(step_size_h/2) + "," +
      str(array[-1]) + "+" + str(k1/2) + ")"
      " = " + str(step_size_h) + "*" + "{:.10f}".format(Dy(i+(step_size_h/2),array[-1]+(k1/2)))
      )
k2 = float("{:.10f}".format(step_size_h*Dy(i+(step_size_h/2),array[-1]+(k1/2))))
print("k2 = " + str(k2))

#Calculating k3
print("\nk3 = " +
      str(step_size_h) + "*f(" +
      str(i) + "+" + str(step_size_h/2) + "," +
      str(array[-1]) + "+" + str(k2/2) + ")"
      " = " + str(step_size_h) + "*" + "{:.10f}".format(Dy(i+(step_size_h/2),array[-1]+(k2/2)))
      )
k3 = float("{:.10f}".format(step_size_h*Dy(i+(step_size_h/2),array[-1]+(k2/2))))
print("k3 = " + str(k3))

#Calculating k4
print("\nk4 = " +
      str(step_size_h) + "*f(" +
      str(i + step_size_h) + "," +
      str(array[-1]) + "+" + str(k3) + ")"
      " = " + str(step_size_h) + "*" + "{:.10f}".format(Dy(i+step_size_h,array[-1]+k3))
      )
k4 = float("{:.10f}".format(step_size_h*Dy(i+step_size_h,array[-1]+k3)))
print("k4 = " + str(k4))

print("\nw_" + str(count) + " = " +
      str(array[-1]) + " + (" + str(k1) +
      " + " + str(2*k2) + " + " + str(2*k3) + " + " + str(k4) + ")/6"
      )

y_next = float("{:.10f}".format(array[-1] + ((k1+(2*k2)+(2*k3)+k4)/6)))
print("w_" + str(count) + " = " + str(y_next) + "\n")

array.append(y_next)
i += step_size_h
count += 1
print("========== Finding w_i for i=2,3,.. ==========")
while i<upper_bound:
    wi_1 = symbols("w" + str(count))
    i = float("{:.10f}".format(i))
    i_1 = float("{:.10f}".format(i-step_size_h))
    ip1 = float("{:.10f}".format(i+step_size_h))
    ans = float("{:.10f}".format(solve(wi_1-array[-1]-
                (step_size_h*((5*Dy(ip1,wi_1)) +
                              (8*Dy(i,array[-1])) -
                              Dy(i_1,array[-2]))/12))[0]))
    

    print("\nw" + str(count) + " = " +
          str(array[-1]) + " + " + str(step_size_h) + "[5f(" +
          str(ip1) + ", " + str(wi_1) + ") + 8f(" +
          str(i) + ", " + str(array[-1]) + ") - f(" +
          str(i_1) + ", " + str(array[-2])+ ")]/12")
    
    print("w" + str(count) + " = " +
          str(array[-1]) + " + " + str(step_size_h) + "(" +
          str(5*Dy(ip1,wi_1)) + " + " + "{:.10f}".format(8*Dy(i,array[-1])) +
          " - " + "{:.10f}".format(Dy(i_1,array[-2])) + ")/12")
    print("w" + str(count) + " = " + str(ans))

    array.append(ans)
    i += step_size_h
    count += 1
    

    
    
