public class problem1 {
    public static void main(String[] args) {
        
        // Creates Player 1
        Player player1 = new Player("Player 1");
        // Creates Player 2
        Player player2 = new Player("Player 2");

        // Loop for the game, keeps going until 
        // one of the players have a score of 1
        while (true) {
            // Rolls dice and subtracts from score
            player1.play();
            player2.play();

                // Tie if both get to 1 on the same turn
            if (player1.getscore() == 1 && player2.getscore() == 1) {
                System.out.println("The game ended in a draw!");
                break;
              
                // If Player one gets a score of one first
                // They win
            } else if (player1.getscore() == 1) {
                System.out.println(player1.name + " Wins!");
                break;
                // If Player two gets a score of one first
                // They win
            } else if (player2.getscore() == 1) {
                System.out.println(player2.name + " Wins!");
                break;
            }
        }
    }
}
