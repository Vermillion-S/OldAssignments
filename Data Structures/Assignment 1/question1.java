
import java.util.Scanner;

public class question1 {
    public static int hex2Dec(String hexString){

        // Ends recursion if the string is empty
        // which means all digits have been converted
        if (hexString.isEmpty()) {
            return 0;
        }

        // Last digit of the hexidecimal, which we convert first
        char lastDigit = Character.toUpperCase(hexString.charAt(hexString.length()-1));

        // Save remaining digits to convert later
        String remainingDigits = hexString.substring(0, hexString.length() -1);

        // variable for the converted digit
        int convertedDigit = 0;

        // If the digit is a decimal value....
        if (lastDigit>= '0' && lastDigit <= '9'){
            // Convert it to the proper integer
            convertedDigit = lastDigit - '0';
        }
        // If the digit is between A-F....
        else if (lastDigit >= 'A' && lastDigit <= 'F'){
            // Get relative value and add ten, since A-F == 11-16
            convertedDigit = lastDigit - 'A' + 10;
        }
        else {
            // exception if digit outside of hex bounds
            throw new IllegalArgumentException("Enter a valid hexidecimal");
        } 

        // converts the remaining digits
        // multiply the next conversion by 16 to account for new base
        // add the previously converted digit
        // returns fully converted hex at end of recursion
        return hex2Dec(remainingDigits) * 16 + convertedDigit;

    }
    public static void main(String[] args) {
        // Initialize scanner
        try(Scanner input = new Scanner(System.in);){
            
            // Take user input
            System.out.print("Enter a hexidecimal value to convert:\n>> ");
            String hex = input.next();

            // Display converison
            System.out.println("The decimal conversion of " + hex + " is: " + hex2Dec(hex));
        } catch (Exception e){
            System.out.println(e.getMessage()); // exception message
        }
    }
}
