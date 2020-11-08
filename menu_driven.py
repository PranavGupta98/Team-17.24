import os
import time

while True:
    os.system("tput setaf 2")
    print("\t\tWelcome to Team 17.24 Menu Driven program.")
    print("\t\t------------------------------------------")
    print("")
    print("")
    os.system("tput setaf 7")


    print("""
    1. Create a directory
    2. List files in current directory
    3. Create an empty file
    4. Create a file and open for editing
    5. Add a new user
    6. Set/change password
    7. Show current RAM usage
    8. Show the disk usage
    9. Check if command is present
    10. Removes a command
    11. Checks the hadoop version
    12. Lists the network configuration
    13. Checks the java running services
    14. Format a hadoop namenode
    15. Start the namenode service
    16. Start the datanode service
    17. Show the hadoop report
    18. List the CPU info
    19. Show currenty running processes
    20. Show running time of device
    21. Clear the cache
    22. List all files present in hadoop filesystem
    23. Upload the file to hadoop filesystem
    24. Remove the file from hadoop filesystem
    25. List the contents of a file in hdfs
    26. Upload the file with a defined block size
    27. Create an empty file in hadoop filesystem
    28. Check which package provide the command
    29. Checks the connectivity to IP
    30. Create a user for running a specific command
    0. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter directory name: ")
        str = "mkdir " + name
        os.system(str)
        print("")
        print("")
    elif choice == "2":
        os.system("ls -alh")
        print("")
        print("")
    elif choice == "3":
        name = input("Enter file name: ")
        str = "touch " + name
        os.system(str)
        print("")
        print("")
    elif choice == "4":
        name = input("Enter file name: ")
        str = "vim " + name
        os.system(str)
        print("")
        print("")
    elif choice == "5":
        name = input("Enter username: ")
        str = "useradd " + name
        os.system(str)
        print("")
        print("")
    elif choice == "6":
        name = input("Enter username: ")
        str = "passwd " + name
        os.system(str)
        print("")
        print("")
    elif choice == "7":
        os.system("free -m")
        print("")
        print("")
    elif choice == "8":
        os.system("df -h")
        print("")
        print("")
    elif choice == "9":
        name = input("Enter command name: ")
        str = "rpm -q " + name
        os.system(str)
        print("")
        print("")
    elif choice == "10":
        name = input("Enter command name: ")
        str = "rpm -e " + name
        os.system(str)
        print("")
        print("")
    elif choice == "11":
        os.system("hadoop version")
        print("")
        print("")
    elif choice == "12":
        os.system("ifconfig")
        print("")
        print("")
    elif choice == "13":
        os.system("jps")
        print("")
        print("")
    elif choice == "14":
        os.system("hadoop namenode -format")
        print("")
        print("")
    elif choice == "15":
        os.system("hadoop-daemon.sh start namenode")
        print("")
        print("")
    elif choice == "16":
        os.system("hadoop-daemon.sh start datanode")
        print("")
        print("")
    elif choice == "17":
        os.system("hadoop dfsadmin -report")
        print("")
        print("")
    elif choice == "18":
        os.system("lscpu")
        print("")
        print("")
    elif choice == "19":
        os.system("ps -aux")
        print("")
        print("")
    elif choice == "20":
        os.system("uptime")
        print("")
        print("")
    elif choice == "21":
        os.system("echo 3 > /proc/sys/vm/drop_caches")
        print("")
        print("")
    elif choice == "22":
        os.system("hadoop fs -ls /")
        print("")
        print("")
    elif choice == "23":
        name = input("Enter path of file: ")
        str = "hadoop fs -put " + name
        name = input("Enter the destignation in hadoop: ")
        str = str + name
        os.system(str)
        print("")
        print("")
    elif choice == "24":
        name = input("Enter file to delete from hdfs: ")
        str = "hadoop fs -rm " + name
        os.system(str)
        print("")
        print("")
    elif choice == "25":
        name = input("Enter file whose content to view: ")
        str = "hadoop fs -cat " + name
        os.system(str)
        print("")
        print("")
    elif choice == "26":
        name = input("Enter the block size (in bytes): ")
        str = "hadoop fs -Ddfs.block.size=" + name
        name = input("Enter path of file: ")
        str = str + " -put " + name + " "
        name = input("Enter the destignation in hadoop: ")
        str = str + name
        os.system(str)
        print("")
        print("")
    elif choice == "27":
        name = input("Enter name of file to create in hdfs: ")
        str = "hadoop fs -touchz / " + name
        os.system(str)
        print("")
        print("")
    elif choice == "28":
        name = input("Enter the command to search: ")
        str = "yum whatprovides " + name
        os.system(str)
        print("")
        print("")
    elif choice == "29":
        name = input("Enter the IP to check connectivity to: ")
        str = "ping -c 5 " + name
        os.system(str)
        print("")
        print("")
    elif choice == "30":
        name = input("Enter the commad: ")
        str = "useradd -s " + name
        name = input("Enter the username: ")
        str = str + name
        os.system(str)
        print("")
        print("")
    elif choice == "0":
        exit()
    else:
        os.system("tput setaf 1")
        print("ERROR: Command not found")
        os.system("tput setaf 7")
        print("")
        print("")

    time.sleep(2)
