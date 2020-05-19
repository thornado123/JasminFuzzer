
// KØR MED gcc -o test add1.s main.c

#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>
#include <limits.h>
#include <float.h>
#include <math.h>
#include <stdbool.h>

extern uint64_t add1(int64_t p);
unsigned int REPETITIONS = 1000;
unsigned int MAX_DEPTH   = 1000;

double asm_func_input(int64_t input){
    
    unsigned int i;
    double avg_time;
    clock_t measured_time;
    time_t rawtime;
    int64_t result;
    struct tm * timeinfo;
    
    
    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    printf ("Current local time and date: %s", asctime (timeinfo) );
    printf("TESTING with: %lld\n", input);

    for (i = 0; i < REPETITIONS; i++)
    {
        measured_time   = clock();
        result          = add1(input);
        measured_time   = clock() - measured_time;
        double time_t   = ((double) measured_time )/CLOCKS_PER_SEC;
        avg_time        += time_t;
    }
    
    avg_time = avg_time / REPETITIONS;
    return avg_time;
}

void running_asm_func()
{
    bool while_con;
    double avg_time, slowest, fastest, difference, dif_tresh;
    unsigned int counter;
    int64_t result, s_input, f_input, search_min, search_max, middle, input;
    
    while_con   = true;
    avg_time    = 0;
    slowest     = 0;
    fastest     = FLT_MAX;
    search_min  = -9223372036854775800;
    search_max  = 9223372036854775807;
    middle      = 0;
    dif_tresh   = 0.02;
    input       = 0;
    
    while(while_con){
        
        
        
        counter ++;
        avg_time = asm_func_input(input);
        
        if(slowest < avg_time){
        
            s_input = input;
            slowest = avg_time;
            
        }
        
        if(fastest > avg_time){
            
            f_input = input;
            fastest = avg_time;
            
        }
        
        difference  = fabs(fastest - slowest);
        avg_time    = 0;
        while_con   = counter < MAX_DEPTH && difference < dif_tresh;
    }

    printf("Fastest: %f - %lld\n", fastest, f_input);
    printf("Slowest: %f - %lld\n", slowest, s_input);
}

int main()
{
    running_asm_func();
    return 0;
}
