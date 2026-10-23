public class account {
    private final String name;
    private final String email;
    private final String username;
    private final String role;
    
    // Constructor
    public account(String Name, String Email, String Username, String Role) {
        this.name = Name;
        this.email = Email;
        this.username = Username;
        this.role = Role;
    }

    // Access Methods

    public String getName() {
        return this.name;
    }

    public String getUsername() {
        return this.username;
    }

    public String getEmail() {
        return this.email;
    }


    public String getRole() {
        return this.role;
    }

    // Compares string to active username and returns a boolean value
    public boolean login(String userAttempt) {
        return this.username.equals(userAttempt);
    }

    // Generates a user report
    public void reportGenerator() {
        System.out.println("Name: " + this.name + ", Email: " + this.email + ", Role: " + this.role);
    }
}