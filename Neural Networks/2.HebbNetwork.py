"""
----------Hebb network-------------
Initially w1=w2=b=0
w1new=w1old+x1t1
w2new=w2old+x2t2
bnew=bold+t1
wt1old=[] #weight1 old list
wt1new=[] #weight1 new list
"""
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
w1old,w2old,bold=0,0,0
w1new,w2new,bnew=0,0,0
wt1old=[]
wt1new=[]
wt2old=[]
wt2new=[]
bias_old=[]
bias_new=[]
classlabel_minus_1,classlabel_1=0,0
print(f"-----------Hebb Network Table For {gates[selection]} Gate----------")
print(f"{'x1':<8}{'x2':<8}{'t':<8}{'w1_old':<11}{'w2_old':<11}{'b_old':<11}{'w1_new':<11}{'w2_new':<11}{'b_new':<11}")
print("-" * 85)
for i in range(len(x1)):
    w1new=w1old+(x1[i]*t[selection][i])
    wt1old.append(w1old)
    w1old=w1new
    wt1new.append(w1new)
    
    w2new=w2old+(x2[i]*t[selection][i])
    wt2old.append(w2old)
    w2old=w2new
    wt2new.append(w2new)
    
    bnew=bold+t[selection][i]
    bias_old.append(bold)
    bold=bnew
    bias_new.append(bnew)
    print(f"{x1[i]:<8}{x2[i]:<8}{t[selection][i]:<8}{wt1old[i]:<11}{wt2old[i]:<11}{bias_old[i]:<11}{wt1new[i]:<11}{wt2new[i]:<11}{bias_new[i]:<11}")
    if t[selection][i]==-1:
        classlabel_minus_1+=1
    else:
        classlabel_1+=1
print(f"w1={w1new}, w2={w2new}, b={bnew}")
if classlabel_minus_1==classlabel_1:
    print("This Problem is NOT Linearly Seperable")
else:
    print("This Problem is Linearly Seperable")


    
