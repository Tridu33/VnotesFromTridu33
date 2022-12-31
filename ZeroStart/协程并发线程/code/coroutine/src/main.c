#include <stdio.h>
#include "coroutine.h"

struct args
{
    int n;
};

static void foo(void* ud)
{
    struct args* arg = ud;
    int start = arg->n;
    for (int i = 0; i < 5; ++i)
    {
        printf("coroutine %d: %d\n", Coroutine_running(), start + i);
        coroutine_yield();
    }
}

int main(void)
{
    schedule_initialize();

    struct args arg1 = { 0 };
    struct args arg2 = { 100 };

    int co1 = coroutine_create(foo, &arg1, DEFAULT_STACK_SIZE);
    int co2 = coroutine_create(foo, &arg2, DEFAULT_STACK_SIZE);
    printf("main start\n");
    while (coroutine_status(co1) && coroutine_status(co2))
    {
        coroutine_resume(co1);
        coroutine_resume(co2);
    }
    printf("main end\n");

    schedule_destroy();
}