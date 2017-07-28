"""

"""

import os
import codecs
from .State import FileState


def dump_dir(directory, found_files, found_users, found_groups):
    subdirs = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        st = FileState(path)
        found_users.add(st.Uid)
        found_groups.add(st.Gid)
        (subdirs if st.IsDirectory else found_files).append(st)

    for subdir in subdirs:
        found_files.append(subdir)
        dump_dir(subdir.Path, found_files, found_users, found_groups)


def prepare_known_users():
    known_user_names = {}
    known_user_ids = {}
    with codecs.open('/etc/passwd', 'r', 'utf-8') as file:
        for line in file:
            name = line.split(':')[0]
            uid = int(line.split(':')[2])
            known_user_names[name] = uid
            known_user_ids.setdefault(uid, set()).add(name)
    # print(known_user_names)
    # print(known_user_ids)
    return known_user_names, known_user_ids


def prepare_known_groups():
    known_group_names = {}
    known_group_ids = {}
    with codecs.open('/etc/group', 'r', 'utf-8') as file:
        for line in file:
            name = line.split(':')[0]
            gid = int(line.split(':')[2])
            known_group_names[name] = gid
            known_group_ids.setdefault(gid, set()).add(name)
    # print(known_group_names)
    # print(known_group_ids)
    return known_group_names, known_group_ids


def dump(directory,
         output_file,
         script_type,
         conflict_user_restore,
         conflict_group_restore):

    found_files = []
    found_users = set()
    found_groups = set()

    directory = os.path.realpath(directory)
    dump_dir(directory, found_files, found_users, found_groups)

    known_user_names, known_user_ids = prepare_known_users()
    known_group_names, known_group_ids = prepare_known_groups()

    dict_users = dict(map(lambda uid: (uid, list(known_user_ids[uid])), found_users))
    dict_groups = dict(map(lambda gid: (gid, list(known_group_ids[gid])), found_groups))

    for st in found_files:
        print("%04o | %5d | %5d | %s" % (st.Permission, st.Uid, st.Gid, st.Path))
    print(dict_users)
    print(dict_groups)
