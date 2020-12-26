#!/usr/bin/env python
# coding: utf-8

# # 2I

# In[1]:


from sympy.solvers import solve
from sympy.core import sympify
ans=solve(sympify('Eq((x+2)*(x-3),(x-5)*(x-6))'))
print('The solve to the question is:',ans)


# # 3C

# In[2]:


import math
from sympy.solvers import solve
from sympy import Symbol
x=Symbol('x')
key=solve([10-2*x-6],list=False)
ans=math.fabs(key[x])
print('The solve to the question is:',ans)


# # 3C-聯立方程式求解

# In[3]:


#4*x+3*y-4,2*x+2*y-2*z-0,5*x+3*y+z+2
eq1=input('enter an equation:')
eq2=input('enter an equation:')
eq3=input('enter an equation:')
from sympy.solvers import solve
from sympy import symbols
x,y,z=symbols('x,y,z')
ans=solve([eq1,eq2,eq3])
print('The solve to the question is:',ans)


# # 4A-聯立方程式求解_2

# In[2]:


#2*a+2*b-c+d-4,4*a+3*b-c+2*d-6,8*a+5*b-3*c+4*d-12,3*a+3*b-2*c+2*d-6
eq1=input('enter an equation:')
eq2=input('enter an equation:')
eq3=input('enter an equation:')
eq4=input('enter an equation:')
from sympy.solvers import solve
from sympy import symbols
a,b,c,d=symbols('a,b,c,d')
ans=solve([eq1,eq2,eq3,eq4])
print('The solve to the question is:',ans)

