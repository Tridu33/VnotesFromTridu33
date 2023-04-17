// https://chlorie.github.io/ChloroBlog/posts/2020-08-10/0-generator.html
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

generator<char> lower_chars(const char* str)
{
    while (*str)
        co_yield static_cast<char>(std::tolower(*str++));
}

int main() // NOLINT
{
    for (char ch : lower_chars("HELLO WORLD!"))
        std::cout << ch;
    // 输出: hello world!
    return 0;
}