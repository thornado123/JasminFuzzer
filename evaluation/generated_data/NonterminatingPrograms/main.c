#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <stdbool.h>

extern int64_t f0(int64_t p);

int main(){
    int32_t res = f0(42);
    printf("%" PRId32 "\n", res);
    return 1;
}