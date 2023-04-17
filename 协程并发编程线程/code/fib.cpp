// yield.cpp : Defines the entry point for the console application.
// https://github.com/kirkshoop/await
// https://chlorie.github.io/ChloroBlog/posts/2020-08-10/0-generator.html 面向修复编译器报错编程——基于 C++20 协程写一个生成器


#include<iostream> 
#include<stdio.h>
#include <tchar.h>
// MSCV
// #include <experimental/resumable>
// #include <experimental/generator>
// #include <experimental/coroutine>
// namespace ex = std::experimental;

// g++ -fcoroutines -std=c++20
//clang++ -std=c++20 -stdlib=libc++ -fcoroutines-ts
//  选https://godbolt.org/ x86-64-gcc(couroutines) 跑斐波那契理解为何 编译选项 -fcoroutines -std=c++20 为何
#include <coroutine>
#include <thread>
using namespace std;
//https://chlorie.github.io/ChloroBlog/posts/2020-08-10/0-generator.html
template <typename T>
class generator final
{
public:
    class promise_type;
    using handle_type = stdx::coroutine_handle<promise_type>;

    class promise_type final
    {
    private:
        T value_;

    public:
        generator get_return_object() { return generator{ handle_type::from_promise(*this) }; }
        stdx::suspend_always initial_suspend() { return {}; }
        stdx::suspend_always final_suspend() { return {}; }
        stdx::suspend_always yield_value(T value)
        {
            value_ = std::move(value);
            return {};
        }
        void return_void() {}
        void unhandled_exception() {}

        const T& get_value() const { return value_; }
    };

    struct sentinel final {};

    class iterator final
    {
    private:
        handle_type handle_;

    public:
        explicit iterator(const handle_type handle):
            handle_{ handle }
        {
            handle_.resume();
        }

        iterator& operator++()
        {
            handle_.resume();
            return *this;
        }

        const T& operator*() const { return handle_.promise().get_value(); }

        friend bool operator==(const iterator it, sentinel) { return it.handle_.done(); }
    };

private:
    handle_type handle_;

public:
    explicit generator(const handle_type handle): handle_{ handle } {}
    generator(generator&& other) noexcept:
        handle_{ std::exchange(other.handle_, {}) } {}
    ~generator() noexcept
    {
        if (handle_)
            handle_.destroy();
    }

    iterator begin() const { return iterator{ handle_ }; }
    sentinel end() const { return {}; }
};


generator<int> fibonacci(int n) {
    int a = 0;
    int b = 1;

    while (n-- > 0) {
        //  `yield_value` keyword:
        //   await generator<T>::promise_type::yield_value(T)
        co_yield a; // co_yield xxx 会被转化为 co_await promise.yield_value(xxx)
        // http://kirkshoop.github.io/async/rxcpp/await/c++/2015/03/17/await-in-c++-yield-the-next.html
        auto next = a + b; a = b;
        b = next;
    }
}

//Fibonacci数列递归解法 C++ 实现
int Fib(int n) 
{
	if(n==0) 
		return 0;
	else if(n==1)
		return 1;
	else
		return Fib(n-1)+Fib(n-2);
}


int fib(int n)
{
	if(n==0)
		return 0;
	if(n==1)
		return 1;
	int f1=1;
	int f2=0;
	int fn=0;
	for(int i=2;i<=n;i++) 
	{
		fn=f2+f1;
		f2=f1;
		f1=fn;
	}
	return fn;
}

int fib(int n){
	int f1=1;
	int f2=1;
	int s;
	if(n==1||n==2)  return 1;
	else{
		for(int i=3;i<=n;i++){
			s=f1+f2;
			f1=f2;
			f2=s;
		}
		return s;
	}
}

int _tmain(int argc, _TCHAR* argv[]) {
	int n;
	cout<<"请输入一个数：";
	cout<<endl;
	cin>>n;
	cout<<Fib(n)<<endl;
	return 0;


    for (auto v : fibonacci(35)) {
        if (v > 10)
            break;
        std::cout << v << ' ';
    }
}