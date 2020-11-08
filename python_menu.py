import os
import time

while True:
    os.system("tput setaf 2")
    print("\t\tWelcome to Team 17.24 Menu Driven program.")
    print("\t\t------------------------------------------")
    print("")
    print("")
    os.system("tput setaf 3")
    print("Which Service do you want to automate: ")
    print("")
    print("")
    os.system("tput setaf 7")

    print("""
    01. Linux
    02. Hadoop
    03. AWS
    04. Docker
    00. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("""
        01. Create a directory
        02. List files in current directory
        03. Create an empty file
        04. Create a file and open for editing
        05. Add a new user
        06. Set/change password
        07. Show current RAM usage
        08. Show the disk usage
        09. Check if command is present
        10. Removes a command
        11. Lists the network configuration
        12. Checks the java running services
        13. List the CPU info
        14. Show currenty running processes
        15. Show running time of device
        16. Clear the cache
        17. Check which package provide the command
        18. Checks the connectivity to IP
        19. Create a user for running a specific command
        00. Go to previous menu
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
            os.system("ifconfig")
            print("")
            print("")
        elif choice == "12":
            os.system("jps")
            print("")
            print("")
        elif choice == "13":
            os.system("lscpu")
            print("")
            print("")
        elif choice == "14":
            os.system("ps -aux")
            print("")
            print("")
        elif choice == "15":
            os.system("uptime")
            print("")
            print("")
        elif choice == "16":
            os.system("echo 3 > /proc/sys/vm/drop_caches")
            print("")
            print("")
        elif choice == "17":
            name = input("Enter the command to search: ")
            str = "yum whatprovides " + name
            os.system(str)
            print("")
            print("")
        elif choice == "18":
            name = input("Enter the IP to check connectivity to: ")
            str = "ping -c 5 " + name
            os.system(str)
            print("")
            print("")
        elif choice == "19":
            name = input("Enter the commad: ")
            str = "useradd -s " + name
            name = input("Enter the username: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "2":
        print("""
        01. Checks the hadoop version
        02. Format a hadoop namenode
        03. Start the namenode service
        04. Start the datanode service
        05. Show the hadoop report
        06. List all files present in hadoop filesystem
        07. Upload the file to hadoop filesystem
        08. Remove the file from hadoop filesystem
        09. List the contents of a file in hdfs
        10. Upload the file with a defined block size
        11. Create an empty file in hadoop filesystem
        00. Go to previous menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("hadoop version")
            print("")
            print("")
        elif choice == "2":
            os.system("hadoop namenode -format")
            print("")
            print("")
        elif choice == "3":
            os.system("hadoop-daemon.sh start namenode")
            print("")
            print("")
        elif choice == "4":
            os.system("hadoop-daemon.sh start datanode")
            print("")
            print("")
        elif choice == "5":
            os.system("hadoop dfsadmin -report")
            print("")
            print("")
        elif choice == "6":
            os.system("hadoop fs -ls /")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter path of file: ")
            str = "hadoop fs -put " + name
            name = input("Enter the destignation in hadoop: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "8":
            name = input("Enter file to delete from hdfs: ")
            str = "hadoop fs -rm " + name
            os.system(str)
            print("")
            print("")
        elif choice == "9":
            name = input("Enter file whose content to view: ")
            str = "hadoop fs -cat " + name
            os.system(str)
            print("")
            print("")
        elif choice == "10":
            name = input("Enter the block size (in bytes): ")
            str = "hadoop fs -Ddfs.block.size=" + name
            name = input("Enter path of file: ")
            str = str + " -put " + name + " "
            name = input("Enter the destignation in hadoop: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "11":
            name = input("Enter name of file to create in hdfs: ")
            str = "hadoop fs -touchz / " + name
            os.system(str)
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "3":
        print("""
        01. Configure AWS
        02. Create a Key-Pair
        03. Create a Security Group
        04. Launching an instance
        05. Creating EBS
        06. Attaching EBS
        07. Creating S3 Bucket
        08. Storing file in S3 Bucket
        00. Go to previous menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("aws configure")
            print("")
            print("")
        elif choice == "2":
            name = input("Enter the key name: ")
            os.system("aws ec2 create-key-pair --key-name {name}")
            print("")
            print("")
        elif choice == "3":
            group_name = input("Enter the group name: ")
            description = input("Enter the description of security group: ")
            os.system('aws ec2 create-security-group --group-name {group_name} --description "{description}"')
            print("")
            print("")
        elif choice == "4":
            ami = input("Enter the Amazon Machine Image ID: ")
            instance_type = input("Enter the instance type: ")
            count = input("Enter the number of instances you want to launch: ")
            subnet_id = input("Enter the subnet id where you want to launch: ")
            key_name = input("Enter the key pair value you want to use: ")
            security_group = input("Enter the security group name that you use: ")
            os.system("aws ec2 run-instances --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} --security-group-ids {security_group}")
            print("")
            print("")
        elif choice == "5":
            zone = input("Enter availability zone: ")
            size = input("Enter the size: ")
            os.system("aws ec2 create-volume --availability-zone {zone} --no-encrypted --size {size}")
            print("")
            print("")
        elif choice == "6":
            instance_id = input("Enter the Instance-ID: ")
            vol_id = input("Enter the Volume-ID: ")
            os.system("aws ec2 attach-volume --instance-id {instance_id} --volume-id {vol_id} --device xvdh")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter the name you want to give to bucket: ")
            region = input("Enter the region: ")
            os.system = input("aws s3api create-bucket --bucket {name} --region {region} --create-bucket-configuration LocationConstraint={region}")
            print("")
            print("")
        elif choice == "8":
            bucket = input("Enter the name of the bucket: ")
            file_object = input("Enter the path of the object with name: ")
            name_dir = input("Enter the name which you want to give to the object when i will save in the bucket: ")
            os.system = input("aws s3api put-object --bucket {bucket} --key {name_dir} --body \"{file_object}\"")
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "4":
        print("""
        01. Checks the docker version
        02. Creating a container
        03. Pull image from dockerhub
        04. List running docker containers
        05. List all docker containers
        06. List all images present in system
        07. Starting a docker container
        08. Stopping a docker container
        09. Deleting a docker container
        10. Stop all docker containers
        11. Delete all docker containers
        00. Go to previous menu
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("docker version")
            print("")
            print("")
        elif choice == "2":
            name = input("Enter name of image: ")
            str = "docker run -it " + name
            name = input("Enter the version of image: ")
            str = str + ":" + name
            os.system(str)
            print("")
            print("")
        elif choice == "3":
            name = input("Enter name of image: ")
            str = "docker pull " + name
            name = input("Enter the version of image: ")
            str = str + ":" + name
            os.system(str)
            print("")
            print("")
        elif choice == "4":
            os.system("docker ps")
            print("")
            print("")
        elif choice == "5":
            os.system("docker ps -a")
            print("")
            print("")
        elif choice == "6":
            os.system("docker images")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter container name: ")
            str = "docker container start " + name
            os.system(str)
            print("")
            print("")
        elif choice == "8":
            name = input("Enter container name: ")
            str = "docker container stop " + name
            os.system(str)
            print("")
            print("")
        elif choice == "9":
            name = input("Enter container name: ")
            str = "docker container rm " + name
            os.system(str)
            print("")
            print("")
        elif choice == "10":
            os.system("docker container rm $(docker container ls –aq)")
            print("")
            print("")
        elif choice == "11":
            os.system("docker container stop $(docker container ls –aq) && docker system prune –af ––volumes")
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
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