NFS is running on port 2049/tcp. Let’s list the remote shares: 

first of all we need to install nfs-common

To mount an NFS file system on a given mount point, use the mount command in the following form:

mount [OPTION...] NFS_SERVER:EXPORTED_DIRECTORY MOUNT_POINT

Use the steps below to manually mount a remote NFS share on your Linux system:

    First, create a directory to serve as the mount point for the remote NFS share:

    sudo mkdir /var/backups

Mount point is a directory on the local machine where the NFS share is to be mounted.

Mount the NFS share by running the following command as root or user with sudo privileges:

sudo mount -t nfs 10.10.0.10:/backups /var/backups

Where 10.10.0.10 is the IP address of the NFS server, /backup is the directory that the server is exporting and /var/backups is the local mount point.

On success, no output is produced.


There is a FTP server running on default port 21/tcp, which allows anonymous connections. Listing the files, we find a file named file.txt, that we download using the get command: 


Let’s connect to the MySQL database using the credentials gathered from the file.txt file we gathered via FTP: 

mysql -h 10.10.125.220 -u root -p

> show databases;

> use database_name;

> show tables;

> select * from table_name;