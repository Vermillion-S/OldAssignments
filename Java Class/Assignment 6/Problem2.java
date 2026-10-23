public class Problem2 {
    public static void main(String[] args) {
        PreferredCustomer guy = new PreferredCustomer("Guy McMan", "123 Street", "555-555-555", 2, true, 400.23f);
        
        // Initial Properties

        // Person Properties
        System.out.println("Name: " + guy.getName());
        System.out.println("Address: " + guy.getAddress());
        System.out.println("Phone: " + guy.getPhone());
        // Customer Properties
        System.out.println("Number: " + guy.getCustomerNumber());
        System.out.println("On-Mailing-List: " + guy.isOnMailingList());
        // Preferred Customer Properties
        System.out.println("Purchase Amount: " + guy.getPurchaseAmount());
        System.out.println("Discount Percent: " + guy.getDiscountPercent()+ "%\n");

        // Mutate Properties

        // Person Properties
        guy.changeName("Gal McLady");
        guy.changeAddress("445 Drive");
        guy.changePhone("444-444-4444");
        // Customer Properties
        guy.changeCustomerNumber(3);
        guy.changeMailingPreference(false);
        
        guy.updatePurchaseAmount(1000.12f);

        // Updated Properties

        // Person Properties
        System.out.println("Name: " + guy.getName());
        System.out.println("Address: " + guy.getAddress());
        System.out.println("Phone: " + guy.getPhone());
        // Customer Properties
        System.out.println("Number: " + guy.getCustomerNumber());
        System.out.println("On-Mailing-List: " + guy.isOnMailingList());
        // Preferred Customer Properties
        System.out.println("Purchase Amount: " + guy.getPurchaseAmount());
        System.out.println("Discount Percent: " + guy.getDiscountPercent()+ "%");
    }
}
