# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# SIERPINSKI TRIANGLE

# %%
import matplotlib.pyplot as plt
import random

def trans1(p):
    a=p[0]
    b=p[1]
    a1=0.5*a
    b1=0.5*b
    
    return a1,b1
def trans2(p):
    a=p[0]
    b=p[1]
    a1=0.5*a+0.5
    b1=0.5*b+0.5
    return a1,b1
def trans3(p):
    a=p[0]
    b=p[1]
    a1=0.5*a+1
    b1=0.5*b
    return a1,b1
        


# %%
transformations=[trans1,trans2,trans3]
a1=[]
b1=[]
a,b=0,0 


# %%
for i in range(1,100000):
    tran=random.choice(transformations)
    a,b=tran((a,b))
    a1.append(a)
    b1.append(b)


# %%
plt.rc("figure",figsize=(16,10))
plt.plot(a1,b1,"o")
plt.show


# %%


