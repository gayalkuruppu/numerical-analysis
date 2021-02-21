from sympy import symbols, Eq, solve
import math

# u1 = f(t, u1, u2)
# u2 = g(t, u1, u2)

# u1 = y and u2 = y' (always)


##Bounds of the independent variable##

lower_bound = 1
upper_bound = 1.2

##Step size or 'h' value##

h = 0.1

## functions for u1 and u2, (f, g respectively)

def f(x,u1,u2):
    return u2

def g(x,u1,u2):
    return ((-2*u2/x) + (2*u1/x**2) + (math.sin(math.log(x))/x**2))

## initial values

u1_0 = 1
u2_0 = 0

## Don't change anything after this line
###########################################################################################
from tabulate import tabulate

print("========== Applying RK4 ==========")
print("K will represent values for u1, k will represent values for u2")

print("\nK_1 = hf(t_n,u1_n,u2_n)"
      "\nK_2 = hf(t_n + h/2, u1_n + K_1/2, u2_n + k_1/2)"
      "\nK_3 = hf(t_n + h/2, u1_n + K_2/2, u2_n + k_2/2)"
      "\nK_4 = hf(t_n+1, u1_n + K_3, u2_n + k_3)"
      "\nu1_n+1 = u1_n + (K_1 + 2K_2 + 2K_3 + K_4)/6"
      "\nwhere,"
      "\nk_1 = hg(t_n,u1_n,u2_n)"
      "\nk_2 = hg(t_n + h/2, u1_n + K_1/2, u2_n + k_1/2)"
      "\nk_3 = hg(t_n + h/2, u1_n + K_2/2, u2_n + k_2/2)"
      "\nk_4 = hg(t_n+1, u1_n + K_3, u2_n + k_3)"
      "\nu2_n+1 = u2_n + (k_1 + 2k_2 + 2k_3 + k_4)/6"
      )

u1_arr = [u1_0]
u2_arr = [u2_0]

i = lower_bound
count = 1

while i<upper_bound:
    print("\nIteration %i," %(count))
    i = float("{:.10f}".format(i))
    ##K1, k1
    K1_func = "K1 = " + str(h) + "*f(" + str(i) + ", " + str(u1_arr[-1]) + ", " + str(u2_arr[-1])+ ")"

    K1_mid = "K1 = " + str(h) + "*" + "{:.10f}".format(f(i, u1_arr[-1], u2_arr[-1]))
    K1_ans = "K1 = " + "{:.10f}".format(h*f(i, u1_arr[-1], u2_arr[-1]))

    K1 = float("{:.10f}".format(h*f(i, u1_arr[-1], u2_arr[-1])))

    k1_func = "k1 = " +str(h) + "*g(" +str(i) + ", " + str(u1_arr[-1]) + ", " + str(u2_arr[-1])+ ")"

    k1_mid = "k1 = " + str(h) + "*" + "{:.10f}".format(g(i, u1_arr[-1], u2_arr[-1]))
    k1_ans = "k1 = " + "{:.10f}".format(h*g(i, u1_arr[-1], u2_arr[-1]))

    k1 = float("{:.10f}".format(h*g(i, u1_arr[-1], u2_arr[-1])))

    ##K2, k2

    K2_func = "K2 = " + str(h) + "*f(" +"{:.10f}".format(i + (h/2)) + ", " +"{:.10f}".format(u1_arr[-1] + (K1/2)) + ", " +"{:.10f}".format(u2_arr[-1] + (k1/2))+ ")"

    K2_mid = "K2 = " + str(h) + "*" +"{:.10f}".format(f(float("{:.10f}".format(i + (h/2))),
                                                                  float("{:.10f}".format(u1_arr[-1] + (K1/2))),
                                                                  float("{:.10f}".format(u2_arr[-1] + (k1/2)))))
                     
    K2_ans = "K2 = " + "{:.10f}".format(h*f(float("{:.10f}".format(i + (h/2))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K1/2))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k1/2)))))

    K2 = float("{:.10f}".format(h*f(
        float("{:.10f}".format(i + (h/2))),
        float("{:.10f}".format(u1_arr[-1] + (K1/2))),
        float("{:.10f}".format(u2_arr[-1] + (k1/2))))))


    k2_func = "k2 = " +str(h) + "*g(" +"{:.10f}".format(i + (h/2)) + ", " +"{:.10f}".format(u1_arr[-1] + (K1/2)) + ", " +"{:.10f}".format(u2_arr[-1] + (k1/2))+ ")"

    k2_mid = "k2 = " + str(h) + "*" +"{:.10f}".format(g(float("{:.10f}".format(i + (h/2))),
                       float("{:.10f}".format(u1_arr[-1] + (K1/2))),
                     float("{:.10f}".format(u2_arr[-1] + (k1/2)))))
                     
    k2_ans = "k2 = " + "{:.10f}".format(h*g(float("{:.10f}".format(i + (h/2))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K1/2))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k1/2)))))

    k2 = float("{:.10f}".format(h*g(
        float("{:.10f}".format(i + (h/2))),
        float("{:.10f}".format(u1_arr[-1] + (K1/2))),
        float("{:.10f}".format(u2_arr[-1] + (k1/2))))))

    ##K3, k3

    K3_func = "K3 = " +str(h) + "*f(" +"{:.10f}".format(i + (h/2)) + ", " +"{:.10f}".format(u1_arr[-1] + (K2/2)) + ", " +"{:.10f}".format(u2_arr[-1] + (k2/2))+ ")"

    K3_mid = "K3 = " + str(h) + "*" +"{:.10f}".format(f(float("{:.10f}".format(i + (h/2))),
                       float("{:.10f}".format(u1_arr[-1] + (K2/2))),
                     float("{:.10f}".format(u2_arr[-1] + (k2/2)))))
                     
    K3_ans = "K3 = " + "{:.10f}".format(h*f(float("{:.10f}".format(i + (h/2))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K2/2))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k2/2)))))

    K3 = float("{:.10f}".format(h*f(
        float("{:.10f}".format(i + (h/2))),
        float("{:.10f}".format(u1_arr[-1] + (K2/2))),
        float("{:.10f}".format(u2_arr[-1] + (k2/2))))))

    k3_func = "k3 = " +str(h) + "*g(" +"{:.10f}".format(i + (h/2)) + ", " +"{:.10f}".format(u1_arr[-1] + (K2/2)) + ", " +"{:.10f}".format(u2_arr[-1] + (k2/2))+ ")"

    k3_mid = "k3 = " + str(h) + "*" +"{:.10f}".format(g(float("{:.10f}".format(i + (h/2))),
                       float("{:.10f}".format(u1_arr[-1] + (K2/2))),
                     float("{:.10f}".format(u2_arr[-1] + (k2/2)))))
                     
    k3_ans = "k3 = " + "{:.10f}".format(h*g(float("{:.10f}".format(i + (h/2))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K2/2))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k2/2)))))

    k3 = float("{:.10f}".format(h*g(
        float("{:.10f}".format(i + (h/2))),
        float("{:.10f}".format(u1_arr[-1] + (K2/2))),
        float("{:.10f}".format(u2_arr[-1] + (k2/2))))))

    ##K4, k4

    K4_func = "K4 = " +str(h) + "*f(" +"{:.10f}".format(i + h) + ", " +"{:.10f}".format(u1_arr[-1] + (K3)) + ", " +"{:.10f}".format(u2_arr[-1] + (k3))+ ")"

    K4_mid = "K4 = " + str(h) + "*" +"{:.10f}".format(f(float("{:.10f}".format(i + (h))),
                       float("{:.10f}".format(u1_arr[-1] + (K3))),
                     float("{:.10f}".format(u2_arr[-1] + (k3)))))
                     
    K4_ans = "K4 = " + "{:.10f}".format(h*f(float("{:.10f}".format(i + (h))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K3))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k3)))))

    K4 = float("{:.10f}".format(h*f(
        float("{:.10f}".format(i + (h))),
        float("{:.10f}".format(u1_arr[-1] + (K3))),
        float("{:.10f}".format(u2_arr[-1] + (k3))))))

    k4_func = "k4 = " +str(h) + "*g(" +"{:.10f}".format(i + h) + ", " +"{:.10f}".format(u1_arr[-1] + (K3)) + ", " +"{:.10f}".format(u2_arr[-1] + (k3))+ ")"

    k4_mid = "k4 = " + str(h) + "*" +"{:.10f}".format(g(float("{:.10f}".format(i + (h))),
                       float("{:.10f}".format(u1_arr[-1] + (K3))),
                     float("{:.10f}".format(u2_arr[-1] + (k3)))))
                     
    k4_ans = "k4 = " + "{:.10f}".format(h*g(float("{:.10f}".format(i + (h))),
                                                      float("{:.10f}".format(u1_arr[-1] + (K3))),
                                                      float("{:.10f}".format(u2_arr[-1] + (k3)))))

    k4 = float("{:.10f}".format(h*g(
        float("{:.10f}".format(i + (h))),
        float("{:.10f}".format(u1_arr[-1] + (K3))),
        float("{:.10f}".format(u2_arr[-1] + (k3))))))

    u1_func = "u1," + str(count) + " = " + str(u1_arr[-1]) + " + (" + str(K1) + " + " + str(2*K2) + " + " + str(2*K3) + " + " + str(K4) + ")/6)"

    u2_func = "u2," + str(count) + " = " + str(u2_arr[-1]) + " + (" + str(k1) + " + " + str(2*k2) + " + " + str(2*k3) + " + " + str(k4) + ")/6)"

    u1_ans = "u1," + str(count) + " = " + "{:.10f}".format(u1_arr[-1] + ((K1+(2*K2)+(2*K3)+K4)/6))
    u2_ans = "u2," + str(count) + " = " + "{:.10f}".format(u2_arr[-1] + ((k1+(2*k2)+(2*k3)+k4)/6))

    U1 = float("{:.10f}".format(u1_arr[-1] + ((K1+(2*K2)+(2*K3)+K4)/6)))
    U2 = float("{:.10f}".format(u2_arr[-1] + ((k1+(2*k2)+(2*k3)+k4)/6)))

    u1_arr.append(U1)
    u2_arr.append(U2)
    i += h
    count += 1

    data1 = [[K1_func, k1_func], [K1_mid, k1_mid], [K1_ans, k1_ans]]
    data2 = [[K2_func, k2_func], [K2_mid, k2_mid], [K2_ans, k2_ans]]
    data3 = [[K3_func, k3_func], [K3_mid, k3_mid], [K3_ans, k3_ans]]
    data4 = [[K4_func, k4_func], [K4_mid, k4_mid], [K4_ans, k4_ans]]

    dataU = [[u1_func, u2_func], [u1_ans, u2_ans]]

    print(tabulate(data1))
    print("\n")
    print(tabulate(data2))
    print("\n")
    print(tabulate(data3))
    print("\n")
    print(tabulate(data4))
    print("\n")
    print(tabulate(dataU))
    print("\n")

    
        
    































    

