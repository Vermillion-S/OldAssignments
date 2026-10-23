public class Player {
    // Player name
    String name;
    // Associated die
    private final Die die;
    // Current score
    private int score;

    // Constructor
    public Player(String name){
        // Sets name
        this.name = name;
        // Creates new die object
        this.die = new Die();
        // Starts player with a score of 50
        this.score = 50;
    }

    // Plays 1 round
    public void play(){
        System.out.println(this.name + " Roll!");
        // Rolls die
        this.die.roll();
        // Saves roll val to variable
        int roll = this.die.getval();
        System.out.println(this.name + " Rolled a " + roll);
        // Adds to score if it overshoots 1
        if (this.score - roll < 1) {
            this.score += roll;
            // Otherwise subtracts from score
        } else {this.score -= roll;}

        System.out.println(this.name + "'s score is now " + this.score);
    }
    // Method for accessing score
    public int getscore() {
        return this.score;
    }
}
