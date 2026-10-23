import java.util.Random;

public class Die {
    // Die stored values

    // what the dice rolled
    private int currentval;
    // Number of sides
    private final int sides;

    // Die constructor
    public Die() {
        this.currentval = 1;
        this.sides = 6;
    }

    // Medthod for rolling
    public void roll() {
        // creates RNG
        Random random = new Random();
        
        // set current val to an integer between 1-6
        currentval = random.nextInt(sides) + 1;
    }

    // returns current val
    public int getval() {
        return currentval;
    }
}
