"""

"""

from __future__ import print_function

import argparse
import os
import sys

try:
    from statedump import Meta, StateDump
except ImportError:
    sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
    from statedump import Meta, StateDump


def parse_arguments():

    class MyArgumentParser(argparse.ArgumentParser):
        def error(self, message):  # override
            print('ERROR: %s\n' % message, file = sys.stderr)
            self.print_help(file = sys.stderr)
            sys.exit(2)

    parser = MyArgumentParser(
        description = Meta.__description__,
        add_help = False)
    parser.add_argument('Directory',
                        metavar = '<directory>')
    parser.add_argument('-h', '--help',
                        dest = 'IsHelp',
                        action = 'store_true',
                        help = 'Show this help message and exit.')
    parser.add_argument('-o', '--output',
                        metavar = '<output_file>',
                        dest = 'OutputFile',
                        default = '',
                        help = 'Specify name of the generated script.\n'
                               'Default: "%s.<ext>".' % Meta.OUTPUT_FILE_DEFAULT)
    parser.add_argument('-t', '--type',
                        metavar = '<script_type>',
                        dest = 'ScriptType',
                        choices = Meta.OUTPUT_SCRIPT_FORMATS,
                        default = Meta.OUTPUT_SCRIPT_FORMAT_SHELL,
                        help = 'Specify type of generated script: %s. Default: "%s".'
                               % (Meta.OUTPUT_SCRIPT_FORMATS, Meta.OUTPUT_SCRIPT_FORMAT_SHELL))
    parser.add_argument('--conflict-user-restore',
                        metavar = '<prefer>',
                        dest = 'ConflictUserRestore',
                        choices = Meta.CONFLICT_PREFERS,
                        default = Meta.CONFLICT_PREFER_ID,
                        help = 'Specify your preference when there is a conflict on '
                               'restoring user\'s *name* and *id*: %s. Default: "%s".'
                               % (Meta.CONFLICT_PREFERS, Meta.CONFLICT_PREFER_ID))
    parser.add_argument('--conflict-group-restore',
                        metavar = '<prefer>',
                        dest = 'ConflictGroupRestore',
                        choices = Meta.CONFLICT_PREFERS,
                        default = Meta.CONFLICT_PREFER_ID,
                        help = 'Specify your preference when there is a conflict on '
                               'restoring group\'s *name* and *id*: %s. Default: "%s".'
                               % (Meta.CONFLICT_PREFERS, Meta.CONFLICT_PREFER_ID))
    return parser.parse_args()


def main():
    args = parse_arguments()
    print(args)
    StateDump.dump(args.Directory, args.OutputFile, args.ScriptType, args.ConflictUserRestore, args.ConflictGroupRestore)
    return 0


if __name__ == '__main__':
    sys.exit(int(main() or 0))
