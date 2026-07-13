
x_points=[90,	
85,	
80,	
75,	
70,	
65,	
60,	
55
]
y_points=[0.107,
0.105,
0.103,
0.1015,
0.1,
0.098,
0.0965,
0.0945
]
x_error =[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
y_error =[0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005,0.0005]
x_step  =0.01
y_step  =0.0001

iteration = 0

lengthx =int((2*x_error[-1])/x_step)
lengthy =int((2*y_error[-1])/y_step)
total =((lengthx**2)*(lengthy**2))
if total >1000000:
    if input("Warning, a lot of iterations. Type Y to continue or N to bail ").upper() == "N":
        raise Exception("Bail")
if total > 1000000:
    print("This may take a minute, ctr+c to cancel")
if total > 1000000000:
    raise Exception("Refuse, too many iterations")

largest=0
smallest_intercept=0
smallest=0
largest_intercept=0

x_movements = [(lengthx-2*i)*x_step for i in range(lengthx)]
y_movements = [(lengthy-2*i)*y_step for i in range(lengthy)]


def get_grad(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)
def get_y_intercept(x,y,gradient):
    return (y-gradient*x)
def get_y(x,gradient,intercept):
    return x*gradient +intercept
gradient = get_grad(x_points[0],x_points[-1],y_points[0],y_points[-1])
largest = gradient
smallest=gradient
try:
    for k in range(lengthx):
        print(f"{100*k/lengthx:.1f}%")
        for l in range(lengthx):
            
            for i in range(lengthy):
                for j in range(lengthy):
                    
                    gradient = get_grad(x_points[0]+x_movements[k],
                                        x_points[-1]+x_movements[l],
                                        y_points[0]+y_movements[i],
                                        y_points[-1]+y_movements[j])
                    if smallest <=gradient <= largest:
                        continue
                    intercept =get_y_intercept(x_points[-1]+x_movements[l],
                                            y_points[-1]+y_movements[j],gradient)
                    valid = True
                    for point in range(len(y_points)):
                        
                        y = get_y(x_points[point],gradient,intercept)
                        if y >y_points[point] + y_error[point]  or y < y_points[point] - y_error[point]:
                            valid = False
                            break
                    if valid:
                        if gradient > largest :
                            largest = gradient
                            smallest_intercept = intercept
                        elif gradient < smallest:
                            smallest = gradient
                            largest_intercept = intercept

    print("The highest gradient was",largest,".With a y intercept of",smallest_intercept)
    print("the smallest gradient was",smallest,".With a y intercept of",largest_intercept)  
    delta_g = (largest-smallest)/2
    print("Gradient uncertainty is +-",delta_g)

except KeyboardInterrupt:
    print("Cancelled by user")