

package lab5;


public class RocketShip {

    int MAX_FUEL_LEVEL = 100;

    int fuelLevel;
    int currentHeight;
    
    public static void main(String[] a){
    	System.out.println("Hello world,?");
    }

    public RocketShip(int fuelLevel) {
        this.fuelLevel = fuelLevel;
        this.currentHeight = 0;
    }

    public int getFuelLevel() {
        return fuelLevel;
    }

    public int getCurrentHeight() {
        return currentHeight;
    }

    public void fuelUp(int fuelAmount) {
        fuelLevel += fuelAmount;
    }

    public void takeOff() {
            fuelLevel -= 20;
            currentHeight += 20;
    }

    public void goHigher() {
        fuelLevel -= 10;
        currentHeight += 50;
    }

    public void goLower() {
        currentHeight -= 50;
    }

    public void land() {
        currentHeight = 0;
    }
}
