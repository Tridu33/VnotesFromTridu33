# 1. 嵌套括号匹配python






https://www.codenong.com/5454322/



堆栈是完成这项工作的最佳工具

```python
import re
def matches(line, opendelim='(', closedelim=')'):
    stack = []

    for m in re.finditer(r'[{}{}]'.format(opendelim, closedelim), line):
        pos = m.start()

        if line[pos-1] == '\\\':
            # skip escape sequence
            continue

        c = line[pos]

        if c == opendelim:
            stack.append(pos+1)

        elif c == closedelim:
            if len(stack) > 0:
                prevpos = stack.pop()
                # print("matched", prevpos, pos, line[prevpos:pos])
                yield (prevpos, pos, len(stack))
            else:
                # error
                print("encountered extraneous closing quote at pos {}: '{}'".format(pos, line[pos:] ))
                pass

    if len(stack) > 0:
        for pos in stack:
            print("expecting closing quote to match open quote starting at: '{}'"
                  .format(line[pos-1:]))
```























```python
line = '(((1+0)+1)+1)'
for openpos, closepos, level in matches(line):
    print(line[openpos:closepos], level)
```












