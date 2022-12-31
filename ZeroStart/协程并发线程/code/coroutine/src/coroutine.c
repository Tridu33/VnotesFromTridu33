
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#include "coroutine.h"

#define MOV_REG2MEM(reg, mem) asm volatile ("movq %%" #reg ", %0\n\t" : "=m" (mem) :: "memory")
#define MOV_MEM2REG(mem, reg) asm volatile ("movq %0, %%" #reg "\n\t" : :"m" (mem) : #reg)

#define REG_STORE(reg, pointer) MOV_REG2MEM(reg, pointer->regs.reg)
#define REG_RESTORE(reg, pointer) MOV_MEM2REG(pointer->regs.reg, reg)

#define REG_STORE2(reg, obj) MOV_REG2MEM(reg, obj.regs.reg)
#define REG_RESTORE2(reg, obj) MOV_MEM2REG(obj.regs.reg, reg)

static struct Schedule schedule;

static void main_func(void);

// save current context to prev, and switch context to next
static void context_swap(struct Context* prev_, struct Context* next_)
{
    // store in .data, avoid copying stack frame to the new stack
    static uint64_t eip;
    static volatile struct Context* prev;
    static volatile struct Context* next;

    prev = prev_;
    next = next_;
    eip = next->regs.rip;

    // store current context in prev
    REG_STORE(rax, prev);
    REG_STORE(rbx, prev);
    REG_STORE(rcx, prev);
    REG_STORE(rdx, prev);
    REG_STORE(rsi, prev);
    REG_STORE(rdi, prev);
    REG_STORE(r8, prev);
    REG_STORE(r9, prev);
    REG_STORE(r10, prev);
    REG_STORE(r11, prev);
    REG_STORE(r12, prev);
    REG_STORE(r13, prev);
    REG_STORE(r14, prev);
    REG_STORE(r15, prev);
    REG_STORE(rbp, prev);
    REG_STORE(rsp, prev);
    // jump to $eip_to_store
    asm volatile ("movq $eip_to_store, %0" : "=m" (prev->regs.rip));

    // resotre context from next
    REG_RESTORE(rax, next);
    REG_RESTORE(rbx, next);
    REG_RESTORE(rcx, next);
    REG_RESTORE(rdx, next);
    REG_RESTORE(rsi, next);
    REG_RESTORE(rdi, next);
    REG_RESTORE(r8,  next);
    REG_RESTORE(r9,  next);
    REG_RESTORE(r10, next);
    REG_RESTORE(r11, next);
    REG_RESTORE(r12, next);
    REG_RESTORE(r13, next);
    REG_RESTORE(r14, next);
    REG_RESTORE(r15, next);
    REG_RESTORE(rbp, next);
    REG_RESTORE(rsp, next);
    asm volatile ("jmpq *%0\n\t" : : "m" (eip));

    // label: eip_to_store
    asm volatile("eip_to_store:\n");
}

// construct a Coroutine and return it
static struct Coroutine* co_new(Func func, void* arg, size_t stack_size)
{
    struct Coroutine* co = malloc(sizeof(*co));
    co->func = func;
    co->arg  = arg;
    co->stack_size = stack_size;
    co->stack = malloc(stack_size);
    co->status = CO_RUNNABLE;
    co->context.regs.rsp = (uint64_t)co->stack + co->stack_size;
    co->context.regs.rip = (uint64_t)main_func;

    return co;
}

// destruct a Coroutine
static void co_delete(struct Coroutine* co)
{
    free(co->stack);
    free(co);
}

// Coroutine task
static void main_func(void)
{
    static uint8_t stack[1024 * 1024];
    static void* new_rbp = stack + 1024*1024;

    void* new_rsp;
    void* old_rbp;
    void* old_rsp;

    struct Coroutine* co;

    co = schedule.coroutines[schedule.running_id];
    co->func(co->arg);

    // get rbp and rsp
    asm volatile ("movq %%rbp, %0" : "=m" (old_rbp));
    asm volatile ("movq %%rsp, %0" : "=m" (old_rsp));

    // switch to the temporary stack，copy red zone and [rsp, rbp]
    new_rsp = new_rbp - (old_rbp - old_rsp);
    memcpy(new_rsp - 128, old_rsp - 128, old_rbp - old_rsp + 128);
    asm volatile ("movq %0, %%rbp" : : "m" (new_rbp));
    asm volatile ("movq %0, %%rsp" : : "m" (new_rsp));

    // free co
    co_delete(co);

    // update schedule
    schedule.coroutines[schedule.running_id] = NULL;
    --schedule.co_size;
    schedule.running_id = -1;

    // switch to shcedule.main
    REG_RESTORE2(rax, schedule.main);
    REG_RESTORE2(rbx, schedule.main);
    REG_RESTORE2(rcx, schedule.main);
    REG_RESTORE2(rdx, schedule.main);
    REG_RESTORE2(rsi, schedule.main);
    REG_RESTORE2(rdi, schedule.main);
    REG_RESTORE2(r8,  schedule.main);
    REG_RESTORE2(r9,  schedule.main);
    REG_RESTORE2(r10, schedule.main);
    REG_RESTORE2(r11, schedule.main);
    REG_RESTORE2(r12, schedule.main);
    REG_RESTORE2(r13, schedule.main);
    REG_RESTORE2(r14, schedule.main);
    REG_RESTORE2(r15, schedule.main);
    REG_RESTORE2(rbp, schedule.main);
    REG_RESTORE2(rsp, schedule.main);
    asm volatile ("jmpq *%0\n\t" : : "m" (schedule.main.regs.rip));
}

// initialize static schedule
void schedule_initialize(void)
{
    schedule.running_id = -1;
    schedule.co_capacity = DEFAULT_COROUTINE_SIZE;
    schedule.co_size = 0;
    schedule.coroutines = malloc(sizeof(struct Coroutine*) * schedule.co_capacity);
    memset(schedule.coroutines, 0, sizeof(struct Coroutine*) * schedule.co_capacity);
}


// destroy static schedule
void schedule_destroy(void)
{
    for (int i = 0; i < schedule.co_size; ++i)
    {
        if (schedule.coroutines[i] != NULL)
        {
            co_delete(schedule.coroutines[i]);
        }
    }
    free(schedule.coroutines);
}

// create a coroutine, register a call back function
int coroutine_create(Func func, void* arg, size_t stack_size)
{
    struct Coroutine* co = co_new(func, arg, stack_size);
    if (schedule.co_size >= schedule.co_capacity)
    {
        int id = schedule.co_capacity;
        schedule.coroutines = realloc(schedule.coroutines, 2 * schedule.co_capacity * sizeof(struct Coroutine*));
        memset(schedule.coroutines + schedule.co_capacity, 0, schedule.co_capacity * sizeof(struct coroutine*));
        schedule.co_capacity *= 2;
        schedule.coroutines[id] = co;
        return id;
    }
    else
    {
        for (int i = 0; i < schedule.co_capacity; ++i)
        {
            if (schedule.coroutines[i] == NULL)
            {
                schedule.coroutines[i] = co;
                ++schedule.co_size;
                return i;
            }
        }
    }
    assert(0);
    return -1;
}

// execute a coroutine
void coroutine_resume(int id)
{
    assert(schedule.running_id == -1);
    assert(id >= 0 && id < schedule.co_capacity);
    assert(schedule.coroutines[id] != NULL);

    struct Coroutine* co = schedule.coroutines[id];
    switch (co->status)
    {
        case CO_RUNNABLE:
            co->status = CO_RUNNING;
            schedule.running_id = id;
            context_swap(&schedule.main, &co->context);
            break;

        case CO_SUSPEND:
            co->status = CO_RUNNING;
            schedule.running_id = id;
            context_swap(&schedule.main, &co->context);
            break;

        default:
            assert(0);
    }
}

// switch to the coroutine which resumed current coroutine
void coroutine_yield(void)
{
    int id = schedule.running_id;
    assert(id >= 0);
    schedule.running_id = -1;
    struct Coroutine* co = schedule.coroutines[id];
    co->status = CO_SUSPEND;
    context_swap(&co->context, &schedule.main);
}

// get a coroutine's status
enum Coroutine_status coroutine_status(int id)
{
    assert(id >= 0 && id < schedule.co_capacity);
    if (schedule.coroutines[id] == NULL)
        return CO_DEAD;
    else
        return schedule.coroutines[id]->status;
}

// get current running coroutine
int Coroutine_running(void)
{
    return schedule.running_id;
}


