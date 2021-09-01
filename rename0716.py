import os
cwd=os.getcwd()
res=os.listdir(cwd)
for i in res:
 if ".h5" in i:
  pathsepa = os.path.splitext(i)
#  l1 = len(pathsepa)
  s = pathsepa[0]
  k=0
#  for k in range(0,l1-1):
#   s = s.join(pathsepa)[k]

  
  print (s)
  s1 = s.replace('-2800','-1800')
  print (s1)
  os.rename(os.path.join(cwd,i),os.path.join(cwd,s1))
