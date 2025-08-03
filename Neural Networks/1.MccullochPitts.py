"""
--------Mcculloch Pitts Network------------
yin=w1x1+w2x2
stepfunction-->Activation Function
Y=f(x)=1 ,if yin>=0
          =0 ,if yin<0
compare Y&t
yins=yin summation

w1=1
w2=1
theta=2
"""
selection=int(input("Enter 0:AND 1:OR 2:AND NOT :"))#select the gate
gates={0:"AND",1:"OR",2:"AND NOT"}
x1=[1,1,0,0]
x2=[1,0,1,0]
t=[[1,0,0,0],[1,1,1,0],[0,1,0,0]]
yin=[]
Y=[]
result=0
ctY=[]
while True:
    if result==4:
        break
    result=0
    w1=int(input("Enter Weight1:"))
    w2=int(input("Enter Weight2:"))
    theta=int(input("Enter Theta:"))
    Y=[]
    ctY=[]
    yin=[]
    print(f"---------Mcculloch Table for {gates[selection]} Gate----------------------")
    print(f"{'x1':<9}{'x2':<9}{'t':<9}{'yin':<9}{'Y':<9}{'compare t&Y':<12}")
    print("-" * 60)
    for i in range(len(x1)):
        yins=((w1*x1[i])+(w2*x2[i]))
        yin.append(yins)
        if yin[i]>=theta:
            Y.append(1)
        else:
            Y.append(0)
        if t[selection][i]==Y[i]:
            result+=1
            ctY.append("t==Y")
        else:
            ctY.append("t!=Y")
        print(f"{x1[i]:<9}{x2[i]:<9}{t[selection][i]:<10}{yin[i]:<10}{Y[i]:<10}{ctY[i]:<14}")
    if result==4:
        print("All the 4 input target values are Equal to Y(output)")
    else:
        print("Try Another Iteration Until You get it! Give another Weights and Threshold Values")
    
    
