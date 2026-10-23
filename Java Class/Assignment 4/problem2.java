public class problem2 {
    public static void main(String[] args) {
        // Initializes Computer die
        int computerScore = 0;
        Die computerDie = new Die();

        // Initializes player die
        int playerScore = 0;
        Die playerDie = new Die();

        System.out.println("Lets Play Dice!");

        // Loops 10 times
        for (int i = 0; i < 10; i++) {
            
            System.out.println("\nRoll " + (i+1) +":");
            // Roll dice
            computerDie.roll();
            playerDie.roll();
            // print values
            System.out.print("Player Rolled a " + playerDie.getval());
            System.out.print(" and the Computer Rolled a " + computerDie.getval() +"\n");

            // Calculate who rolls the higher number
            // and add to score accordingly
            if (playerDie.getval() > computerDie.getval()) {
                System.out.println("Player Wins Round " + (i+1));
                playerScore++;
            } else if (playerDie.getval() < computerDie.getval()) {
                System.out.println("Computer Wins Round " + (i+1));
                computerScore++;
            } else {
                System.out.println("Round was a Tie");
            }
        }

        System.out.println("\nEnd Score of P: " + playerScore + " || C: " + computerScore);
        // Compare score after all rolls to determine who wins
        if (playerScore > computerScore) {
                System.out.println("Player Wins!");
                playerScore++;
            } else if (playerScore < computerScore) {
                System.out.println("Computer Wins!");
                computerScore++;
            } else {
                System.out.println("Game tied");
            }
    }
}
