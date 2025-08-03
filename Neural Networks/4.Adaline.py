selection=int(input("Enter 0:AND 1:OR 2:ANDNOT 3:XOR :"))
gates={0:"AND",1:"OR",2:"AND NOT",3:"XOR"}
Input=int(input("Enter 0:Binary Inputs  1:Bipolar Inputs:"))
target=int(input("Enter 0:Binary Target 1:Bipolar Target:"))
if Input==1:
    x1=[1,-1,1,-1]
    x2=[1,1,-1,-1]
    print("Bipolar Inputs Selected")
else:
    x1=[1,0,1,0]
    x2=[1,1,0,0]
    print("Binary Inputs Selected")
if target==0:
    t=[[1,0,0,0],[1,1,1,0],[0,1,0,0],[1,0,1,0]]
    print("Binary Target Selected")
else:
    t=[[1,-1,-1,-1],[1,1,1,-1],[-1,-1,1,-1],[-1,1,1,-1]]
    print("Bipolar Target Selected")
w1_old,w2_old,b_old=0.1,0.1,0.1
MSE=0
Epoch=int(input("Enter No.of epochs"))
alpha=float(input("Enter Alpha"))
iteration=1
print(f"---------ADALINE NETWORK for {gates[selection]} Gate------------")
while(iteration<=Epoch):
    print("Epoch:",iteration)
    MSE=0
    print(f"{'x1':<4} {'x2':<4} {'t':<4} {'w1_old':<11} {'w2_old':<11} {'b_old':<11} {'yin':<11} {'error':<11} {'w1_new':<11} {'w2_new':<11} {'b_new':<11} {'sq_error':<11}")

    for i in range(4):
        yin = w1_old * x1[i] + w2_old * x2[i] + b_old
        error = t[selection][i] - yin
        w1_new = w1_old + alpha * error * x1[i]
        
        w2_new = w2_old + alpha * error * x2[i]
        b_new = b_old + alpha * error
        squared_Error = error * error
        MSE+=squared_Error
        print(f"{x1[i]:<4} {x2[i]:<4} {t[selection][i]:<4} {w1_old:<11.3f} {w2_old:<11.3f} {b_old:<11.3f} {yin:<11.3f} {error:<11.3f} {w1_new:<11.3f} {w2_new:<11.3f} {b_new:<11.3f} {squared_Error:<11.3f}")
        w1_old=w1_new
        w2_old=w2_new
        b_old=b_new
    MSE=MSE/4
    print(f"Mean Square Error For Epoch{Epoch} is: {MSE:.4f}")
    iteration+=1

        
        
        
        
    
    
