import matplotlib.pyplot as plt
def math_func(x):
    return [i**2 for i in x] 

def math_func_der(x):
    return 2*x

def GradientDescent(starting_pt = 0, steps = 0, learning_rate = 0.1, min_step_size = 0.001):
    x = [starting_pt]
    x0 = starting_pt
    step_size = 0.1
    if steps > 0:
        for i in range(0,steps):
            step_size = learning_rate*math_func_der(x0)
            x1 = x0 - step_size
            x.append(x1)
            x0 = x1
            if step_size < min_step_size:
                break
            
    else: 
        while(step_size > min_step_size):
            step_size = learning_rate*math_func_der(x0)
            x1 = x0 - step_size
            x.append(x1)
            x0 = x1
    
    return x


x_vals = GradientDescent(starting_pt=2)
y_vals = math_func(x_vals)
#print("X:", x_vals)
#print("Y:", math_func(x_vals))
x_coords = [i/10.0 for i in range(-20,21)]
y_coords = math_func(x_coords)

plt.scatter(x_vals, y_vals)
plt.plot(x_coords, y_coords)
plt.show()