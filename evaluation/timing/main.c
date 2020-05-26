
#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <stdbool.h>

extern int64_t f0(int64_t p);
int main()
{
int input = 41;
int64_t result;
result = f0(input);
printf("Result: %lld", result);
return 0;
}
