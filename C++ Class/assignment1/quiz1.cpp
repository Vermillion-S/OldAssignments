#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    // Initialize input values //
    float length, width, height;

    // Assign user input //
    cout << "Insert Crate Length: ";
    cin >> length;
    cout << "Insert Crate Width: ";
    cin >> width;
    cout << "Insert Crate Height: ";
    cin >> height;
    
    // Calculate crate info based on user input //
    float volume = length * width * height;
    float cost = volume * 0.23;
    float charge = volume * 0.5;
    float profit = charge - cost;

    // Output Crate Details //
    cout << "\n" << fixed << setprecision(2);
    cout << "Crate Details:\nVolume: " << volume << " cubic units"<< endl;
    cout << "Cost to Produce: $"  << cost << endl;
    cout << "Customer Charge: $" << charge << endl;
    cout << "Profit: $" << profit << endl;

    return 0;
}
