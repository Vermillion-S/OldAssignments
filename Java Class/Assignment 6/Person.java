// person class
public class Person {
    // Class Variables
    // Protected instead of private to share with subclasses
    protected String Name;
    protected String Address;
    protected String Phone_Number;

    // Class COnstructor
    public Person(String Name, String Address, String Phone_Number) {
        this.Name = Name;
        this.Address = Address;
        this.Phone_Number = Phone_Number;
    }

    // Accessor Methods

    public String getName(){
        return this.Name;
    }

    public String getAddress(){
        return this.Address;
    }

    public String getPhone(){
        return this.Phone_Number;
    }

    // Mutator Methods

    public void changeName(String Name) {
        this.Name = Name;
    }

    public void changeAddress(String Address) {
        this.Address = Address;
    }

    public void changePhone(String Number) {
        this.Phone_Number = Number;
    }
}
