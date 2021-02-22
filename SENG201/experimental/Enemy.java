

public abstract class Enemy{

    float hp;
    float max_hp;

    float dmg;

    String name;

    public boolean isAlive(){
        return this.hp > 0;
    }

    public float heal(float amount){
        this.hp = Math.max(this.hp + amount, this.max_hp);
        return this.hp;
    }

    public void tauntUser(){
        System.out.println(this.name + " taunts the programmer!");
    }
}

