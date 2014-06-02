#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
	long x, n;
	double r;

	x = 100;

	if (argc == 2)
	{
		x = atol(argv[1]);
	}

	n = 1;
	while (n < x)
	{
		// quadratic formula calc
		r = (8*n) - (8*pow(n,2));
		r = sqrt(4 - r);
		r = (r +2)/4;
		
		if (r == floor(r))
		{
			printf("\n%lu/%lu %lu/%lu\n", (unsigned long)r, n,
									      (unsigned long)(r-1), n-1);
		}
			
		n++;
	}
}
