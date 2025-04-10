import socket

HOST = "127.0.0.1"
PORT = 65432

employees = {
    "E00123": {"Name": "Aadya Khan", "Salary": 38566, "2018": {"Year": 2018,"Pay": 32000,"ot": 3566, "Leave": 25}, "2016": {"Year": 2016, "Pay": 30000,"ot": 2000, "Leave": 22}, "C_Leave": 25},
    "E01033": {"Name": "John Smith", "Salary": 35000, "2018": {"Year": 2018,"Pay": 29400, "ot": 2587, "Leave": 25}, "2016": {"Year": 2016, "Pay": 27000, "ot": 1500, "Leave": 22}, "C_Leave": 25}
}

def handle(data):
    try:
        command,emp,command2,command3 = data.split()
        if emp not in employees:
            return f"Error: Employee ID {emp} not found."

        if emp in employees:
            if command == "S":
                if command2 == "C":
                    return f"Employee: {employees[emp]['Name']} Current Salary: {employees[emp]['Salary']}"
                elif command2 == "T":
                    if command3 == "2018":
                        return f"Employee: {employees[emp]['Name']} Total Salary for {employees[emp]['2018']['Year']}: Pay: {employees[emp]['2018']['Pay']} Overtime: {employees[emp]['2018']['ot']}"
                    elif command3 == "2016":
                        return f"Employee: {employees[emp]['Name']} Total Salary for {employees[emp]['2016']['Year']}: Pay: {employees[emp]['2016']['Pay']} Overtime: {employees[emp]['2016']['ot']}"
                    
                
            elif command == "L":
                if command2 == "C":
                    return f"Employee: {employees[emp]['Name']} Current annual leave: {employees[emp]['C_Leave']} Days"
                elif command2 == "Y":
                    if command3 == "2018":
                        return f"Employee: {employees[emp]['Name']} Total Leave for {employees[emp]['2018']['Year']}: {employees[emp]['2018']['Leave']} Days"
                    elif command3 == "2016":
                        return f"Employee: {employees[emp]['Name']} Total Leave for {employees[emp]['2016']['Year']}: {employees[emp]['2016']['Leave']} Days"
            
            else:
                return "Error: Invalid command. Use 'S' or 'L'."
            
    except Exception as e:
        return f"Error: {str(e)}"

                
            
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        print("Server is listening on", (HOST, PORT))
        conn,addr = s.accept()
        with conn:
            print(f"connected by {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                response = handle(data)
                conn.sendall(response.encode())     

if __name__ == "__main__":
    main()