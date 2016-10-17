doors=["closed"]*101    #this is the inital status of the doors, all of them closed

for steps in range(1,101): #there's 100 status change (open/close) in the algorithm
    for status in range(steps,101,steps):   #this gives wich doors are changed in each steps
        if doors[status]=="closed":    #the following 4 lines are changing the doors status
            doors[status]="opened"
        elif doors[status]=="opened":
            doors[status]="closed"

doors_list=[]   #this is an empty list for the pretty output :)
for open_doors in range(1,101): #this is the list of the opened doors in the end
    if doors[open_doors]=="opened": #we are chosing the numbers of the opened doors
        doors_list.append(open_doors) #we are importing the numbers of the opened doors

print("The following doors are open:\n",*doors_list) #printing the output