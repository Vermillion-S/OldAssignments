import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class problem2 {
    // Function for finding the max freqency
    public static void frequencyMap(ArrayList<Integer> data) {
        // Create new Hashmap for frequency pairs
        Map<Integer, Integer> frequencies = new HashMap<>();

        // Iterate through arraylist
        for (Integer item : data) {
            // If Key already inserted, add 1 to its value
            // otherwise create a new key entry with one more occurance
            // GetOrDefault method: Gets a key's value if it exits, create one if it does not
            frequencies.put(item, frequencies.getOrDefault(item, 0) + 1);
        }

        // Highest frequency value
        final int maxval;

        // Create a collection view containing all frequencies,
        // and take the highest from that set
        maxval = Collections.max(frequencies.values());

        System.out.println("Top frequency");

        // Iterate through Hashmap
        frequencies.forEach((k,v) -> {
            // If the value of the key matches MaxVal...
            if (v == maxval) {
                // Print the values
                System.out.println("Num: " + k + "\tFreq: " + v);
            }
        });
    } 
    public static void main(String[] args) {
        // Arraylist for user input
        ArrayList<Integer> data = new ArrayList<>();

        System.out.print("Input Integers to test for frequency (insert 0 to end)\n>> ");
        // Input Scanner
        Scanner input = new Scanner(System.in);
        try {
            // While there is still input to take...
            while(input.hasNext()) {
                // take integers from input
                Integer Num = input.nextInt();
                // End loopif it is 0
                // Add to arraylist if not
                if (Num != 0) {
                    data.add(Num);
                } else {break;}
            }

            // Once input is taken, input it to frequency function.
            frequencyMap(data);

        } catch (Exception e) {
            // Bad Data Exception
            System.out.println("input correct data type");
        }
        
        // Close input
        input.close();
    }
}
