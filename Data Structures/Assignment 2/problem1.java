import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

public class problem1 {
    // Returns true if it finds an error
    public static boolean bracketError(String code) {
        // Valid characters
        String openers = "([{";
        String closers = ")]}";

        // Create Stack To Save unpaired opening brackets
        GenericStack<Character> unmatchedOpeners = new GenericStack<>();

        for (Character ch : code.toCharArray()) {
            // IF character is a valid opening bracket...
            if (openers.indexOf(ch) != -1) {
                // Add it to the stack
                unmatchedOpeners.push(ch);
            } else if (closers.indexOf(ch) != -1) {
                // If there is no opening bracket to match, then there is an error 
                if (unmatchedOpeners.isEmpty()) {return true;}

                // For Every closing character, it must ALWAYS match the last opening character

                // In the unicode sheet, [] and {} are 2 characters away
                // While ( and ) are 1 character away, while being far apart from the other pairs
                // I'll take advantage of this fact to find if they're the right pair by unicode distance

                if (ch - unmatchedOpeners.pop() > 2) {return true;} // If the pair matches, 
                                                                    // then the matched opener is removed and the program continues
            }
        }
        
        // If there are no more pairs left, then there is no error
        // If there is an unmatched opener left, then there is an error
        return !unmatchedOpeners.isEmpty();
    }
    public static void main(String[] args) {
        // Declare File and read the contents as a string
        Scanner input = new Scanner(System.in);

        System.out.print("Enter file path to check: ");
        try {
            Path filePath = Path.of(input.next());
            String code = Files.readString(filePath);

            if (bracketError(code)) {
                System.out.println("This File has unmatched brackets");
            } else {
                System.out.println("This File has no bracket error");
            }

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {input.close();}
    }
}
