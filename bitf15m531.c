#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
int gl[4]={0,0,0,0};
int main()
{
	int i;
	int cpid1=vfork();
	int a[100];
	int status=0;
	for (i=0;i<=100;i++)
		a[i]=i+1;
	if (cpid1<0)
		printf("vFork 1 Failed\n");
	else if (cpid1==0)
	{
		for (i=0;i<25;i++)
			gl[0]+=a[i];
		int cpid2=vfork();
		if (cpid2<0) printf("vFork 2 Failed\n");
		else if  (cpid2==0)
		{
			for (i=25;i<50;i++)
				gl[1]+=a[i];
			int cpid3=vfork();
			if (cpid3<0) printf("vFork 3 Failed\n");
			else if (cpid3==0)
			{
				for (i=50;i<75;i++)
					gl[2]+=a[i];
				int cpid4=vfork();
				if (cpid4<0) printf("vFork 4 Failed\n");
				else if (cpid4==0)
					for (i=75;i<100;i++)
						gl[3]+=a[i];
				exit(0);
			}
			exit(0);
		}
		exit(0);
	}
	else 
	{
		wait(&status);
		printf("Total Sum is %d\n",gl[0]+gl[1]+gl[2]+gl[3]);
	}
	return 0;
}
