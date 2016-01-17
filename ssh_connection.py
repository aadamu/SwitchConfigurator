import paramiko
import time


def disable_paging(remote_conn):
    remote_conn.send("term leng 0")
    time.sleep(1)

    device_output = remote_conn.recv(1024)

    return device_output


def print_output(remote_conn):
    device_output = remote_conn.recv(65535)
    print(device_output)


def open_connection(device_ip, user_username, user_password):

    remote_conn_pre = paramiko.SSHClient()

    remote_conn_pre.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
    )
    
    remote_conn_pre.connect(
            device_ip, username=user_username, password=user_password, look_for_keys=False, allow_agent=False
    )
    
    remote_conn = remote_conn_pre.invoke_shell()
    
    disable_paging(remote_conn)
    
    remote_conn.send("\n")
    time.sleep(2)
    
    print_output(remote_conn)

    return remote_conn.get_id()


def run_command(command, device_ip, user_username, user_password):

    remote_conn_pre = paramiko.SSHClient()

    remote_conn_pre.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
    )

    remote_conn_pre.connect(
            device_ip, username=user_username, password=user_password, look_for_keys=False, allow_agent=False
    )

    remote_conn = remote_conn_pre.invoke_shell()

    disable_paging(remote_conn)

    remote_conn.send("\n")
    remote_conn.send(command)
    remote_conn.send("\n")
    remote_conn.send("exit \n")

    time.sleep(2)

    print_output(remote_conn)

    return remote_conn.get_id()









