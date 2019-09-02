import netmiko

connection = netmiko.ConnectHandler(ip="", device_type="cisco_ios", username="", password="cisco")
print(connection.send_command("show run"))
