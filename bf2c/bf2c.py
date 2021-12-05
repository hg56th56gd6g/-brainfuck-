#-*- coding:utf-8 -*-
#python2.7.18_bf2c
__all__=["str_bf2c","file_bf2c"]
class inputerror(Exception):pass
class codeerror(Exception):pass
_=frozenset(("\x2b","\x2d","\x3c","\x3e","\x5b","\x5d","\x2c","\x2e"))
throw=(_ for _ in "").throw
def str_bf2c(code="",bits=64,left_mode=1,right_mode=1,pause=True,add=True,sub=True):
    if type(code)==str and type(pause)==type(add)==type(sub)==bool:
        loop_level=0
        for a in code:
            if a=="[":loop_level=loop_level+1
            elif a=="]":
                if loop_level==0:raise codeerror("loop error")
                else:loop_level=loop_level-1
        if loop_level!=0:raise codeerror("loop error")
        right_mode="if(pointer!=data+length-1){pointer=pointer+1;}else{goto right_move_out_of_range;}" if right_mode==0 else "if(pointer!=data+length-1){pointer=pointer+1;}else{if(data=(uint8_t *)realloc(data,length=length+1)){pointer=data+length-1;*pointer=0;}else{goto memory_error;}}" if right_mode==1 else "if(pointer!=data+length-1){pointer=pointer+1;}else{pointer=data;}" if right_mode==2 else throw(inputerror)
        left_mode="if(pointer!=data){pointer=pointer-1;}else{goto left_move_out_of_range;}" if left_mode==0 else "if(pointer!=data){pointer=pointer-1;}else{if(data=(uint8_t *)realloc(data,length=length+1)){a=data+length;b=a-1;while(b!=data){a=a-1;b=b-1;*a=*b;}*pointer=0;}else{goto memory_error;}}" if left_mode==1 else "if(pointer!=data){pointer=pointer-1;}else{pointer=data+length-1;}" if left_mode==2 else throw(inputerror)
        add="if(*pointer!=255){*pointer=*pointer+1;}else{goto end_of_maindd_overflow;}" if add==0 else "if(*pointer!=255){*pointer=*pointer+1;}else{*pointer=0;}" if add==1 else throw(inputerror)
        sub="if(*pointer){*pointer=*pointer-1;}else{goto sub_overflow;}" if sub==0 else "if(*pointer){*pointer=*pointer-1;}else{*pointer=255;}" if sub==1 else throw(inputerror)
        return "".join(("#include <stdint.h>\n#include <stdlib.h>\n#include <stdio.h>\nvoid main(void){\n    uint8_t *data,*pointer,*a,*b;\n    if(pointer=data=(uint8_t *)calloc(1,1)){\n        uint","16" if bits==16 else "32" if bits==32 else "64" if bits==64 else throw(inpurerror),"_t length=1;\n        ","".join(("*pointer=getch();" if a=="," else "putchar(*pointer);" if a=="." else "while(*pointer){" if a=="[" else "}" if a=="]" else add if a=="+" else sub if a=="-" else left_mode if a=="<" else right_mode if a==">" else "" for a in code if a in _)),"\n        goto end_of_main;\n    }\n    memory_error:\n    putchar(10);putchar(109);putchar(101);putchar(109);putchar(111);putchar(114);putchar(121);putchar(32);putchar(101);putchar(114);putchar(114);putchar(111);putchar(114);putchar(10);goto end_of_main;\n    add_overflow:\n    putchar(10);putchar(97);putchar(100);putchar(100);putchar(32);putchar(111);putchar(118);putchar(101);putchar(114);putchar(102);putchar(108);putchar(111);putchar(119);putchar(10);goto end_of_main;\n    sub_overflow:\n    putchar(10);putchar(115);putchar(117);putchar(98);putchar(32);putchar(111);putchar(118);putchar(101);putchar(114);putchar(102);putchar(108);putchar(111);putchar(119);putchar(10);goto end_of_main;\n    right_move_out_of_range:\n    putchar(10);putchar(114);putchar(105);putchar(103);putchar(104);putchar(116);putchar(32);putchar(109);putchar(111);putchar(118);putchar(101);putchar(32);putchar(111);putchar(117);putchar(116);putchar(32);putchar(111);putchar(102);putchar(32);putchar(114);putchar(97);putchar(110);putchar(103);putchar(101);putchar(10);goto end_of_main;\n    left_move_out_of_range:\n    putchar(10);putchar(108);putchar(101);putchar(102);putchar(116);putchar(32);putchar(109);putchar(111);putchar(118);putchar(101);putchar(32);putchar(111);putchar(117);putchar(116);putchar(32);putchar(111);putchar(102);putchar(32);putchar(114);putchar(97);putchar(110);putchar(103);putchar(101);putchar(10);goto end_of_main;\n    end_of_main:","\n    putchar(10);\n    system(\"pause\");\n}" if pause else "\n}"))
    else:raise inputerror
def file_bf2c(input_file,output_file,bits=64,left_mode=1,right_mode=1,pause=True,add=True,sub=True):
    try:
        if type(input_file.read(0))!=str:raise inputerror
        output_file.write("")
    except:raise inputerror
    if type(pause)==type(add)==type(sub)==bool:
        loop_level=0
        right_mode="if(pointer!=data+length-1){pointer=pointer+1;}else{goto right_move_out_of_range;}" if right_mode==0 else "if(pointer!=data+length-1){pointer=pointer+1;}else{if(data=(uint8_t *)realloc(data,length=length+1)){pointer=data+length-1;*pointer=0;}else{goto memory_error;}}" if right_mode==1 else "if(pointer!=data+length-1){pointer=pointer+1;}else{pointer=data;}" if right_mode==2 else throw(inputerror)
        left_mode="if(pointer!=data){pointer=pointer-1;}else{goto left_move_out_of_range;}" if left_mode==0 else "if(pointer!=data){pointer=pointer-1;}else{if(data=(uint8_t *)realloc(data,length=length+1)){a=data+length;b=a-1;while(b!=data){a=a-1;b=b-1;*a=*b;}*pointer=0;}else{goto memory_error;}}" if left_mode==1 else "if(pointer!=data){pointer=pointer-1;}else{pointer=data+length-1;}" if left_mode==2 else throw(inputerror)
        add="if(*pointer!=255){*pointer=*pointer+1;}else{goto end_of_maindd_overflow;}" if add==0 else "if(*pointer!=255){*pointer=*pointer+1;}else{*pointer=0;}" if add==1 else throw(inputerror)
        sub="if(*pointer){*pointer=*pointer-1;}else{goto sub_overflow;}" if sub==0 else "if(*pointer){*pointer=*pointer-1;}else{*pointer=255;}" if sub==1 else throw(inputerror)
        output_file.write("#include <stdint.h>\n#include <stdlib.h>\n#include <stdio.h>\nvoid main(void){\n    uint8_t *data,*pointer,*a,*b;\n    if(pointer=data=(uint8_t *)calloc(1,1)){\n        uint")
        output_file.write("16" if bits==16 else "32" if bits==32 else "64" if bits==64 else throw(inpurerror))
        output_file.write("_t length=1;\n        ")
        buffer=input_file.read(1)
        while buffer!="":
            if buffer in _:
                if buffer=="[":loop_level=loop_level+1
                elif buffer=="]":
                    if loop_level==0:raise codeerror("loop error")
                    else:loop_level=loop_level-1
                output_file.write("*pointer=getch();" if buffer=="," else "putchar(*pointer);" if buffer=="." else "while(*pointer){" if buffer=="[" else "}" if buffer=="]" else add if buffer=="+" else sub if buffer=="-" else left_mode if buffer=="<" else right_mode if buffer==">" else "")
            buffer=input_file.read(1)
        if loop_level!=0:raise codeerror("loop error")
        output_file.write("\n        goto end_of_main;\n    }\n    memory_error:\n    putchar(10);putchar(109);putchar(101);putchar(109);putchar(111);putchar(114);putchar(121);putchar(32);putchar(101);putchar(114);putchar(114);putchar(111);putchar(114);putchar(10);goto end_of_main;\n    add_overflow:\n    putchar(10);putchar(97);putchar(100);putchar(100);putchar(32);putchar(111);putchar(118);putchar(101);putchar(114);putchar(102);putchar(108);putchar(111);putchar(119);putchar(10);goto end_of_main;\n    sub_overflow:\n    putchar(10);putchar(115);putchar(117);putchar(98);putchar(32);putchar(111);putchar(118);putchar(101);putchar(114);putchar(102);putchar(108);putchar(111);putchar(119);putchar(10);goto end_of_main;\n    right_move_out_of_range:\n    putchar(10);putchar(114);putchar(105);putchar(103);putchar(104);putchar(116);putchar(32);putchar(109);putchar(111);putchar(118);putchar(101);putchar(32);putchar(111);putchar(117);putchar(116);putchar(32);putchar(111);putchar(102);putchar(32);putchar(114);putchar(97);putchar(110);putchar(103);putchar(101);putchar(10);goto end_of_main;\n    left_move_out_of_range:\n    putchar(10);putchar(108);putchar(101);putchar(102);putchar(116);putchar(32);putchar(109);putchar(111);putchar(118);putchar(101);putchar(32);putchar(111);putchar(117);putchar(116);putchar(32);putchar(111);putchar(102);putchar(32);putchar(114);putchar(97);putchar(110);putchar(103);putchar(101);putchar(10);goto end_of_main;\n    end_of_main:")
        output_file.write("\n    putchar(10);\n    system(\"pause\");\n}" if pause else "\n}")
    else:raise inputerror
if __name__=="__main__":
    from sys import argv
    if len(argv)==3:
        a=open(argv[1],"rb")
        b=open(argv[2],"wb")
        file_bf2c(a,b)
        a.close()
        b.close()
    elif len(argv)==4:
        a=open(argv[1],"rb")
        b=open(argv[2],"wb")
        c=argv[3].split("|")
        if len(c)==6:
            file_bf2c(a,b,int(c[0],base=10),int(c[1],base=10),int(c[2],base=10),True if c[3]=="True" else False if c[3]=="False" else throw(inputerror),True if c[4]=="True" else False if c[4]=="False" else throw(inputerror),True if c[5]=="True" else False if c[5]=="False" else throw(inputerror))
        else:raise inputerror
    else:raise inputerror