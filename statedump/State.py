
import os
import pwd
import grp


if os.name != "posix":
    raise OSError('"stat" is supported in "posix" systems only, but current is "%s"' % os.name)


S_IFMT   = 0o0170000   # bitmask for the file type bitfields
S_IFSOCK = 0o0140000   # socket
S_IFLNK  = 0o0120000   # symbolic link
S_IFREG  = 0o0100000   # regular file
S_IFBLK  = 0o0060000   # block device
S_IFDIR  = 0o0040000   # directory
S_IFCHR  = 0o0020000   # character device
S_IFIFO  = 0o0010000   # fifo
S_ISUID  = 0o0004000   # set UID bit
S_ISGID  = 0o0002000   # set GID bit (see below)
S_ISVTX  = 0o0001000   # sticky bit (see below)
S_IRWXU  = 0o00700     # mask for file owner permissions
S_IRUSR  = 0o00400     # owner has read permission
S_IWUSR  = 0o00200     # owner has write permission
S_IXUSR  = 0o00100     # owner has execute permission
S_IRWXG  = 0o00070     # mask for group permissions
S_IRGRP  = 0o00040     # group has read permission
S_IWGRP  = 0o00020     # group has write permission
S_IXGRP  = 0o00010     # group has execute permission
S_IRWXO  = 0o00007     # mask for permissions for others (not in group)
S_IROTH  = 0o00004     # others have read permission
S_IWOTH  = 0o00002     # others have write permisson
S_IXOTH  = 0o00001     # others have execute permission


class FileState:
    def __init__(self, path):
        stat = os.lstat(path)
        self.Path = path
        self.Uid = stat.st_uid
        self.Gid = stat.st_gid
        self.Permission = stat.st_mode & 0o7777
        self.IsDirectory = ((stat.st_mode & S_IFMT) == S_IFDIR)
        self.IsLink = ((stat.st_mode & S_IFMT) == S_IFLNK)
