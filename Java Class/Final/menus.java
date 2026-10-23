import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class menus {
    // Creates array lists to store users and sessions
    public static ArrayList<account> users = new ArrayList<>();
    public static ArrayList<session> sessions = new ArrayList<>();

    // Use a single Scanner for System.in to avoid closing it accidentally
    public static final Scanner input = new Scanner(System.in);

    // File paths for stored data
    public static final String USER_FILE = "data/users.txt";
    public static final String SESSION_FILE = "data/sessions.txt";

    // Reads user data from a file and returns an ArrayList of account objects
    public static ArrayList<account> readUserfromfile(String filename) {

        ArrayList<account> userList = new ArrayList<>();
        try {
            // Open file
            File file = new File(filename);
            // Initialize scanner
            Scanner scanner = new Scanner(file);
            // loop through each line in the file
            while (scanner.hasNextLine()) {
                // Record line
                String line = scanner.nextLine();
                // Split along regex
                String[] data = line.split(",");
                // vaidates data length
                if (data.length == 4) {
                    // pass parameters as new object
                    account user = new account(data[0], data[1], data[2], data[3]);
                    // add object to arraylist
                    userList.add(user);
                }
            }
            // close scanner
            scanner.close();
        } catch (Exception e) {
            System.out.println("Error reading user file: " + e.getMessage());
        }
        
        // return arrayList
        return userList;
    }

    // Reads session data from a file and returns an ArrayList of session objects
    public static ArrayList<session> readSessionfromFile(String filename) {
        // Creates new Arraylist
        ArrayList<session> sessionList = new ArrayList<>();
        try {
            // New file object
            File file = new File(filename);
            // File Scanenr
            Scanner scanner = new Scanner(file);
            // While there is still data to read....
            while (scanner.hasNextLine()) {
                // Read a line of text
                String line = scanner.nextLine();
                // Split data along regex
                String[] data = line.split(",");
                // Validate data length
                if (data.length == 7) {
                    // parse data to set type
                    // and save
                    int sessionId = Integer.parseInt(data[0]);
                    String subject = data[1];
                    String dateTime = data[2];
                    float rate = Float.parseFloat(data[3]);
                    String tutorUsername = data[4];
                    String status = data[5];
                    String studentUsername = data[6];
                    // pass parameters as new object
                    session sess = new session(sessionId, subject, dateTime, rate, tutorUsername, status, studentUsername);
                    // add to arraylist
                    sessionList.add(sess);
                }
            }
            // close scanner
            scanner.close();
        } catch (Exception e) {
            System.out.println("Error reading session file: " + e.getMessage());
        }
       
        // return arraylist
        return sessionList;
    }

    // Writes User data to a text file
    public static void writeUserToFile(String filename, ArrayList<account> users) {
        // Create file writer
        try (FileWriter writer = new FileWriter(filename);) {
            // iterate through arraylist
            for (account user : users) {
                // write data values to line
                writer.write(user.getName() + "," + user.getEmail() + "," + user.getUsername() + "," + user.getRole() + "\n");
            }
        } catch (Exception e) {
            System.out.println("Error writing user file: " + e.getMessage());
        }
    }
    // Writes Session data to a text file
    public static void writeSessionToFile(String filename, ArrayList<session> sessions) {
        // Create file writer
        try (FileWriter writer = new FileWriter(filename);) {
            // iterate through arraylist
            for (session sess : sessions) {
                // write data values to line
                writer.write(sess.getSessionId() + "," + sess.getSubject() + "," + sess.getDate() + "," + sess.getRate() + "," + sess.getTutorUsername() + "," + sess.getStatus() + "," + sess.getStudentUsername() + "\n");
            }
        } catch (Exception e) {
            System.out.println("Error writing session file: " + e.getMessage());
        }
    }
    
    // Main menu
    public static void front_page() {
        System.out.print("\033[H\033[2J");
        System.out.print("""
        ================================================         
          ______      __             __    _       __  
         /_  __/_  __/ /_____  _____/ /   (_)___  / /__
          / / / / / / __/ __ \\/ ___/ /   / / __ \\/ //_/
         / / / /_/ / /_/ /_/ / /  / /___/ / / / / ,<   
        /_/  \\__,_/\\__/\\____/_/  /_____/_/_/ /_/_/|_|  
        
        ================================================                                             
        """);
        
        // menu loop
        while (true) {
            // Display account login options
            System.out.println("\nLogin as one of the following users");
            for (int i = 0; i < users.size(); i++) {
                account User = users.get(i);
                System.out.println((i + 1) + ")-| " + User.getName() + " [" + User.getRole() + "]");
            }

            System.out.print("\nInput -1 to exit\n>> ");

            try {
                // User input for menu
                int choice;
                // if next input is an integer
                if (input.hasNextInt()) {
                    // take integer
                    choice = input.nextInt();
                    input.nextLine(); // consume the newline
                } else {
                    // otherwise throw exception
                    input.nextLine(); // consume invalid input
                    throw new Exception("Invalid input. Please enter a number.");
                }

                // Escape Case
                if (choice == -1) {
                    System.out.println("Exiting....");
                    break;
                } else if (choice <= 0 || choice > users.size()) {
                    // exeption if choice is out of bounds
                    throw new Exception("Invalid Choice");
                } else {
                    // Set selected user to attempt
                    account userAttempt = users.get(choice - 1);

                    System.out.print("Enter username for " + userAttempt.getName() + ":\n>> ");
                    // Username attempt
                    String attempt;
                    // if next input exists
                    if (input.hasNextLine()) {
                        // take input
                        attempt = input.nextLine();
                        // Exception on blank input
                        if (attempt.isEmpty()) {
                            throw new Exception("Invalid input. Please enter a valid username.");
                        }
                    } else {
                        // exception on bad datatype
                        throw new Exception("Invalid input. Please enter a valid username.");
                    }
                    // Attempt login...
                    if (userAttempt.login(attempt)) {
                        // Access menu on success
                        System.out.println("Login Successfull!");
                        roleAccess(userAttempt);
                    } else {
                        // Exception on failure
                        throw new Exception("Invalid Username");
                    }
                }
              // Exception Hanlder
            } catch (Exception e) {
                System.out.println("[ERROR]: " + e.getMessage());
            }
        }
    }

    // Menu for admin type users
    public static void admin_menu(account activeUser) {
        System.out.print("\033[H\033[2J");
        while (true) {
            // Display menu options
            System.out.println("Welcome " + activeUser.getName());
            System.out.println("Choose a menu option:");
            System.out.print("(1) Create Account\n(2) Delete Account\n(3) View Users Report\n(4) View Sessions Report\n(5) Logout\n>> ");

            try {
                // Take menu option
                int choice;
                // Ensure input is an integer
                if (input.hasNextInt()) {
                    choice = input.nextInt();
                    input.nextLine(); // consume newline
                } else {
                    // Throw exeption on bad data type
                    input.nextLine();
                    throw new Exception("Invalid input. Please enter a number.");
                }
                switch (choice) {
                    // Create user account
                    case 1 -> {
                        // Input namee
                        System.out.print("Enter Name for new account:\n>> ");
                        String name = input.nextLine();
                        // Input Email
                        System.out.print("Enter Email for new account:\n>> ");
                        String email = input.nextLine();
                        // Input Username
                        System.out.print("Enter username for new account:\n>> ");
                        String username = input.nextLine();
                        // Compare username to existing ones to ensure no repeats
                        for (account user : users) {
                            // Throw exception on repeat
                            if (user.getUsername().equals(username)) {
                                throw new Exception("Username already exists! Please choose a different username.");
                            }
                        }
                        // Input Role
                        System.out.print("Enter role for new account (Admin/Tutor/Student):\n>> ");
                        String role = input.nextLine();
                        // Must enter correct role type
                        if (!role.equals("Admin") && !role.equals("Tutor") && !role.equals("Student")) {
                            throw new Exception("Invalid role! Please enter Admin, Tutor, or Student.");
                        }
                        // Create new account object and add it to arrayList
                        users.add(new account(name, email, username, role));
                        System.out.println("Account created successfully!");
                    }
                    // Delete user case
                    case 2 -> {
                        // Select username
                        System.out.print("Enter username of account to delete:\n>> ");
                        String username = input.nextLine();
                        boolean found = false;
                        // Make sure username does not match active user
                        if (username.equals(activeUser.getUsername())){
                            throw new Exception("You cannot delete yourself");
                        }
                        // Search for matching username
                        for (int i = 0; i < users.size(); i++) {
                            // on match...
                            if (users.get(i).getUsername().equals(username)) {
                                // repeat username to confirm deletion
                                System.out.print("Type username again to confirm deletion:\n>> ");
                                String confirm = input.nextLine();
                                if (confirm.equals(username)){
                                    // delete user
                                    users.remove(i);
                                    System.out.println("Account deleted successfully!");
                                }
                                // Declare user was found
                                found = true;
                                // terminate loop
                                break;
                            }
                        }
                        // Message for if account wasnt found
                        if (!found) {
                            throw new Exception("Account not found!");
                        }
                    }
                    // User Report Case
                    case 3 -> {
                        System.out.println("Users Report:");
                        // Incase of no users in list
                        if (users.isEmpty()) {
                            System.out.println("No users available.");
                            break;
                        }
                        // Iterates through user arrayList
                        for (account user : users) {
                            // Calls userReport generator
                            user.reportGenerator();
                        }
                        // PRints total users
                        System.out.println("Total Users: " + users.size());
                    }
                    // Session Report Case
                    case 4 -> {
                        System.out.println("Sessions Report:");
                        System.out.println("----------------------------");
                        // Case of empty session Arraylist
                        if (sessions.isEmpty()) {
                            System.out.println("No sessions available.");
                            break;
                        }
                        // Iterate Trhough session objects
                        for (session session : sessions) {
                            // Call session generator method
                            session.reportGenerator();
                            System.out.println("----------------------------");
                        }
                        // Print sessions length
                        System.out.println("Total Sessions: " + sessions.size());
                    }
                    // Escape case
                    case 5 -> {
                        System.out.println("Logging out...");
                        return;
                    }
                    // bad input case
                    default -> {
                        throw new Exception("Invalid choice! Please try again.");
                    }
                }
                // Exception Handler
            } catch (Exception e) {
                System.out.println("[ERROR]: " + e.getMessage());
            }
        }
    }

    // Logic for Tutor Menu
    public static void tutor_menu(account activeUser) {
        System.out.print("\033[H\033[2J");
        while (true) {
            // Display menu options
            System.out.println("Welcome " + activeUser.getName());
            System.out.println("Choose a menu option:");
            System.out.print("(1) List Availability\n(2) Remove Availability\n(3) View My Sessions\n(4) Logout\n>> ");
            try {
                // Take user input
                int choice;
                // Validate data type
                if (input.hasNextInt()) {
                    choice = input.nextInt();
                    input.nextLine();
                } else {
                    //exception on bad datatype
                    input.nextLine();
                    throw new Exception("Invalid input. Please enter a number.");
                }
                // Menu
                switch (choice) {
                    // List availability Case
                    case 1 -> {
                        // Input Subject
                        System.out.print("Enter subject for availability:\n>> ");
                        String subject = input.nextLine();
                        // Input Date
                        System.out.print("Enter date and time for availability (in format 'yyyy-MM-dd HH:mm'):\n>> ");
                        String dateTime = input.nextLine();
                        // Input Rate
                        System.out.print("Enter rate for session:\n>> ");
                        float rate;
                        // validate datatype
                        if (input.hasNextFloat()) {
                            rate = input.nextFloat();
                            input.nextLine();
                        } else {
                            //exception on bad datatype
                            input.nextLine();
                            throw new Exception("Invalid input. Please enter a valid rate.");
                        }
                        // Set status
                        String status = "Open";
                        // Blank student
                        String studentUsername = " ";
                        // New id
                        int sessionId = sessions.size() + 1;
                        // Create new session object and add it to Arraylist
                        sessions.add(new session(sessionId, subject, dateTime, rate, activeUser.getUsername(), status, studentUsername));
                        System.out.println("Availability added successfully!");
                    }
                    // Remove Availability case 
                    case 2 -> {
                        // Select session id
                        System.out.print("Enter session ID to remove availability:\n>> ");
                        int sessionId;
                        // validate datatype
                        if (input.hasNextInt()) {
                            sessionId = input.nextInt();
                            input.nextLine();
                        } else {
                            input.nextLine();
                            throw new Exception("Invalid input. Please enter a valid session ID.");
                        }
                        boolean found = false;
                        // Search session arraylist for match
                        for (int i = 0; i < sessions.size(); i++) {
                            session sessAttempt = sessions.get(i);
                            // Ensure id matches AND Active User owns it
                            if (sessAttempt.getSessionId() == sessionId && sessAttempt.getTutorUsername().equals(activeUser.getUsername())) {
                                System.out.println("Availability removed successfully!");
                                // remove if found
                                sessions.remove(i);
                                found = true;
                                break;
                            }
                        }
                        // message on not found
                        if (!found) {
                            System.out.println("Session not found or you are not the tutor for this session!");
                        }
                    }
                    // View sessions case
                    case 3 -> {
                        System.out.println("My Sessions:");
                        boolean hasSessions = false;
                        // iterate session objects
                        for (session sess : sessions) {
                            // IF active user owns session...
                            if (sess.getTutorUsername().equals(activeUser.getUsername())) {
                                hasSessions = true; // set flag
                                sess.reportGenerator(); // call session report generator
                            }
                        }
                        // message on no sessions
                        if (!hasSessions) {
                            System.out.println("No sessions available for you.");
                        }
                    }
                    // Escape Case
                    case 4 -> {
                        System.out.println("Logging out...");
                        return;
                    }
                    // Bad menu option case
                    default -> {
                        throw new Exception("Invalid choice! Please try again.");
                    }
                }
                // Exception Handler
            } catch (Exception e) {
                System.out.println("[ERROR]: " + e.getMessage());
            }
        }
    }

    // Student menu logic
    public static void student_menu(account activeUser) {
        System.out.print("\033[H\033[2J");
        while (true) {
            // Menu Options
            System.out.println("Welcome " + activeUser.getName());
            System.out.println("Choose a menu option:");
            System.out.print("(1) View Available Sessions\n(2) Book Session\n(3) Logout\n>> ");
            try {
                // menu input
                int choice;
                // validate input
                if (input.hasNextInt()) {
                    choice = input.nextInt(); // take input
                    input.nextLine();
                } else {
                    input.nextLine();
                    throw new Exception("Invalid input. Please enter a number.");
                }
                // Menu
                switch (choice) {
                    // Available session case
                    case 1 -> {
                        System.out.println("Available Sessions:");
                        boolean hasSessions = false;
                        // iterate sessions
                        for (session sess : sessions) {
                            // if session is available....
                            if (sess.isAvailable()) {
                                hasSessions = true; // set flag
                                sess.reportGenerator(); // generate report
                            }
                        }
                        // message for no sessions
                        if (!hasSessions) {
                            System.out.println("No available sessions at the moment.");
                        }
                    }
                    // Book session case
                    case 2 -> {
                        // Take input
                        System.out.print("Enter session ID to book:\n>> ");
                        int sessionId;
                        // validate input
                        if (input.hasNextInt()) {
                            sessionId = input.nextInt();
                            input.nextLine();
                        } else {
                            input.nextLine();
                            throw new Exception("Invalid input. Please enter a valid session ID.");
                        }
                        // found flag
                        boolean found = false;
                        // iterate sessions
                        for (session sess : sessions) {
                            // if ID matches AND the session is "Open"
                            if (sess.getSessionId() == sessionId && sess.isAvailable()) {
                                // Set active User to student
                                sess.changeStudent(activeUser.getUsername());
                                sess.toggleStatus(); // set status to "Closed"
                                System.out.println("Session booked successfully!");
                                found = true; // set flag
                                break;
                            }
                        }
                        // Message for not found
                        if (!found) {
                            System.out.println("Session not found or already booked!");
                        }
                    }
                    // escape case
                    case 3 -> {
                        System.out.println("Logging out...");
                        return;
                    }
                    // bad menu option case
                    default -> {
                        throw new Exception("Invalid choice! Please try again.");
                    }
                }
                //exception handler
            } catch (Exception e) {
                System.out.println("[ERROR]: " + e.getMessage());
            }
        }
    }

    // Role access function
    public static void roleAccess(account activeUser) {
        // Gets role of active user, 
        // and redirects them to the relevant menu
        switch (activeUser.getRole()) {
            case "Tutor" -> tutor_menu(activeUser);
            case "Admin" -> admin_menu(activeUser);
            case "Student" -> student_menu(activeUser);
        }
    }

    public static void main(String[] args) {
        // Fill arrayLists with file content
        users = readUserfromfile(USER_FILE);
        sessions = readSessionfromFile(SESSION_FILE);

        // Call main menu
        front_page();
        input.close();
        //Execute closing code

        // save changes from arraylist to data files
        writeUserToFile(USER_FILE, users);
        writeSessionToFile(SESSION_FILE, sessions);
    }
}
