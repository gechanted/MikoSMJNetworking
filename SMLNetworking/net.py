import netmiko as nm
import sys



class netHelper:
    global SSHConnection
    # import tkinter as tk
    # from tkinter import ttk
    # from PIL import ImageTk, Image
    # relevant netmiko stuff
    #print("Establishing connection...")

    #SSHConnection.find_prompt()
    #print("Connected!\r\n")

    currentOutput = None
    customCommandString = None


    def connecting(ip, device_type, username, password):
        print("Connecting...")


        print(SSHConnection.session_log)
        print(SSHConnection.is_alive())
        SSHConnection.find_prompt(10)
        if(SSHConnection.is_alive()):
            print("Connected!\r\n")
            return True
        else:
            return False


    def show_ip_state(self):
        current_output = self.SSHConnection.send_command('show ip int brief')
        print(current_output)


    def custom_command(customCommandString):
        current_output = SSHConnection.send_command(customCommandString)
        return current_output


    def create_vlan(self):
        while True:
            try:
                vlan_number = int(input("VLAN Number: "))
                break
            except:
                print("False Input!")

        while True:
            try:
                fast_ethernet_number = int(input("FastEthernet Portnumber (only one between 30 - 40): "))
                if (fast_ethernet_number > 40 or fast_ethernet_number < 30):
                    print("False Input!")
                else:
                    break
            except:
                print("False Input!")
        custom_command_string = ['vlan ' + str(vlan_number), 'name NetmikoVLAN' + str(vlan_number), 'exit',
                               'interface FastEthernet0/' + str(fast_ethernet_number), 'switchport mode access',
                               'switchport access vlan ' + str(vlan_number)]
        currentOutput = SSHConnection.send_config_set(custom_command_string)
        print(currentOutput)


    def delete_vlan(self):
        vlan_number = input("VLAN Number to delete: ")
        custom_command_string = "no vlan " + vlan_number
        current_output = SSHConnection.send_config_set(custom_command_string)
        print(current_output)


    def saveConfigure(self):
        customCommandString = ['exit', 'copy running-config startup-config', 'startup-config']
        currentOutput = SSHConnection.send_config_set(customCommandString)
        print(currentOutput)


    def editVLAN(self):
        while True:
            print(
                "\r\nChoose an action:\r\n   1. Show VLANs\r\n   2. Create VLAN / Add port to existing VLAN\r\n   3. Delete existing VLAN\r\n   4. Go back")
            inputText = input("Input: ")
            if inputText == "1":
                customCommandString = "show vlan brief"
                custom_command()
            elif inputText == "2":
                create_vlan()
            elif inputText == "3":
                delete_vlan()
            elif inputText == "4":
                break
            else:
                print("False input!")


    #while True:

    #    connecting(ip="192.168.101.2", device_type="cisco_ios", username="cisco", password="cisco")

    #    print(
    #        "\r\nChoose an action:\r\n   1. Show status for switchports\r\n   2. Create/Delete/Edit VLAN\r\n   3. Write custom commands to switch\r\n   4. Save config\r\n   5. Exit application")
    #    inputText = input("Input: ")
    #    if inputText == 1:
     #       show_ip_state()
     #   elif inputText == "2":
     #       customCommandString = "show vlan brief"
     #       custom_command()
      #      editVLAN()
      #  elif inputText == "3":
      #      customCommandString = input("Enter your command: ")
      #      custom_command()
      #  elif inputText == "4":
     #       saveConfigure()
     #   elif inputText == "5":
     #       break
     #   else:
     #       print("False input!")
    #sys.exit("Closing app...")

    # def VlanTest(win):
    #    currentOutput = SSHConnection.send_command('show vlan brief')
    #    print(currentOutput)


    # refreshState()