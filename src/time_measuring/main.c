
#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>
extern uint64_t add1(uint64_t *p);

double average_time_ms(void (*func)(u_int64_t), u_int64_t arg){
    clock_t start_time, end_time;
    double avg_time_ms;
    int time_sum = 0;
    uint32_t LOOPS = 1000;

    for(uint32_t i = 1; i <= LOOPS; i++){
        start_time = clock();
        func(arg);
        end_time = clock();
        time_sum += (end_time-start_time);
    }

    avg_time_ms = time_sum/((double)LOOPS);
    return avg_time_ms;
}


int main()
{
    double i = average_time_ms(add1, 42);
    printf("%.10f", i);
    return 0;
}
