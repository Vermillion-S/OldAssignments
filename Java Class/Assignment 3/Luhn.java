import java.util.Scanner;

public class Luhn {
    /** Return true if the card number is valid */
    public static boolean isValid(long number) {

        // Card No. should be between 13 and 16 digits
        if (getSize(number) < 13 || getSize(number) > 16) {
            return false;
        }

        // check whether the card number has a valid prefix [4,5,37,6]
        boolean prefixCheck = false;
        if (prefixMatched(number, 4)) {
            prefixCheck = true;
        } else if (prefixMatched(number, 5)) {
            prefixCheck = true;
        } else if (prefixMatched(number, 37)) {
            prefixCheck = true;
        } else if (prefixMatched(number, 6)) {
            prefixCheck = true;
        }

        if (prefixCheck) {
            //Perform Mod 10 Check
            int digitSum = 0;
            digitSum += sumOfDoubleEvenPlace(number);
            digitSum += sumOfOddPlace(number);
            
            return (digitSum % 10 == 0);
        }

        return false;
    }

    /** Get the result from Step 2 */
    public static int sumOfDoubleEvenPlace(long number) {
        String toString = String.valueOf(number);
        int sum = 0;

        //Start at index 2nd to last index and add every second digit afterward
        for (int i = getSize(number) - 2; i >= 0; i-=2) {
            int digit = toString.charAt(i) - '0';
            digit *= 2;
            sum += getDigit(digit);
        }

        return sum;
    }

    /** Return this number if it is a single digit, otherwise,
    *   return the sum of the two digits */
    public static int getDigit(int number) {
        // If the number is more than one digit, return the sum of the two digits instead
        if (number >= 10) {
            return ((number / 10)+(number % 10));
        }
        // otherwise return the number as is
        return number;
    }

    /** Return sum of odd-place digits in number */
    public static int sumOfOddPlace(long number) {
        String toString = String.valueOf(number);
        int sum = 0;
        // Start at last digit, and then add every other digit before it
        for (int i = getSize(number) - 1; i >= 0; i-=2) {
            int digit = toString.charAt(i) - '0';
            sum += getDigit(digit);
        }

        return sum;
    }

    /** Return true if the number d is a prefix for number */
    public static boolean prefixMatched(long number, int d) {
        int prefix = (int) getPrefix(number, getSize(d));

        return (prefix == d);
    }

    /** Return the number of digits in d */
    public static int getSize(long d) {
        String toString = String.valueOf(d);

        return toString.length();
    }
    
    /** Return the first k number of digits from number. If the
    *   number of digits in number is less than k, return number. */
    public static long getPrefix(long number, int k) {
        String toString = String.valueOf(number);
        String result = "";
        if (getSize(number) < k) {
            return number;
        }
        for (int i = 0; i < k; i++) {
            result += toString.charAt(i);
        }

        return Long.parseLong(result);
    }

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Input a card number to be verified: ");
        
        long cardNO =  input.nextLong();

        if (isValid(cardNO)) {
            System.out.println(cardNO + " is valid");
        } else {
            System.out.println(cardNO +"is invalid");
        }
        
        input.close();
    }
}
