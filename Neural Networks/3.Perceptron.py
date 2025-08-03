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
else:
    t=[[1,-1,-1,-1],[1,1,1,-1],[-1,-1,1,-1],[-1,1,1,-1]]
    print("Bipolar Target Selected")
w1_old,w2_old,b_old=0,0,0
print(f"----------- Perceptron Network {gates[selection]} Gate ------------------")
theta=float(input("Enter Theta:"))
alpha=int(input("Enter Alpha:"))
result=0
Epoch=1
while True:
    if result==4:
        break
    result=0
    print("Epoch:",Epoch)
    print(f"{'x1':<5}{'x2':<5}{'t':<5}{'w1_old':<8}{'w2_old':<8}{'b_old':<8}{'yin':<7}{'Y':<5}{'CtY':<8}{'w1_new':<8}{'w2_new':<8}{'b_new':<8}")
    print("-" * 90)

    for i in range(4):
        yin=w1_old*x1[i]+w2_old*x2[i]+b_old
        if yin>theta:
            Y=1
        elif yin<-theta:
            Y=-1
        else:
            Y=0
        if Y==t[selection][i]:
            ctY="Y==t"
            print(f"{x1[i]:<5}{x2[i]:<5}{t[selection][i]:<5}{w1_old:<8}{w2_old:<8}{b_old:<8}{yin:<7}{Y:<5}{ctY:<8}{w1_new:<8}{w2_new:<8}{b_new:<8}")
            result+=1
        else:
            ctY="Y!=t"
            w1_new=w1_old+alpha*x1[i]*t[selection][i]
            w2_new=w2_old+alpha*x2[i]*t[selection][i]
            b_new=b_old+alpha*t[selection][i]
            print(f"{x1[i]:<5}{x2[i]:<5}{t[selection][i]:<5}{w1_old:<8}{w2_old:<8}{b_old:<8}{yin:<7}{Y:<5}{ctY:<8}{w1_new:<8}{w2_new:<8}{b_new:<8}")

            w1_old=w1_new
            w2_old=w2_new
            b_old=b_new
    Epoch+=1


