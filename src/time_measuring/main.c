
// KØR MED gcc -o test add1.s main.c
// TODO: Iterer filer i en folder? Skal måske implementeres i MakeFile
// TODO: Smid resultaterne i en fil.
// TODO: Ændr funktions-navn. Altid navn "f0"?

#include <stdlib.h>
#include <inttypes.h>
#include <stdio.h>
#include <time.h>

// Funktionsnavne: 'main' eller 'f0'
// TODO: Tag højde for 'main'
extern uint64_t f0(uint64_t *p);

double average_time_micro_sec(uint64_t arg)
{
    struct timeval start_time, end_time;
    double avg_time;
    int time_sum = 0;
    uint32_t REPETITIONS = 1;

    for (uint32_t i = 1; i <= REPETITIONS; i++)
    {
        gettimeofday(&start_time, NULL);
        f0(arg);
        gettimeofday(&end_time, NULL);
        time_sum += (end_time.tv_usec - start_time.tv_usec);
    }

    avg_time = time_sum / ((double)REPETITIONS);
    return avg_time;
}

int main()
{
    double t = average_time_micro_sec(42);
    printf("%.6f", t);
    return 0;
}