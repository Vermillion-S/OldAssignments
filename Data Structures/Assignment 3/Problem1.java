import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Problem1 {
    // Function for packing the inputed data
    public static void pack(ArrayList<Integer> array) {
        // Sorts the inputed arraylist from smallest to largest
        Collections.sort(array);
        // Array list for the bins
        ArrayList<ArrayList<Integer>> dividedArraylist = new ArrayList<>();
        
        // Counts the cumulative weight added to a bin
        int runningTotal = 0;
        // Temp array for a bin
        ArrayList<Integer> subarray = new ArrayList<>();

        // Iterate through the array
        for (int i = 0; i < array.size(); i++) {
            // value variables
            int val, nextval = 0;
            // get array value
            val = array.get(i);
            // Get the next value if it exists
            if (i+1 != array.size()) {
                nextval = array.get(i + 1);
            } 
            // add val to running total and subarray
            runningTotal += val;
            subarray.add(val);

            // Check if next value will exceed 10 or if it's the last element
            if (nextval == 0 ||  runningTotal + nextval > 10) {
                // add a duplicate of the subarray
                dividedArraylist.add(new ArrayList<>(subarray));
                // clear the subarray
                subarray.clear();
                // clear the running total
                runningTotal = 0;
            }
        }

        // display divided array
        for (int i = 0; i < dividedArraylist.size(); i++) {
            System.out.println("Container " + (i + 1) + " contains objects with weight " + dividedArraylist.get(i));
        }
    }
    public static void main(String[] args) {
        // initialize scanner
        Scanner input = new Scanner(System.in);
        
        // array for inputs
        ArrayList<Integer> unpackedArray = new ArrayList<>();
        // take input for object ammount
        System.out.print("Enter the number of objects: ");
        int numObj = input.nextInt();

        try {
            // take input based on submitted number of objects
            System.out.print("Enter the weights of the objects: ");
            for (int i = 0; i < numObj; i++) {
                // attempt to read input value
                int num = input.nextInt();
                // check if it is valid
                if (num < 1) {throw new Exception("Please use a positive integer");}
                if (num > 10) {throw new Exception("Value exceeds maximum");}
                
                // add to unpacked array
                unpackedArray.add(num);
            }
        // exception handler
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {input.close();}
        
        // call packing function
        pack(unpackedArray);
    }
}
