#include "simulation.h"

// Code for simulation class

// Constructor
simulation::simulation(uint64_t vsize, uint64_t psize, uint64_t pgsize)
    : vMemSize(vsize), pMemSize(psize), pageSize(pgsize) {
    // take parameter input
    this->vMemSize = vMemSize;
    this->pMemSize = pMemSize;
    this->pageSize = pageSize;

    // Set frame and page amount based on memory size
    this->numFrames = pMemSize / pageSize;
    this->numVPages = (vMemSize + pageSize - 1) / pageSize;

    // Resize tables to match maximum allowed values
    this->Page_Table.resize(this->numVPages);
    this->Frames.resize(this->numFrames);
    this->Physical_Memory.resize(this->numFrames);

    // Set all Pages as blank by default
    for (uint64_t i = 0; i < this->numFrames; i++)
    {
        this->Frames[i].occupied = false;
        this->Frames[i].VirtualPageNumber = -1;
    }

    // Initialize counters and clock
    this->pageFaultCount = 0;
    this->pageReplacementCount = 0;
    this->clock = 0;
}

// handle data that has not been loaded
int simulation::pageFault(int virtualPageNumber, char rw) {
    // Increase Page Default Stat
    pageFaultCount++;

    cout << "Address has no associated entry at virtual page " << virtualPageNumber << endl;
    
    // Temporary Page to load from disk
    Page tempPage = {-1, ""};

    // Check The disk for the page entry
    for (int i = 0; i < this->disk.size(); i++)
    {
        if (this->disk[i].pageNumber == virtualPageNumber){
            tempPage = this->disk[i];
            cout << "Page found on disk. Now Loading to memory" << endl;
            break;
        }
    }

    // cant read a nonexistent entry
    if (tempPage.pageNumber == -1 && rw == 'R') {
        cout << "Page does not exist, try creating a new entry" << endl;
        return -1;
    }
    

    // check for open frames in virtual stack
    int frame = -1;
    for (uint64_t i = 0; i < this->numFrames; i++)
    {
        // If the frame is open, select it as 
        // the frame we want to allocate the virtual page to
        if (!this->Frames[i].occupied)
        {
            frame = i;
            cout << "Free space found at frame " << frame << ". Allocating to virtual page " << virtualPageNumber << endl;
            break;
        }
    }

    // If there are no empty frames, replace an existing one
    // Using the LRU algorithm
    if (frame == -1) {
        this->pageReplacementCount++; // Increase Page Replacement Count
        cout << "No free space found, overwriting the least used address" << endl;
        // The smaller the number, the older it is
        uint64_t oldestTime = ULLONG_MAX;

        // Indexes of the oldest page in main memory
        int oldestFrame = -1;
        int oldestPageNumber = -1;

        // Iterate through the page table
        for (uint64_t i = 0; i < this->numVPages; i++){
            // active page
            page_entry tempEntry = Page_Table[i];

            // If the page is present and older than the current oldest
            if(tempEntry.present && tempEntry.last_access < oldestTime) {
                // make it the new oldest page
                oldestTime = tempEntry.last_access;
                oldestPageNumber = i;
                oldestFrame = tempEntry.frame; 
            }
        }
        cout << "Oldest page exists on frame " << oldestFrame << ". Overwritting" << endl;

        // Write The Soon to be replaced frame to the disk if it is "Dirty"
        if (oldestPageNumber != -1 && this->Page_Table[oldestPageNumber].dirty) {
            bool existing = false;
            cout << "Replaced frame has been written to, saving contents to disk" << endl;
            // if the disk already has a copy...
            for (auto &page : this->disk)
            {
                if(page.pageNumber == oldestPageNumber) {
                    // update it
                    page.value = this->Physical_Memory[this->Page_Table[oldestPageNumber].frame].value;
                    existing = true;
                }
            }
            // Otherwise make a new entry
            if (!existing) {
                this->disk.push_back(this->Physical_Memory[this->Page_Table[oldestPageNumber].frame]);
            }
        }
        // Assign the frame as the one we want our requested page to exist on
        frame = oldestFrame;

        // Mark the old page as not present in the Page table
        if (oldestPageNumber != -1) {
            this->Page_Table[oldestPageNumber].present = false;
        }
    }

    
    if (rw == 'W' && tempPage.pageNumber == -1) {
        tempPage.pageNumber = virtualPageNumber; // new entry value if it doesn't already exist
    } 

    // Assign page to the frame
    this->Physical_Memory[frame] = tempPage;

    // in the selected frame slot...
    //Load virtual page number into active memory
    this->Page_Table[virtualPageNumber].present = true; // info is loaded in memory
    this->Page_Table[virtualPageNumber].frame = frame; // frame associated with virtual mem
    this->Page_Table[virtualPageNumber].dirty = (rw == 'W'); // mark dirty if write
    this->Page_Table[virtualPageNumber].last_access = clock; // time accessed

    // overwrite frame
    this->Frames[frame].occupied = true; // frame contains data
    this->Frames[frame].VirtualPageNumber = virtualPageNumber; // associated page number

    clock++; // tick clock

    return 1;
};

// translates the virtual address into a physical address
physical_Address simulation::translate(uint64_t vAddress, char rw) {
    // create working addresses 
    virtual_Address va;
    physical_Address pa;

    // Decode the virtual address into page number and offset
    va.pageNumber = vAddress / this->pageSize;
    cout << "Address " << vAddress << " is associated to Virtual Page " << va.pageNumber << endl;
    va.offset = vAddress % this->pageSize;

    // Check if the selected virtual page is present
    // In main memory
    if (!this->Page_Table[va.pageNumber].present) {
        // If not, handle page fault
        int pfResult = pageFault(va.pageNumber, rw);
        if (pfResult == -1) {
            // Push invalid frame on failed page fault
            pa.frameNumber = -1;
            pa.address = 0;
            return pa;
        }
    }

    // After page fault is resolved.....

    // Get frame number of physical address
    pa.frameNumber = this->Page_Table[va.pageNumber].frame;
    
    // Translate address to the physical equivalent
    pa.address = pa.frameNumber * pageSize + va.offset; 

    // update access tick
    this->Page_Table[va.pageNumber].last_access = this->clock++;
    
    // Return the physical address
    return pa;
}

void simulation::read(uint64_t virtualAddress) {
    // call memory from virtual address
    physical_Address pa = translate(virtualAddress, 'R');
    if (pa.frameNumber != -1) {
        cout << "The address " << virtualAddress << " associated with the Frame " << pa.frameNumber << " contains the value " << this->Physical_Memory[pa.frameNumber].value << endl;
    } else {
        cout << "Read failed: invalid address." << endl;
    }

}

// Read data from address
void simulation::write(uint64_t virtualAddress) {
    // call memory from virtual address
    std::cout << "Attempting to write to the address: " << virtualAddress << endl;
    physical_Address pa = translate(virtualAddress, 'W');
    if (pa.frameNumber == -1) {
        cout << "Write failed: invalid address." << endl;
        return;
    }
    cout << "Address has been translated to the Frame: " << pa.frameNumber << endl;
    cout << "Access secured! What did you want to write?\n> ";
    cin >> this->Physical_Memory[pa.frameNumber].value;
    cout << "Data has been written to memory. Marking page as dirty to save to disk" << endl;
    // mark written data as "Dirty"
    this->Page_Table[virtualAddress/this->pageSize].dirty = true;
    return;
};

void simulation::printData() {
    cout << "Memory Access Count:     " << this->clock << "\n" << endl;
    cout << "Page Fault Count:        " << this->pageFaultCount << endl;
    cout << "Page ReplacementCount:   " << this->pageReplacementCount << endl;
    if (clock == 0) {
        cout << "Page Fault Percentage: N/A (no operations performed)" << endl;
    } else {
        cout << "Page Fault Percentage: %" << ((float)pageFaultCount / (float)clock) * 100 << endl;
    }

    int pagecount = 0;

    for (auto &page : this->Page_Table)
    {
        if (page.present) {
            pagecount++;
        }
    }
    
    cout << "Number of pages created: " << pagecount << endl;
}