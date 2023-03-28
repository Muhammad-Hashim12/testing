a=['east','west','north','south']
#'''for i in a:
 #   l=[]
  #  for j in a:
   #     if j!=i:
    ##        if j not in l:
      #          l+=[j]
# print(f'{i} plays with {l}')
for i in range(len(a)):
    for j in range(i+1,len(a)):
        print(f'{a[i]} vs {a[j]}')
        
           
            