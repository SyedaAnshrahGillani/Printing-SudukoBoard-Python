#Soduko model
elements=[[7,8,0,4,0,0,1,2,0],
          [6,0,0,0,7,5,0,0,9],
          [0,0,0,6,0,1,0,7,8],
          [0,0,7,0,4,0,2,6,0],
          [0,0,1,0,5,0,9,3,0],
          [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2],
          [1,2,0,0,0,7,4,0,0],
          [0,4,9,2,0,6,0,0,7]
    ]

for i in range(len(elements)):
    if((i%3==0) and (i!=0)):
        print("_________________________\n")
    for j in range(len(elements[i])):
        if(j%3==0):
            print("| ",end='')
        if(j==8):
            print(elements[i][j])
        else:
            print(str(elements[i][j])+" ",end='')
    
        
