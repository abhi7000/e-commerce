from math import sqrt,floor 


def dynamic(n):
	dynarr=[1 for i in range(n+1)]
	uplmt=floor(sqrt(n))
	temp=2
	while(temp<n+1):
		if(dynarr[temp]==1):
			for i in range(temp*2,n+1,temp):
				dynarr[i]=0
		temp+=1

	for i in range(n+1):
		if(dynarr[i]==1):
			print(i)

number=int(input("enter positive number="))
dynamic(number)

