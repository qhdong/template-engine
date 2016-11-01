# A Template Engine

500 lines中的一个`python`项目，编写一个Django风格的模板引擎。

模板引擎通常包含 **解析**, **渲染** 两个步骤，其中解析有两种实现方式：
1. 解析生成一个关于模板的数据结构，渲染过程中填入相应的数据
2. 解析通过编译生成一个`python`可执行代码，渲染就是执行这段代码

第二种方式效率高，`jinja2`和`Mako`使用这种方式。

一些微优化：

- `result.append('hello')`与 `append_result=result.append append_result('hello')`等价，多次使用后者速度更快
- 将`str`存储在本地局部变量中速度更快， locals are faster than builtins