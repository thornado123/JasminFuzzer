
// KØR MED gcc -o test add1.s main.c

#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <stdbool.h>

extern int64_t main_jazz(int64_t p);

unsigned int REPETITIONS = 1000;
unsigned int MAX_DEPTH   = 1000;
int64_t search_min       = -9223372036854775800;
int64_t search_max       = 9223372036854775807;

double asm_func_input(int64_t input){

unsigned int i;
double avg_time;
clock_t measured_time;
time_t rawtime;
int64_t result;
struct tm * timeinfo;
avg_time = 0;

time ( &rawtime );
timeinfo = localtime ( &rawtime );
//    printf ("Current local time and date: %s", asctime (timeinfo) );
//    printf("TESTING with: %lld\n", input);

for (i = 0; i < REPETITIONS; i++)
{
measured_time   = clock();
result          = main_jazz(input);
measured_time   = clock() - measured_time;
double time_t   = ((double) measured_time )/CLOCKS_PER_SEC;
avg_time        += time_t;
}

avg_time = avg_time / REPETITIONS;
return avg_time;
}

int64_t check_range(double * best_time, int64_t * best_val, int64_t now, int64_t last, bool maxmin){
//    printf("START Best time: %f\n", *best_time);

int64_t c1, c2, cc;
double t1, t2, td1, td2;

printf("Now value: %lld\n", now);

cc = llabs(now - last);
c1 = now - last/2;
c2 = now + last/2;

//printf("Values c1: %lld c2: %lld\n", c1, c2);

t1 = asm_func_input(c1);
t2 = asm_func_input(c2);

td1 = *best_time - t1;
td2 = *best_time - t2;

//    printf("Time t1: %f\n", t1);
//    printf("Time t2: %f\n", t2);
//    printf("Best time: %f\n", **best_time);
//    printf("Time dif1: %f\n", td1);
//    printf("Time dif2: %f\n", td2);
//
// If maxmin == true: then we are trying to maximize the runningtime
if(maxmin){
if(td1 < td2){
if(td1 < 0){
//                printf("td1 < 0: %f\n", t1);
*best_time   = t1;
*best_val    = c1;
//                printf("B - time: %f\n", *best_time);
}
return c1;
}else{
if(td2 < 0){
//                printf("td2 < 0\n");
*best_time   = t2;
*best_val    = c2;
//                printf("B - time: %f\n", *best_time);
}
return c2;
}
}else{
if(td1 > td2){
if(td1 > 0){
//                printf("td1 > 0\n");
*best_time   = t1;
*best_val    = c1;
//                printf("B - time: %f\n", *best_time);
}
return c1;
}else{
if(td2 > 0){
//                printf("td2 > 0\n");
*best_time   = t2;
*best_val    = c2;
//                printf("B - time: %f\n", *best_time);
}
return c2;
}
}
}

void running_asm_func()
{
bool while_con, minimizing, maximizing;
double avg_time, difference, dif_tresh, dbl, slow_in;
int64_t max_now, max_last[2], min_now, min_last[2], a, b;
unsigned int counter;

// Pointer for the maxmin times as well as their values

int64_t * s_input;
int64_t * f_input;
double * fastest;
double * slowest;

minimizing  = false;
maximizing  = true;
while_con   = true;
counter     = 0;
slow_in     = 0;
slowest     = &slow_in;
dbl         = DBL_MAX;
fastest     = &dbl;
dif_tresh   = 0.4;

max_now     = 0;
max_last[0] = search_max/2;
max_last[1] = max_now;
min_now     = 0;
min_last[0] = search_max/2;
min_last[1] = min_now;

a           = 0;
b           = 0;

s_input     = &a;
f_input     = &b;

while(while_con){

//        printf("=== NOW CALLING MIN ===\n\n");
// Calling for min
printf("Itteration: %d\n", counter);
min_now = check_range(fastest, f_input, min_now, min_last[0], minimizing);
min_last[0] = min_last[1];
min_last[1] = min_now;

//        printf("END Best time: %f\n", *fastest);

//        printf("\n=== NOW CALLING MAX ===\n\n");
// Calling for max
max_now = check_range(slowest, s_input, max_now, max_last[0], maximizing);
max_last[0] = max_last[1];
max_last[1] = max_now;

//        printf("END Best time: %f\n\n", *slowest);

printf("Fastest: %f Value: %lld\n", *fastest, *f_input);
printf("Slowest: %f Value: %lld\n", *slowest, *s_input);

// Checking the loop condition
counter += 1;
difference  = fabs(*fastest - *slowest);
while_con   = counter < MAX_DEPTH && difference < dif_tresh;
//printf("DIFF: %f, COUNT: %d", difference, counter);
//        if (!while_con) {
////            printf("\n\nGot to the end\n");
//            printf("Counter: %d\n", counter);
//            printf("Difference: %f\n", difference);
//        }else{
////            printf("Still going\n");
////            printf("\n------------------------------------------------------\n\n");
//        }
}
printf("DIFF: %f, COUNT: %d", difference, counter);
//
//    printf("\nFastest: %f Value: %lld\n", *fastest, *f_input);
//    printf("Slowest: %f Value: %lld\n", *slowest, *s_input);
}

int main()
{
running_asm_func();
printf("DONE");
return 0;
}
