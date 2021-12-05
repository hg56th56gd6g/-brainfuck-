# bf2c.py

brainfuck代码转c代码

支持命令行调用,格式:

### python bf2c.py "input_file_path" "output_file_path" "options"

options格式:

#### bits|left_mode|right_mode|pause|add|sub

### 注意:options要按顺序输入且两边加双引号否则|会被识别成命令,覆写output_file

<br/>

```python
def str_bf2c(code="",bits=64,left_mode=1,right_mode=1,pause=True,add=True,sub=True):
```

将bf代码字符串转为c代码字符串

### code:bf代码字符串

### bits:只能是16,32或64,计算机位数

### left_mode:指针--模式

0:如果指针==最小指针,报错

1:如果指针==最小指针,向左扩展内存

2:如果指针==最小指针,循环到最大指针

### right_mode:指针++模式

0:如果指针==最大指针,报错

1:如果指针==最大指针,向右扩展内存

2:如果指针==最大指针,循环到最小指针

### pause:程序结束后是否暂停

### add:当前单元格从255加到256是否循环到0,否则报错

### sub:当前单元格从0减到-1是否循环到255,否则报错

<br/>

```python
def file_bf2c(input_file,output_file,bits=64,left_mode=1,right_mode=1,pause=True,add=True,sub=True):
```

将bf代码文件写出到c代码文件

### input_file:bf代码文件对象,要求可读(input_file.read())

### output_file:c代码文件对象,要求可写(output_file.write())

### 其他参数同str_bf2c
