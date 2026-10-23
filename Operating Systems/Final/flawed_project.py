#Flawed Code: Combined OS Assignment
# This program attempts to simulate all parts of the assignment
# across Windows, macOS, and Linux.

import subprocess
import time
import platform
import threading
from flask import Flask, request 

# --- Part 4: Cloud/IoT Web App ---
app = Flask(__name__)
iot_device_database = {"dev_01": {"type": "thermostat", "temp": 72}}

@app.route('/api/device/<id>')
def get_device(id):
    """Returns data for a specific device."""
    if id in iot_device_database:
       
        return jsonify(iot_device_database[id])
    else:
       
        return {"error": "Device not found"}, 404

@app.route('/api/register', methods=['POST', 'GET'])
def register_device():
    """Registers a new device from posted data."""
  
    data = request.args
    
    new_id = data['id'] # Mistake 5
    new_type = data['type']
    
    iot_device_database[new_id] = {"type": new_type, "status": "online"}
    print(f"Registered new device: {new_id}")
    return {"status": "created", "id": new_id}, 201

def start_web_server():
    """Starts the Flask server in a separate thread."""
    print("Attempting to start cloud server on port 80...")
    
    server_thread = threading.Thread(target=app.run(host='127.0.0.1', port=80))
    server_thread.start()
    print("Server thread started.")

# --- Part 1: Embedded System Simulator ---
led_state = "OFF" # Global state for the LED

def run_embedded_sim():
    """Simulates the Arduino button and LED logic."""
    print("\n--- Embedded Simulator (Part 1) ---")
    print("Press 'b' to simulate button press. 'q' to quit.")
    
    while True:
        press = input("Input (b/q): ")
        
       
        if press != 'b':
            # Simulating button NOT pressed (PULLUP = HIGH)
            pass
        else:
            # Simulating button IS pressed (LOW)
            print(f"Button pressed. LED is {led_state}")
            led_state = "ON" # Mistake 8
            print(f"LED is {led_state}")
            time.sleep(0.5) # Corresponds to delay(500)
            led_state = "OFF"
          
            
        if press == 'q':
            print("Exiting simulator.")
            break

# --- Part 3: Operating System Security ---
def run_security_audit():
    """Attempts to apply a cross-platform firewall rule."""
    print("\n--- Security Audit (Part 3) ---")
    system_os = platform.system()
    port_to_block = "22" # From assignment
    command = ""
    
    if system_os == "Linux":
        print("Detected Linux. Using iptables.")
   
        command = f"iptables -A INPUT -p tcp --dport {port_to_block} -j DROP"
    elif system_os == "Windows":
        print("Detected Windows. Using netsh.")

        command = f"netsh advfirewall firewall add rule name=BlockSSH dir=in action=block protocol=TCP"
    elif system_os == "Darwin":
        print("Detected macOS. Using pfctl.")
        # This command is syntactically wrong
        command = f"block in proto tcp from any to any port {port_to_block}"
    else:
        print(f"Unsupported OS: {system_os}")
        return

    try:
        print(f"Running: {command}")

        subprocess.run(command, check=True)
        print("Firewall rule successfully applied.")
    except:

        print("!!! FAILED to apply firewall rule. Check syntax and permissions. !!!")


# --- Main Application Menu ---
def main():
    while True:
        print("\n--- Modern OS Final Project ---")
        print(" 1. Run Embedded System Simulator (Part 1)")
        print(" 2. Run Security Audit (Part 3)")
        print(" 3. Launch Cloud Web Server (Part 4)")
        print(" 4. Exit")
        choice = input("Enter your choice: ")
        

        if choice == 1:
            run_embedded_sim()
        elif choice == 2:
            run_security_audit()
        elif choice == 3:
            start_web_server()
        elif choice == 4:
            print("Exiting.")
            break

if __name__ == "__main__":
    main()