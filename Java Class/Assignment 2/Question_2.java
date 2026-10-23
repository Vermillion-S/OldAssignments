import java.util.Scanner;

public class Question_2 {
    public static void main(String[] args) {
        
        //initialize scanner
        Scanner input = new Scanner(System.in);

        //take user input
        System.out.print("Enter the height of the triangle: ");
        int height = input.nextInt();
        
        // loop for each row
        for (int i = 0; i < height - 1; i++) {
            //Prints whitespace for formatting
            for (int j = 0; j < height - i - 1; j++) {
                System.out.print(" ");
            }
            //prevents periods and second star from appearing on the first line
            if (i != 0) {
                //left star
                System.out.print("*");
                //prints periods
                for (int k = 0; k < 2 * i - 1; k++) {
                    System.out.print(".");
                }
            }
            // Right star and new line
            System.out.print("*\n");
        }
        //Prints final line with just stars
        for (int i = 0; i < 2 * height - 1; i++) {
            System.out.print("*");
        }

        input.close();
    }
}
