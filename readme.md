我们在编写brainfuck程序的时候,调试等步骤很容易把我们给气死
所以我编写了这个brainfuck工具包
程序运行在python2.7.18上,支持以模块导入,交互式解释器和命令行调用
匪常的好用!

#### 阅读源码请做好心理准备,这可能是你见过的最难理解的python代码

# 懒得写成markdown了,所以直接复制过来了

这个工具包和网上的那些有什么不同?
它很好的支持了循环嵌套(
如果它以模块形式被import,它会提供["inputerror","dataerror","moveerror","looperror","_","getch","putch","str_compile","file_compile","file_compile","str_run","file_run"]这些可使用的对象
详见"brainfuck.py定义的异常类型","brainfuck.py定义的常量","brainfuck.py定义的函数"
如果它是直接被运行并且没有传入参数,它会打开像python控制台一样的交互模式
详见"brainfuck.py的交互模式"
如果它是直接被运行并且传入了参数,它会解析参数并执行
详见"brainfuck.py的传入参数"

brainfuck代码规则:
数据是一条数据带,每个位置就是一个字节
数据指针就是指向数据带上的位置的指针
+:数据指针位置的数据--
-:数据指针位置的数据++
<:数据指针--

> :数据指针++
[:循环开始,如果数据指针位置的数据==0,跳过此循环,否则,启动此循环
]:循环结束,如果当前数据指针位置的数据==0,则完成此循环,否则继续此循环
,:设置数据指针位置的数据为从输入流中读取一个字节
.:将数据指针位置的数据写入输出流

brainfuck.py定义的异常类型:
inputerror:函数输入参数错误引发的异常
dataerror:数据操作错误时引发的异常
moveerror:数据指针移动错误时引发的异常
looperror:循环错误时引发的异常

brainfuck.py定义的常量:
_:包含了所有brainfuck可执行的8个字符的frozenset

brainfuck定义的函数:
getch:从msvcrt import的函数,用于从控制台读取一个字节
putch:从msvcrt import的函数,用于向控制台输出一个字节
str_compile:
    用途:去除字符串中所有不在常量_里的字节
    输入:code
    描述:code是brainfuck代码字符串
    要求:code必须是字符串
    返回:去除code里所有不在常量_里的字节的字符串
file_compile:
    用途:去除文件里所有不在常量_里的字节
    输入:input_file,output_file
    描述:input_file是brainfuck代码文件路径,output_file是去除input_file里所有不在常量_里的字节的文件路径
    要求:input_file,output_file必须都是字符串
    返回:无
str_run:
    用途:运行brainfuck代码字符串
    输入:code,input,output,add,sub,left,right,ret
    描述:
        code:代码字符串
        input:输入流函数,是一个无输入参数的具有"__call__"方法的对象
        output:输出流函数,是一个有1个输入参数的具有"__call__"方法的对象
        add:是否将数据从255加到1
        sub:是否将数据从0减到255
        left:是否向左动态扩充数据带
        right:是否向右动态扩充数据带
        ret:运行完后是否返回tuple(data,data_pointer)
    要求:code必须是字符串,input和output必须具有"__call__"方法,add和sub和left和right和ret必须是bool
    返回:如果ret == True,返回tuple(data,data_pointer)
file_run
    用途:运行brainfuck代码文件
    输入:input_file,input,output,add,sub,left,right,ret
    描述:
        input_file:代码文件路径
        input:输入流函数,是一个无输入参数的具有"__call__"方法的对象
        output:输出流函数,是一个有1个输入参数的具有"__call__"方法的对象
        add:是否将数据从255加到1
        sub:是否将数据从0减到255
        left:是否向左动态扩充数据带
        right:是否向右动态扩充数据带
        ret:运行完后是否返回tuple(data,data_pointer)
    要求:input_file必须是字符串,input和output必须具有"__call__"方法,add和sub和left和right和ret必须是bool
    返回:如果ret == True,返回tuple(data,data_pointer)

brainfuck.py的交互模式:
你直接运行程序试试不就行了吗跟python解释器一样很容易上手的

brainfuck.py的传入参数:
python brainfuck.py [activity] [input_data] [option]
[activity]:"compile"或"run"
    compile:去除所有不在常量_里的字节
    run:运行
[input_data]:如果[activity]是"compile",要输入input_file和output_file,如果是"run",输入input_file即可
    语法:"[value1]|[value2]"...
[option]:只有[activity]是"run"时才有用,参考file_run中的add,sub,left,right,ret这几个参数,可以省略,要按顺序输入
    语法:"[value1]|[value2]"...
ps:每个传入参数的外面要加双引号哦,不然命令行会把"|"识别成命令
