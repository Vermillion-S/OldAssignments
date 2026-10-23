// Customer Class
// Subclass of Person
public class Customer extends Person{
    // Class Variables
    // Protected instead of private to share with subclasses
    protected int customerNumber;

    protected boolean mailingList;

    // Constructor
    public Customer(String Name, String Address, String Phone_Number, int customerNumber, boolean mailingList){
        
        // Calls parent class constructor
        super(Name, Address, Phone_Number);

        this.customerNumber = customerNumber;

        this.mailingList = mailingList;
    }

    // Accessor Methods

    public int getCustomerNumber(){
        return this.customerNumber;
    }

    public boolean isOnMailingList(){
        return this.mailingList;
    }

    // Mutator Methods

    public void changeCustomerNumber(int Num){
        this.customerNumber = Num;
    }

    public void changeMailingPreference(boolean choice){
        this.mailingList = choice; 
    }
}
