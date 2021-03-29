
/*

Basically, all annotations are compile time
checks.



*/






// EXAMPLE WITH   @override
class Parent{
    public void sayHi(){
        System.out.println("hii from Parent");
    }
}


class Child extends Parent{

    @override
    public void sayHi(int x){
        System.out.println("hii from child");
        /*
    This here raises an error at compile time, because `sayHi`
    has not been overriden; its been overloaded instead.
       calling  `<Child>.sayHi(1)` will print  "hii from Parent",
       due to the integer argument.

    When @override is used, and a method is not overridden, a
    compile error is thrown
        */
    }

}

