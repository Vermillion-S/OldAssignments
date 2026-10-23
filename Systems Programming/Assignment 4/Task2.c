#include <stdio.h>
int main(int argc, char const *argv[])
{
    char itemName[40]; // item name
    int quantity; // quantity
    float price; // price

    // input item name
    printf("Enter Item Name: ");
    scanf("%s", &itemName);

    // input quantity
    printf("Enter Quantity: ");
    scanf("%d", &quantity);

    // input price
    printf("Enter price per item: ");
    scanf("%f", &price);

    // Calculate subtotal
    float subtotal = quantity * price;
    // Calculate tax
    float tax = subtotal * 0.07;
    // Calculate total price
    float total = subtotal + tax;

    // Print Data
    printf("------- Receipt	-------");
    printf("\nItem Name  : %10s\n", itemName);
    printf("Quantity   : %10d\n", quantity);
    // Format monetary values ot 2 decimal precision
    printf("Unit Price : $%9.2f\n", price);
    printf("Subtotal   : $%9.2f\n\n", subtotal);
    printf("Tax (7%%)   : $%9.2f\n", tax);
    printf("Total      : $%9.2f\n", total);
    printf("-----------------------");
    return 0;
}
