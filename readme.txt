�����ڱ�дbrainfuck�����ʱ��,���ԵȲ�������װ����Ǹ�����
�����ұ�д�����brainfuck���߰�
����������python2.7.18��,֧����ģ�鵼��,����ʽ�������������е���
�˳��ĺ���!
######
�Ķ�Դ������������׼��,����������������������python����
######
������߰������ϵ���Щ��ʲô��ͬ?
���ܺõ�֧����ѭ��Ƕ��(
�������ģ����ʽ��import,�����ṩ["inputerror","dataerror","moveerror","looperror","_","getch","putch","str_compile","file_compile","file_compile","str_run","file_run"]��Щ��ʹ�õĶ���
���"brainfuck.py������쳣����","brainfuck.py����ĳ���","brainfuck.py����ĺ���"
�������ֱ�ӱ����в���û�д������,�������python����̨һ���Ľ���ģʽ
���"brainfuck.py�Ľ���ģʽ"
�������ֱ�ӱ����в��Ҵ����˲���,�������������ִ��
���"brainfuck.py�Ĵ������"

brainfuck�������:
������һ�����ݴ�,ÿ��λ�þ���һ���ֽ�
����ָ�����ָ�����ݴ��ϵ�λ�õ�ָ��
+:����ָ��λ�õ�����--
-:����ָ��λ�õ�����++
<:����ָ��--
>:����ָ��++
[:ѭ����ʼ,�������ָ��λ�õ�����==0,������ѭ��,����,������ѭ��
]:ѭ������,�����ǰ����ָ��λ�õ�����==0,����ɴ�ѭ��,���������ѭ��
,:��������ָ��λ�õ�����Ϊ���������ж�ȡһ���ֽ�
.:������ָ��λ�õ�����д�������

brainfuck.py������쳣����:
inputerror:����������������������쳣
dataerror:���ݲ�������ʱ�������쳣
moveerror:����ָ���ƶ�����ʱ�������쳣
looperror:ѭ������ʱ�������쳣

brainfuck.py����ĳ���:
_:����������brainfuck��ִ�е�8���ַ���frozenset

brainfuck����ĺ���:
getch:��msvcrt import�ĺ���,���ڴӿ���̨��ȡһ���ֽ�
putch:��msvcrt import�ĺ���,���������̨���һ���ֽ�
str_compile:
    ��;:ȥ���ַ��������в��ڳ���_����ֽ�
    ����:code
    ����:code��brainfuck�����ַ���
    Ҫ��:code�������ַ���
    ����:ȥ��code�����в��ڳ���_����ֽڵ��ַ���
file_compile:
    ��;:ȥ���ļ������в��ڳ���_����ֽ�
    ����:input_file,output_file
    ����:input_file��brainfuck�����ļ�·��,output_file��ȥ��input_file�����в��ڳ���_����ֽڵ��ļ�·��
    Ҫ��:input_file,output_file���붼���ַ���
    ����:��
str_run:
    ��;:����brainfuck�����ַ���
    ����:code,input,output,add,sub,left,right,ret
    ����:
        code:�����ַ���
        input:����������,��һ������������ľ���"__call__"�����Ķ���
        output:���������,��һ����1����������ľ���"__call__"�����Ķ���
        add:�Ƿ����ݴ�255�ӵ�1
        sub:�Ƿ����ݴ�0����255
        left:�Ƿ�����̬�������ݴ�
        right:�Ƿ����Ҷ�̬�������ݴ�
        ret:��������Ƿ񷵻�tuple(data,data_pointer)
    Ҫ��:code�������ַ���,input��output�������"__call__"����,add��sub��left��right��ret������bool
    ����:���ret == True,����tuple(data,data_pointer)
file_run
    ��;:����brainfuck�����ļ�
    ����:input_file,input,output,add,sub,left,right,ret
    ����:
        input_file:�����ļ�·��
        input:����������,��һ������������ľ���"__call__"�����Ķ���
        output:���������,��һ����1����������ľ���"__call__"�����Ķ���
        add:�Ƿ����ݴ�255�ӵ�1
        sub:�Ƿ����ݴ�0����255
        left:�Ƿ�����̬�������ݴ�
        right:�Ƿ����Ҷ�̬�������ݴ�
        ret:��������Ƿ񷵻�tuple(data,data_pointer)
    Ҫ��:input_file�������ַ���,input��output�������"__call__"����,add��sub��left��right��ret������bool
    ����:���ret == True,����tuple(data,data_pointer)

brainfuck.py�Ľ���ģʽ:
��ֱ�����г������Բ����������python������һ�����������ֵ�

brainfuck.py�Ĵ������:
python brainfuck.py [activity] [input_data] [option]
[activity]:"compile"��"run"
    compile:ȥ�����в��ڳ���_����ֽ�
    run:����
[input_data]:���[activity]��"compile",Ҫ����input_file��output_file,�����"run",����input_file����
    �﷨:"[value1]|[value2]"...
[option]:ֻ��[activity]��"run"ʱ������,�ο�file_run�е�add,sub,left,right,ret�⼸������,����ʡ��,Ҫ��˳������
    �﷨:"[value1]|[value2]"...
ps:ÿ���������������Ҫ��˫����Ŷ,��Ȼ�����л��"|"ʶ�������