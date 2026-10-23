import java.util.ArrayList;
import java.util.Scanner;

public class question2 {
    public static <E extends Comparable<E>> E max(ArrayList<E> list){
        // Initializes max value at start of list
        E currentmax = list.get(0);

        // Iterate through list
        for (E val : list) {
            // IF the list value is larger than the current max....
            if (currentmax.compareTo(val) < 0) {
                // It is the new max value
                currentmax = val;
            }
        }
        // Return the final max value of the Arraylist
        return currentmax;
    }
    public static void main(String[] args) {
        
        // Test for integer type

        // Create test array
        ArrayList<Integer> art = new ArrayList<>();

        // Input Message
        System.out.print("Enter a list of integers to test (Newline to finish):\n>> ");

        // New Scanner object
        try (Scanner input = new Scanner(System.in)) {
            // Take input
            String data = input.nextLine();
            // Split data and add it to arraylist
            for (String x : data.split(" ")) {
                art.add(Integer.valueOf(x));
            }

            // Display max value
            System.out.println("The Largest value provided is: " + max(art));
        } catch (Exception e) {
            // Exception of bad data
            System.out.println("Please enter a valid and consistent datatype");
        }
    }
}
