import java.util.Scanner;

public class Question_1 {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        char looper;
        
        String[] options = new String[6];
        
        options[0] = "Cherries";
        options[1] = "Oranges";
        options[2] = "Plums";
        options[3] = "Bells";
        options[4] = "Melons";
        options[5] = "Bars";

        double total_bet = 0.0;
        double total_won = 0.0;

        do {
            
            System.out.print("Enter How much money you want to bet: ");
            double bet = input.nextDouble();
            total_bet += bet;

            String slot1 = options[0 + (int)(Math.random()*6)];
            String slot2 = options[0 + (int)(Math.random()*6)];
            String slot3 = options[0 + (int)(Math.random()*6)];

            System.out.println("|" + slot1 + "||" + slot2 + "||" + slot3 + "|");

            if (slot1.equals(slot2) && slot2.equals(slot3)) {
                System.out.println("You won $" + (bet * 3) + "!");
                total_won += bet * 3;
            }
            else if (slot1.equals(slot2) || slot2.equals(slot3) || slot1.equals(slot3)) {
                System.out.println("You won $" + (bet * 2) + "!");
                total_won += bet * 2;
            }
            else {
                System.out.println("Sorry, you didn't win :(");
            }

            System.out.print("Do you want to play again? (Y/N): ");
            looper = (input.next().charAt(0));
        } while (looper == 'y' || looper == 'Y');

        System.out.println("You bet $" + total_bet + " in this is session, and won $" + total_won);
        input.close();
    }
    
}