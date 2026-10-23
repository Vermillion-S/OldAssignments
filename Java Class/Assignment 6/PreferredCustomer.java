
// Preferred Customer Class
// Subclass of Customer
public class PreferredCustomer extends Customer{
    // Variables
    private float purchaseAmount;
    

    // Logic for determining discount rate
    private int updateDiscount(float purchaseAmount) {
        if (purchaseAmount < 2000 && purchaseAmount >= 1500) {
            return 7;
        } else if (purchaseAmount < 1500 && purchaseAmount >= 1000) {
            return 6;
        } else if (purchaseAmount < 1000 && purchaseAmount >= 500) {
            return 5;
        } else if (purchaseAmount < 500) {
            return 0;
        } else {return 10;}
    }

    // Constructor
    public PreferredCustomer(String Name, String Address, String Phone_Number, int customerNumber, boolean mailingList, float purchaseAmount){
        // Calls parent constructor
        super(Name, Address, Phone_Number, customerNumber, mailingList);

        this.purchaseAmount = purchaseAmount;
        
        // Variable determined by method instead of passed value
        this.discountPercent = updateDiscount(purchaseAmount);
    }

    private int discountPercent;
    // Accessor Methods
    public float getPurchaseAmount(){
        return this.purchaseAmount;
    }

    public int getDiscountPercent(){
        return this.discountPercent;
    }

    // Mutator method

    public void updatePurchaseAmount(float amount){
        this.purchaseAmount = amount;
        // Purchase amount determines discount percentage
        // So it must be updated as well
        this.discountPercent = updateDiscount(amount);
    }
}
