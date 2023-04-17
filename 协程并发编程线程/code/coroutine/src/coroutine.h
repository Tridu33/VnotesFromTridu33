#ifndef __COROUTINE_H
#define __COROUTINE_H

#include <stddef.h>
#include <stdint.h>
#include <ucontext.h>

#define DEFAULT_STACK_SIZE     (1024 * 1024)
#define DEFAULT_COROUTINE_SIZE 16

// call back function type
typedef void (*Func)(void*);

enum Coroutine_status
{
    CO_DEAD,
    CO_RUNNING,
    CO_RUNNABLE,
    CO_SUSPEND
};

// general registers
struct Registers
{
    uint64_t rip;
    uint64_t rsp;
    uint64_t rbp;
    uint64_t rax;
    uint64_t rbx;
    uint64_t rcx;
    uint64_t rdx;
    uint64_t rsi;
    uint64_t rdi;
    uint64_t r8;
    uint64_t r9;
    uint64_t r10;
    uint64_t r11;
    uint64_t r12;
    uint64_t r13;
    uint64_t r14;
    uint64_t r15;
};

// task context
struct Context
{
    struct Registers regs;
};

struct Coroutine
{
    struct Context context;
    Func func;
    void* arg;
    enum Coroutine_status status;
    size_t stack_size;
    void* stack;
};

struct Schedule
{
    struct Context main;
    int running_id;
    int co_size;
    int co_capacity;
    struct Coroutine** coroutines;
};

void schedule_initialize(void);
void schedule_destroy(void);
int coroutine_create(Func func, void* arg, size_t stack_size);
void coroutine_resume(int id);
void coroutine_yield(void);
enum Coroutine_status coroutine_status(int id);
int Coroutine_running(void);

#endif // __COROUTINE_H

