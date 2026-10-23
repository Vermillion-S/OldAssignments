
import java.util.Arrays;
import java.util.Scanner;

public class problem1 {
    // 2d array sorting method
    public static double[][] sortRows(double[][] matrix) {
        // Creates a new matrix
        double[][] newmatrix;
        // copy's original array, for modification
        newmatrix = matrix;

        // Loops through first dimension
        for (double[] row : newmatrix) {
            // sorts the second dimension
            Arrays.sort(row);
        }
        // returns modified matrix
        return newmatrix;
    }
    public static void main(String[] args) {
        // creates empty 3x3 matrix
        double[][] sortable = new double[3][3];
        double[][] sorted;
        
        // Input scanner
        Scanner input = new Scanner(System.in);


        System.out.println("Enter an unsorted 3x3 matrix:");
        // Loop through array and input doubles from user input
        for (int i = 0; i < sortable.length; i++) {
            for (int j = 0; j < sortable[i].length; j++) {
                sortable[i][j] = input.nextDouble();
            }
        }

        // creates sorted matrix through sorting method
        sorted = sortRows(sortable);
        
        System.out.println("The Sorted array is:");
        
        // Prints sorted array
        for (double[] row : sorted) {
            System.out.println(Arrays.toString(row));
        }

        input.close();
    }
}