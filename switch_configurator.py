import ios_commands
import socket


class NetOperator:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class NetDevice:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip = ""
        self.vendor = ""
        self.model = ""
        self.version = ""


current_operator = NetOperator(raw_input("Username: "), raw_input("Password: "))
current_device = NetDevice(raw_input("Hostname: "))
current_device.ip = socket.gethostbyname(current_device.hostname)

# ssh_connection.open_connection(
#     device_ip=current_device.ip, user_username=current_operator.username, user_password=current_operator.password
# )

ios_commands.set_interface_description(current_operator, current_device, "Fa0")













