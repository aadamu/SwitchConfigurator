from netmiko import ConnectHandler

device_type = "cisco_ios"


def show_version(current_operator, current_device):

    command = "show version"
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=current_device.ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()

    output = net_connect.send_command(command)
    print output


def show_ip_int_br(current_operator, current_device):

    command = "show ip interface brief"
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=current_device.ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()

    output = net_connect.send_command(command)
    print output


def show_int_status(current_operator, current_device):

    command = "show interface status"
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=current_device.ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()

    output = net_connect.send_command(command)
    print output


def set_interface_description(current_operator, current_device, device_interface):

    command_set = [
        "interface " + device_interface,
        "description Aiport Express WAN"
    ]
    net_connect = ConnectHandler(
            device_type=device_type,
            ip=current_device.ip,
            username=current_operator.username,
            password=current_operator.password
    )

    net_connect.find_prompt()

    output = net_connect.send_config_set(command_set)
    print output

