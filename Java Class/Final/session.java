public class session {
    private final int sessionId;
    private String subject;
    private String dateTime;
    private float rate;
    private final String tutorUsername;
    private String status;
    private String studentUsername;


    public session(int sessionId, String subject, String dateTime, float rate, String tutorUsername, String status, String studentUsername) {
        this.sessionId = sessionId;
        this.subject = subject;
        this.dateTime = dateTime;
        this.rate = rate;
        this.tutorUsername = tutorUsername;
        this.status = status;
        this.studentUsername = studentUsername;
    }

    // Accessor Methods //

    public int getSessionId() {
        return this.sessionId;
    }

    public String getSubject() {
        return this.subject;
    }

    public String getDate() {
        return this.dateTime;
    }

    public float getRate() {
        return this.rate;
    }

    public String getTutorUsername() {
        return this.tutorUsername;
    }

    public String getStatus() {
        return this.status;
    }

    public boolean isAvailable() {
        return this.status.equals("Open");
    }

    public String getStudentUsername() {
        return this.studentUsername;
    }

    // Mutator Methods //

    public void changeSubject(String newVal) {
        this.subject = newVal;
    }

    public void changeTime(String newVal) {
        this.dateTime = newVal;
    }

    public void changeRate(float newVal) {
        this.rate = newVal;
    }

    public void changeStudent(String newVal) {
        this.studentUsername = newVal;
    }

    public void toggleStatus() {
        // IF status is open
        if (this.status.equals("Open")) {
            // Set it to booked
            System.out.println("Session " + this.sessionId + " is now booked");
            this.status = "Booked";
        } else {
            // If it's booked, set it to open
            System.out.println("Session " + this.sessionId + " is now open");
            this.status = "Open";
            // Clear student username
            this.studentUsername = " ";
        }
    }

    // Generates Report
    public void reportGenerator() {
        System.out.println("==========================");
        System.out.println("ID: " + this.sessionId);
        System.out.println("Subject: " + this.subject);
        System.out.println("Date: " + this.dateTime);
        System.out.println("Rate: $" + this.rate + "/hr");
        System.out.println("Tutor: " + this.tutorUsername);
        System.out.println("Status: " + this.status);
        System.out.println("Student: " + this.studentUsername);
        System.out.println("==========================");
    }

}
