.class public Program
.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method
.method public static main([Ljava/lang/String;)V
.limit locals 5
.limit stack 1024
new java/util/Scanner
dup
getstatic java/lang/System.in Ljava/io/InputStream;
invokespecial java/util/Scanner.<init>(Ljava/io/InputStream;)V
astore 0
sipush 0
istore 1
sipush 0
istore 2
sipush 0
istore 3
sipush 0
istore 4
iload 2
iload 2
imul
sipush 4
iload 1
imul
iload 3
imul
isub
istore 4
return
.end method
