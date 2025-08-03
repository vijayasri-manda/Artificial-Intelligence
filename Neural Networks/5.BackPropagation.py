import math
def sigmoid(x,selection):
    if selection==1:
        return 1 / (1 + math.exp(-x))
    elif selection==2:
        return (2/(1+ math.exp(-x)))-1
def Error(y,t,selection):
    if selection==1:
        return 0.5 * (t - y) ** 2
    elif selection==2:
        return 0.5 * (t - y) ** 2
selection=int(input("Enter 1:Binary 2:Bipolar: "))
x1=int(input("Enter x1:"))
x2=int(input("Enter x2:"))
t=int(input("Enter Target:"))
alpha=float(input("Enter Alpha:"))
print("-----------Enter weights and bias------------------")
v1,v2,b1=map(float,input("Enter v1,v2 and b1 for Hidden neuron 1:").split())
v3,v4,b2=map(float,input("Enter v3,v4 and b2 for Hidden neuron 2:").split())
w1,w2,b3=map(float,input("Enter w1,w2 and b3 for neuron Y:").split())
print("Binary Inputs Selected")
    #Forward Pass
z1in=v1*x1+v2*x2+b1
z1=sigmoid(z1in,selection)
z2in=v3*x1+v4*x2+b2
z2=sigmoid(z2in,selection)
yin=w1*z1+w2*z2+b3
y=sigmoid(yin,selection)
print("---------Forward Pass-----------")
print(f"zi1n = {z1in:.3f} \nz1 = {z1:.4f}\nz2in = {z2in:.3f}\nz2={z2:.4f}\nyin={yin:.4f}\ny = {y:.4f}")
    #Backward Pass
    #Error at Neuron Y
delta=(t-y)*y*(1-y) if selection==1 else (t-y)*0.5 * (1 + y) * (1 - y)
    #Error at Neuron Z1
delta1=(w1*delta)*z1*(1-z1) if selection==1 else 0.5*(w1*delta)* (1 + z1) * (1 - z1)
    #Error at Neuron Z2
delta2=(w2*delta)*z2*(1-z2) if selection==1 else 0.5*(w2*delta)*(1 + z2) * (1 - z2)
print("------------Backward Pass--------------")
print(f"deltaY={delta:.4f}\ndelta1={delta1:.4f}\ndelta2={delta2:.4f}")
    #Updating the Weights and Bias
w1_new=w1+(alpha*delta*z1)
w2_new=w2+(alpha*delta*z2)
b3_new=b3+(alpha*delta)
v1_new=v1+(alpha*delta1*x1)
v2_new=v2+(alpha*delta1*x2)
b1_new=b1+(alpha*delta1)
v3_new=v3+(alpha*delta2*x1)
v4_new=v4+(alpha*delta2*x2)
b2_new=b2+(alpha*delta2)
print(f"-----------Updated Weights and Bias-------------------")
print(f"w1_new={w1_new:.4f}\nw2_new={w2_new:.4f}\nb3_new={b3_new:.4f}\nv1_new={v1_new:.4f}\nv2_new={v2_new:.4f}\nb1_new={b1_new:.4f}\nv3_new={v3_new:.4f}\nv4_new={v4_new:.4f}\nb2_new={b2_new:.4f}")
