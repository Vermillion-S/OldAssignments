#include "simulation.cpp"

using namespace std;

// Space where the main logic is run

int main()
{
    // size inputs
    uint64_t vmem, pmem, pageS;

    // Take input for memory size only once
    cout << "Insert The size of virtual memory: ";
    cin >> vmem;
    cout << "Insert The size of physical memory: ";
    cin >> pmem;
    cout << "Insert The size of a page: ";
    cin >> pageS;

    // Clear Newline
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    if (vmem < 2 || pmem < 2 || pageS < 2) {
        cout << "Value must be a power of 2" << endl;
        return 0;
    }

    // Check if memory values are a power of 2
    if ((vmem & (vmem - 1)) != 0 ||(pmem & (pmem - 1)) != 0 ||(pageS & (pageS - 1)) != 0) {
        cout << "Value must be a power of 2" << endl;
        return 0;
    }

    // Check if page Size is greater than either memory size
    if (pageS > pmem || pageS > vmem) {
        cout << "Page size cannot be greater than physical memory" << endl;
        return 0;
    }
    
    // Initialize simulation environement
    simulation sim(vmem, pmem, pageS);

    // user input line
    string line;
    while (true) {
        cout << "> ";
        // Prevents bad loop
        if (!getline(cin, line)) {
            break;
        }
        // Prevents null input
        if (line.empty()) {
            continue;
        }
        // Take input with stringstream instead of Cin,
        // since we will have multiple pieces of data in the same line
        stringstream ss(line);

        // Data format "op(Char) addr(64int)"
        string op;
        // Take operator
        ss >> op;
        // if exit condition...
        if (op == "END" || op == "end") {
            break; // exit loop
        }
        // Virtual Memory Address
        uint64_t addr;
        // Handle bad input
        if (!(ss >> addr)) {
            cerr << "Invalid line."<< endl;
            continue;
        }

        if (addr +1 > vmem) {
            cerr << "Address outside of memory limit" << endl;
            continue;
        }

        // Get actual operator
        char type = toupper(op[0]);
        // Read command
        if (type == 'R') {
            sim.read(addr); // Read operation call
        }
        else if (type == 'W') {
            sim.write(addr); // Write operation call
        }
        else cerr << "Invalid op (use R or W)." << endl;// Error Handling
    }

    // Print Metadata
    sim.printData();
    return 0;
}