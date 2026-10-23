import java.util.Scanner;

public class Question2 {

    public static void main(String[] args) {
        
        //Create Scanner Object for input
        Scanner input = new Scanner(System.in);

        System.out.print("Enter three points for p0, p1, and p2: ");

        // values for p0
        double x0 = input.nextDouble();
        double y0 = input.nextDouble();

        
        // values for p1
        double x1 = input.nextDouble();
        double y1 = input.nextDouble();

        // values for p2
        double x2 = input.nextDouble();
        double y2 = input.nextDouble();

        // close scanner to prevent data leak
        input.close();

        // calculate relative position based on the given formula
        double result = (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);

        /* for each result, p2 is 
            - left of line  (> 0)
            - on the line   (= 0)
            - right of line (< 0)
        */

        if (result > 0) {
            System.out.println("p2 is on the left side of the line");
        } else if (result == 0) {
            System.out.println("p2 is on the same line");
        } else if (result < 0) {
            System.out.println("p2 is on the right side of the line");
        }
    }
}
