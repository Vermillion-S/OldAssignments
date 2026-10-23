from collections import OrderedDict
from random import random, sample

test = False ## To help with my testing

## Contains actual file content
class Disk:
    def __init__(self, cylinders, track_sectors, block_size):
        # Disk Cylinders
        self.cylinders = cylinders
        # Tracks per cylinder
        self.trackSectors = track_sectors
        # Size of memory blocks
        self.blockSize = block_size

        # Number of blocks is cylinders * trackSectors; 
        # each block is a bytearray represented by a byte array
        self.blocks = [bytearray(self.blockSize) for _ in range(self.cylinders * self.trackSectors)]

    ## Finds what cylinder a block of data is on (for Disk Scheduler)
    def blockCylinder(self, blockNum):
        # Exception Hanlder
        if blockNum < 0 or blockNum >= self.cylinders * self.trackSectors:
            raise ValueError("Block number out of range")
        # Returns cylinder of block
        return blockNum // self.trackSectors

    # Get block data
    def read(self, blockNum):
        return bytes(self.blocks[blockNum])

    # Set block data
    def write(self, blockNum, data):
        ## Create a new byteArray
        temp = bytearray(self.blockSize)
        
        # Fill byteArray (clipping what doesnt fit)
        temp[:len(data)] = data

        ## Replace block with new data
        self.blocks[blockNum] = temp

## Cache for recently accessed files
class Buffer:
    def __init__(self, capacity):
        # Size of buffer
        self.capacity = capacity
        # Contains disk data.
        # Ordered for LRU
        self.storage = OrderedDict()
        # Count of found buffers calls
        self.hits = 0
        # Count of missed buffer calls
        self.misses = 0

    # Find datablock in buffer
    def get(self, blockNums):
        # Accepts int or an int list.
        # If given a list, return data only if all blocks are cached.
        if isinstance(blockNums, list):
            if not blockNums: # empty list case
                self.misses += 1
                return None
            # check that all requested blocks are present
            if all(block in self.storage for block in blockNums):
                # mark each block as recently used (LRU)
                for block in blockNums:
                    self.storage.move_to_end(block)
                # hit
                self.hits += 1
                # Return file data concatenated to a single bytearray
                return b''.join(
                    bytes(self.storage[block]) if not isinstance(self.storage[block], (bytes, bytearray)) else self.storage[block]
                    for block in blockNums
                )
            else:
                # Miss
                self.misses += 1
                return None
        else:
            # int case
            if blockNums in self.storage:
                # Move to end to mark as recently used (LRU)
                self.storage.move_to_end(blockNums)
                # Hit
                self.hits += 1
                # Return the file data
                return self.storage[blockNums]
            else:
                # Miss
                self.misses += 1
                return None
    
    # Add data to buffer
    def put(self, blockNum, data):
        # Update if block already exists in buffer
        if blockNum in self.storage:
            # Update existing block and mark as recently used
            self.storage.move_to_end(blockNum)
        
        self.storage[blockNum] = data
        # If storage is full...
        if len(self.storage) > self.capacity:
            # Remove least recently used block [the first one] (LRU)
            self.storage.popitem(last=False)

    ## Returns buffer statistics
    def summary(self):
        hitrate = self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': f"{hitrate * 100}%"
        }

## Object to hold diskScheduler statistics
class DiskStats:
    def __init__(self):
        self.maxCylinders = 0
        self.headMovement = 0
        self.accessCount = 0  # Counter instead of timestamps
        self.utilization = 0.0
        
        self.seekTimes = []

    ## Returns disk scheduler stats
    def summary(self):
        total_seek_time = sum(self.seekTimes)
        avg_seek = sum(self.seekTimes) / len(self.seekTimes) if self.seekTimes else 0
        # utilization calculation based on idle time
        self.utilization = total_seek_time / (self.maxCylinders * self.accessCount) if self.accessCount > 0 else 0.0
        return {
            'total_head_movement': self.headMovement,
            'accesses': self.accessCount,
            'avg_seek_time': f"{avg_seek:.2f}",
            'utilization': f"{self.utilization * 100:.2f}%"
        }

# Schedules Disk Requests
class DiskScheduler:
    def __init__(self, disk: Disk, algorithm: str = 'FCFS'):
        # Working Disk
        self.disk = disk
        # Position of the disk reader, start random
        self.headPos = int(random() * disk.cylinders)
        # logging info
        self.stats = DiskStats()
        # Scheduling algorithm
        self.algorithm = algorithm
        # Counter for operations
        self.opCount = 0
        self.stats.maxCylinders = disk.cylinders

    ## Calls the scheduling algorithm
    def schedule(self, requests: list[int], algorithm: str = 'FCFS'):
        algo = algorithm.upper()
        ## calls strategies in schedule call
        strategies = {
            'FCFS': self.fcfs,
            'SSTF': self.sstf,
            'SCAN': self.scan,
            'C-SCAN': self.cscan,
            'CSCAN': self.cscan
        }

        if algo not in strategies:
            raise ValueError(f"Unknown algorithm: {algorithm}")

        # Use the selected strategy to get optimal request order
        ordered_requests = []

        ordered_requests = strategies[algo](requests)
        
        # Update utilization based on total accesses
        total_accesses = len(requests)
        if total_accesses > 0:
            utilization = total_accesses / self.opCount
            self.stats.utilization = utilization
            
        return ordered_requests
    
    ## Simulates accessing a block (updates head position and stats)
    def simulate_access(self, blockNum):
        try:
            cylinder = self.disk.blockCylinder(blockNum)
            self.opCount += 1
            self.stats.accessCount += 1
            seek_time = abs(self.headPos - cylinder)
            self.headPos = cylinder
            self.stats.headMovement += seek_time
            self.stats.seekTimes.append(seek_time)
            
        except Exception as e:
            print(f"Error in simulating access for block {blockNum}: {str(e)}")
            raise

    def rotate_head(self, steps):
        # Compute a rotated position without logging seek events (useful for wrap-around logic).
        newPos = (self.headPos + steps) % self.disk.cylinders
        return newPos

    ## Sends disk read request
    def request(self, blockNum):
        try:
            data = self.disk.read(blockNum)
            return data
        except Exception as e:
            print(f"Error in disk request for block {blockNum}: {str(e)}")
            raise
        
    # First come first serve
    def fcfs(self, requests):
        ordered_requests = []
        for req in requests:
            # Simulate access to update stats
            self.simulate_access(req)
            ordered_requests.append(req)
        return ordered_requests

    # Shortest seek time first
    def sstf(self, requests):
        ordered_requests = []
        pending_requests = requests.copy()
        while pending_requests:
            # Find closest request based on cylinder distance
            closest_req = min(pending_requests, key=lambda req: abs(self.disk.blockCylinder(req) - self.headPos))
            # Simulate access to update stats
            self.simulate_access(closest_req)
            ordered_requests.append(closest_req)
            pending_requests.remove(closest_req)
        return ordered_requests

    # SCAN (Elevator Algorithm)
    def scan(self, requests):
        ordered_requests = []
        direction = 1  # 1 for up, -1 for down
        pending_requests = requests.copy()
        
        while pending_requests:
            # choose candidates in current direction
            if direction == 1:
                candidates = [req for req in pending_requests if self.disk.blockCylinder(req) >= self.headPos]
            else:
                candidates = [req for req in pending_requests if self.disk.blockCylinder(req) <= self.headPos]
            
            # No candidates in current direction, reverse
            if not candidates:
                direction *= -1
                continue
            
            # find the closest candidate
            closest_req = min(candidates, key=lambda req: abs(self.disk.blockCylinder(req) - self.headPos))
            # Simulate access to update stats
            self.simulate_access(closest_req)
            ordered_requests.append(closest_req)
            pending_requests.remove(closest_req)
        return ordered_requests
    
    # Circular SCAN
    def cscan(self, requests):
        ordered_requests = []
        pending_requests = requests.copy()
        
        while pending_requests:
            # Always move in one direction (up)
            candidates = [req for req in pending_requests if self.disk.blockCylinder(req) >= self.headPos]

            ## loop around
            if not candidates:
                # Move head back to start and continue scanning
                self.headPos = 0
                # Simulate the seek to beginning
                self.simulate_access(0)
                continue
            
            # find the closest candidate
            closest_req = min(candidates, key=lambda req: abs(self.disk.blockCylinder(req) - self.headPos))
            # Simulate access to update stats
            self.simulate_access(closest_req)
            ordered_requests.append(closest_req)
            pending_requests.remove(closest_req)

        return ordered_requests

# Virtual Representation for a section of disk memory
class simFile:
    def __init__(self, name, size, blocks, allocation):
        # File Name
        self.name = name
        # size (in bytes)
        self.size = size
        ## blocks the file takes up
        self.blocks = blocks
        ## how its blocks were allocated
        self.allocation = allocation

class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirs = {}
        self.files = {}

class fileSystem:
    def __init__(self, disk: Disk, allocation, diskScheduler: DiskScheduler = None, buffer: Buffer = None):
        self.disk = disk # Working Disk
        self.diskScheduler = diskScheduler # Disk Scheduler
        self.buffer = buffer # Buffer
        self.directory = Directory('/') # Root Directory
        self.freespace = set(range(disk.cylinders * disk.trackSectors)) # Free space tracking
        self.allocation = allocation # Allocation strategy
        self.activeFile = None # Currently opened file
        self.loadedContent = None # Loaded file content
        self.statLog = {} # Statistics log

    def actions(self, operations):
        
        # Map each operation to its blocks
        block_requests = []  # List of tuples: (blockNum, op_idx, command)

        for idx, (command, args) in enumerate(operations):
            blocks = []

            if command == 'write':
                path, content = args
                if isinstance(content, str):
                    content = content.encode('utf-8')
                numBlocks = (len(content) + self.disk.blockSize - 1) // self.disk.blockSize

                # Allocate blocks for scheduling only
                if self.allocation == 'contiguous':
                    sortedFree = sorted(self.freespace)
                    for i in range(len(sortedFree) - numBlocks + 1):
                        if sortedFree[i + numBlocks - 1] - sortedFree[i] == numBlocks - 1:
                            blocks = sortedFree[i:i + numBlocks]
                            break
                elif self.allocation == 'linked':
                    if len(self.freespace) >= numBlocks:
                        blocks = sample(list(self.freespace), numBlocks)

            elif command in ('read', 'open', 'delete'):
                # Get current blocks if file exists
                path = args if isinstance(args, str) else args[0]
                dir_path = '/'.join(path.split('/')[:-1])
                file_name = path.split('/')[-1]
                currentDir = self.transverse(dir_path)
                if file_name in currentDir.files:
                    blocks = currentDir.files[file_name].blocks

            # Only add blocks if they exist
            for b in blocks:
                block_requests.append((b, idx, command))

        # Step 2: Schedule blocks using disk scheduler
        block_nums = [b for b, _, _ in block_requests]
        scheduled_blocks = self.diskScheduler.schedule(block_nums)

        executed_ops = set()

        # Step 3: Execute operations in scheduled block order
        for b in scheduled_blocks:
            for _, op_idx, command in filter(lambda x: x[0] == b, block_requests):
                if op_idx not in executed_ops:
                    command, args = operations[op_idx]
                    if command == 'read':
                        self.read(args)
                    elif command == 'write':
                        self.write(args[0], args[1])
                    elif command == 'delete':
                        self.delete(args)
                    executed_ops.add(op_idx)

        # Step 4: Execute remaining operations with no blocks (e.g., reads immediately after writes)
        for idx, (command, args) in enumerate(operations):
            if idx not in executed_ops:
                if command == 'read':
                    self.read(args)
                elif command == 'write':
                    self.write(args[0], args[1])
                elif command == 'delete':
                    self.delete(args)
                executed_ops.add(idx)


    def translatePath(self, path):
        if not path:
            return ['']
        if path.startswith('/'):
            path = path[1:]
        return path.split('/')

    def transverse(self, path:str):
        currentDir = self.directory
        pathTree = self.translatePath(path)
        for dir in pathTree:
            if dir != '':
                if dir in currentDir.subdirs:
                    currentDir = currentDir.subdirs[dir]
                else:
                    currentDir.subdirs[dir] = Directory(dir)
                    currentDir = currentDir.subdirs[dir]
        return currentDir

    def open(self, path):
        # empty argument check
        if not path:
            raise ValueError("Empty path provided")
        
        ## Convert path to directory and file name
        path_parts = path.split('/')
        file_name = path_parts[-1] # filename
        dir_path = '/'.join(path_parts[:-1]) # directory path
        currentDir = self.transverse(dir_path) # get dictionary of directory

        # Close currently active file
        self.close()

        # Create file if it doesn't exist
        if file_name not in currentDir.files:
            currentDir.files[file_name] = simFile(file_name, 0, [], self.allocation)

        ## set active file
        self.activeFile = currentDir.files[file_name]

        ## if the file has listed blocks, load its content
        if self.activeFile.blocks:
            # Try loading from buffer first
            if self.buffer:
                bufferedData = self.buffer.get(self.activeFile.blocks)
                if bufferedData is not None:
                    self.loadedContent = bufferedData
                    print(f"[open] Loaded content from buffer for file: {self.activeFile.name}")

            # Load from disk if not in buffer
            if self.loadedContent is None:
                data = bytearray()
                for blockNum in self.activeFile.blocks:
                    blockData = self.diskScheduler.request(blockNum)
                    data.extend(blockData)
                self.loadedContent = bytes(data[:self.activeFile.size])
                print(f"[open] Loaded content from disk for file: {self.activeFile.name}")
        else:
            # New file has no content yet
            self.loadedContent = None
            print(f"[open] Created new file: {file_name}")

    ## reads file content
    def read(self, path):
        ## Check if file is already opened.. if not, open it
        if self.activeFile is None or self.activeFile.name != path.split('/')[-1]:
            self.open(path)
        ## result is the loaded content of the active file
        result = self.loadedContent if self.loadedContent is not None else b''
        ## convert to string for printing
        content_str = result.decode('utf-8') if result else ''
        # print content
        print(f"[read] Read \"{content_str}\" ({len(result)} bytes) from file: {self.activeFile.name} at cylinders {self.activeFile.blocks}")
    
    ## writes file content
    def write(self, path, content):
        ## Check if content is string, convert to bytes
        if isinstance(content, str):
            content = content.encode('utf-8')

        ## Check if file is already opened.. if not, open it
        if self.activeFile is None or self.activeFile.name != path.split('/')[-1]:
            self.open(path)

        ## Determine number of blocks needed for new content
        numBlocks = (len(content) + self.disk.blockSize - 1) // self.disk.blockSize
        allocatedBlocks = []

        ## Allocate blocks based on strategy
        if self.allocation == 'contiguous':
            sortedFree = sorted(self.freespace)
            ## check for contiguous space that fits content size
            for i in range(len(sortedFree) - numBlocks + 1):
                if sortedFree[i + numBlocks - 1] - sortedFree[i] == numBlocks - 1:
                    allocatedBlocks = sortedFree[i:i + numBlocks] # allocate blocks
                    break
            if not allocatedBlocks:
                raise MemoryError("Not enough contiguous space available")

        elif self.allocation == 'linked':
            ## check for any free space that fits content size
            if len(self.freespace) < numBlocks:
                raise MemoryError("Not enough space available")
            # Randomize allocation for linked files
            allocatedBlocks = sample(list(self.freespace), numBlocks)
        else:
            raise ValueError("Unknown allocation strategy")

        # Write content into allocated blocks
        for i, blockNum in enumerate(allocatedBlocks):
            ## resize content chunks to block size
            start = i * self.disk.blockSize
            end = start + self.disk.blockSize
            blockData = content[start:end]
            self.disk.write(blockNum, blockData) # write to disk
            self.diskScheduler.request(blockNum) # log access
            self.freespace.remove(blockNum) # mark block as used
            ## update buffer
            if self.buffer:
                self.buffer.put(blockNum, blockData)

        # Update file metadata
        self.activeFile.size = len(content)
        self.activeFile.blocks = allocatedBlocks
        self.loadedContent = content
        print(f"[write] Wrote \"{content.decode('utf-8')}\" ({len(content)} bytes) to cylinders {allocatedBlocks}")

    ## closes active file
    def close(self):
        if self.activeFile is None:
            return
        name = self.activeFile.name
        
        print(f"[close] Closed file: {name}")
        
        # update buffer
        if self.buffer is not None:
            for blockNum in self.activeFile.blocks:
                start = blockNum * self.disk.blockSize
                end = start + self.disk.blockSize
                blockData = self.loadedContent[start:end]
                self.buffer.put(blockNum, blockData)
        self.activeFile = None
        self.loadedContent = None

    ## deletes a file
    def delete(self, path):
        # split path from filename
        dir_path = '/'.join(path.split('/')[:-1])
        file_name = path.split('/')[-1]
        ## get working directory
        currentDir = self.transverse(dir_path)
        ## check if file exists in directory
        if file_name in currentDir.files:
            file = currentDir.files[file_name]
            for blockNum in file.blocks:
                ## dont request, since deletion is an overwriting mechanism
                self.freespace.add(blockNum) ## update free space
            del currentDir.files[file_name]
            print(f"[delete] Deleted file: {file_name}")
        else:
            print(f"[delete] File not found: {file_name}")

def main():
    ## test operations
    testops = [
        ('write', ('/fileA.txt', 'A'*512)),  # 1 block
        ('write', ('/fileB.txt', 'B'*512)),  # 1 block
        ('write', ('/fileC.txt', 'C'*512)),  # 1 block
        ('read', '/fileA.txt'),               
        ('read', '/fileB.txt'),               
        ('read', '/fileC.txt')
    ]

    ## Disk inputs
    cylinders = int(input("Enter number of cylinders (e.g., 100): "))
    track_sectors = int(input("Enter number of track sectors (e.g., 1): "))
    block_size = int(input("Enter block size in bytes (e.g., 512): "))
    disk = Disk(cylinders=cylinders, track_sectors=track_sectors, block_size=block_size)
    
    ## Buffer inputs
    buffer_capacity = int(input("Enter buffer capacity (e.g., 1): "))
    buffer = Buffer(capacity=buffer_capacity)
    
    ## Disk Scheduler inputs
    scheduled_algorithm = input("Enter disk scheduling algorithm ('FCFS', 'SSTF', 'SCAN', 'C-SCAN'): ").strip().upper()
    disk_scheduler = DiskScheduler(disk, scheduled_algorithm)

    ## File system
    allocation = input("Enter allocation strategy ('contiguous' or 'linked'): ").strip().lower()
    fs = fileSystem(disk, allocation, disk_scheduler, buffer)
    
    operations = []
    ## Interactive operation input
    ## Check if user wants interactive mode or test mode
    if not test:
        use_interactive = input("Enter operations(1) or use a test set(2): ").strip() == '1'
        
        if use_interactive:
            while True:
                command = input("Enter command (read, write, delete, exit): ").strip().lower()
                if command == 'exit':
                    break
                elif command == 'write':
                    path = input(f"Enter Path: ")
                    content = input("Enter content to write: ")
                    operations.append((command, (path, content)))
                elif command == 'read':
                    path = input(f"Enter Path: ")
                    operations.append((command, path))
                elif command == 'delete':
                    path = input(f"Enter Path: ")
                    operations.append((command, path))
                else:
                    print("Unknown command. Please try again.")
        else:
            operations = testops
    else:
        operations = testops # for testing purposes
    
    try:
        fs.actions(operations) # Execute operations
    except Exception as e:
        print(f"{e}")
    
    ## Print Disk Scheduler Stats
    print("\nDisk Scheduler Stats:")
    for key, val in disk_scheduler.stats.summary().items():
        print(f"--| {key}: {val}")
    
    ## Print Disk Scheduler Stats
    print("\nBuffer Stats:")
    for key, val in buffer.summary().items():
        print(f"--| {key}: {val}")

if __name__ == "__main__":
    main()