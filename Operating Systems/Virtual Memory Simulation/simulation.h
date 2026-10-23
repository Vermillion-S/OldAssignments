#pragma once
#include <cstdint>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <sstream>
#include <string>
#include <limits>


using namespace std;

// Header for Simulation Class

// Default structure for a Page Table Entry
struct page_entry {
    bool present = false; // is frame in memory? 
    int frame = -1; // Frame number of entry
    uint64_t last_access = 0; // for memory caching
    bool dirty = false; // was frame written to?

};

// Virtual Address
struct virtual_Address {
    int pageNumber = -1;
    uint64_t offset = 0;
};

// Physical Address
struct physical_Address {
    int frameNumber = -1;
    uint64_t address = 0;
};

// Structure for a memory entry
struct Page {
    int pageNumber;
    string value;
};

// Structure for A page of Virtual Memory
struct Memory_Frame {
    int VirtualPageNumber; // virtual address of process
    bool occupied; // Does the page exist?
};

class simulation {
    private:
        int pageFaultCount = 0;
        int pageReplacementCount = 0;
        uint64_t vMemSize; // Size of virtual Memory Space
        uint64_t pMemSize; // Size of physical memory space
        uint64_t pageSize; // size of pages

        int numFrames; // Physical Memory Size
        int numVPages; // Virtual memory size

        vector<page_entry> Page_Table; // Page Translation Table

        vector<Memory_Frame> Frames; // Simulated Virtual Memory
        vector<Page> Physical_Memory; // Simulated Physical Memory
        vector<Page> disk; // Simulated Disk

        uint64_t clock = 1; // Simulation Clock

        int pageFault(int virtualPageNumber, char rw); // Page Fault Function

        physical_Address translate(uint64_t vAddress, char r); // Address Translation Function
        
    public:
        simulation(uint64_t vMemSize, uint64_t pMemSize, uint64_t pageSize); // Class Constuctor

        void read(uint64_t virtualAddress); // Read Operation

        void write(uint64_t virtualAddress); // Write Operation

        void printData(); // Metadata Output
};
