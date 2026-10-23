public class Problem1 {
    public static void main(String[] args) {
        Customer customer1 = new Customer("John Doe", "444 Street", "555-555-5555", 12, false);

        // Initial Properties

        // Person Properties
        System.out.println("Name: " + customer1.getName());
        System.out.println("Address: " + customer1.getAddress());
        System.out.println("Phone: " + customer1.getPhone());
        // Customer Properties
        System.out.println("Number: " + customer1.getCustomerNumber());
        System.out.println("On-Mailing-List: " + customer1.isOnMailingList());

        // Mutate Properties

        // Person Properties
        customer1.changeName("Jane Doe");
        customer1.changeAddress("445 Drive");
        customer1.changePhone("444-444-4444");
        // Customer Properties
        customer1.changeCustomerNumber(13);
        customer1.changeMailingPreference(true);

        // Updated Properties

        // Person Properties
        System.out.println("Name: " + customer1.getName());
        System.out.println("Address: " + customer1.getAddress());
        System.out.println("Phone: " + customer1.getPhone());
        // Customer Properties
        System.out.println("Number: " + customer1.getCustomerNumber());
        System.out.println("On-Mailing-List: " + customer1.isOnMailingList());
    }
}
