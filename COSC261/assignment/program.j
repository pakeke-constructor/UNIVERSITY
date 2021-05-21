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
sipush 1
istore 1
sipush 1
istore 2
sipush 1
istore 3
l1:
iload 3
sipush 50
if_icmpge l2
iload 2
istore 4
iload 1
iload 2
iadd
istore 2
iload 4
istore 1
iload 3
sipush 1
iadd
istore 3
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 1
invokestatic java/lang/String/valueOf(I)Ljava/lang/String;
invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V
goto l1
l2:
return
.end method
