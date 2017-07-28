"""

"""


__description__ = 'A Python package helping to dump and restore ' \
                  'files\' "state"(user, group, permissions) in a directory'


OUTPUT_FILE_DEFAULT = 'restore-state'


OUTPUT_SCRIPT_FORMAT_SHELL = "shell"
OUTPUT_SCRIPT_FORMAT_PYTHON = "python"
OUTPUT_SCRIPT_FORMAT_CSHARP = "csharp"
OUTPUT_SCRIPT_FORMATS = [
    OUTPUT_SCRIPT_FORMAT_SHELL,
    OUTPUT_SCRIPT_FORMAT_PYTHON,
    OUTPUT_SCRIPT_FORMAT_CSHARP
]


CONFLICT_PREFER_ERROR = 'error'
CONFLICT_PREFER_NAME = 'name'
CONFLICT_PREFER_ID = 'id'
CONFLICT_PREFERS = [
    CONFLICT_PREFER_ERROR,
    CONFLICT_PREFER_NAME,
    CONFLICT_PREFER_ID
]
