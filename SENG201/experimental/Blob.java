

public class Blob extends Enemy{
    public Blob(String name){
        this.hp = 10;
        this.max_hp = 100;
        this.dmg = 2;
        
        this.name = name + " the blob";

        System.out.println(this.isAlive());
        this.heal(-100);
        System.out.println(this.isAlive());
        
        this.tauntUser();
    };
}

