import itertools 

def surveillanceSystem(containers, L, reports):
 	poss_set=set()
	for report in set(reports):	
		poss_set |= set([j for j in range(int(L/2), len(containers)-L/2) if containers[j-L/2:j+L/2+1].count('X')==report])
		''''Builds a Range of possible places the cameras (only distinguished by reports element) 
			could be by looping through and counting 'X' viz. containers they would monitor'''
	scenarios=itertools.combinations(poss_set, len(reports)) #Gen scenarios for all cameras
	count_list=["-"]*len(containers)
	for c, scenario in enumerate(scenarios):
		for i in range(len(count_list)):
			if count_list[i]=="?":	continue #Time saver
			if (sum([i-L/2<=scen<=i+L/2 for scen in scenario])>0):	
				if count_list[i]=="-": count_list[i]="+" if c==0 else "?"
			else:	
				if count_list[i]=="+":	count_list[i]="?"
		#Transforms array of '-' viz no camera for each camera into + or ?'
	return "".join(count_list)
print surveillanceSystem("-XX--X-XX-X-X--X---XX-X---XXXX-----X", 7, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])#Sample Game

