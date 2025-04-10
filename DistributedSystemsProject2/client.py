import socket

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        print("HR System 1.0")
        print("---------------")
        while True:
            command = input("Enter command (S for salary, L for leave, or X to exit): ").strip().upper()
            if command == "X":
                print("Exiting")
                break
        
            emp_id = input("Enter Employee ID: ").strip()
            if command == "S":
                command2 = input("Enter C for Current salary or T for Total salary for a year: ").strip().upper()
                command3 = "Done!"
                if command2 == "T":
                    command3 = input("Enter Year (Data for 2016 and 2018 are on record only): ").strip()
                    
            elif command == "L":
                command2 = input("Enter C for Current leave entitlement or Y for Leave taken for a year: ").strip().upper()
                if command2 == "Y":
                    command3 = input("Enter Year (Data for 2016 and 2018 are on record only): ").strip()
            else:
                print("Invalid command. Please try again.")
                continue
            
            full_command = f"{command} {emp_id} {command2} {command3}"
        
            s.sendall(full_command.encode())
            data = s.recv(1024).decode()
            print(data)
        
if __name__ == "__main__":
    main()