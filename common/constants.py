DEFAULT_PADDING = 4
DEFAULT_PADDING_LEFT = DEFAULT_PADDING
DEFAULT_PADDING_RIGHT = DEFAULT_PADDING
DEFAULT_ALIGN = 'left'
DEFAULT_WIDTH = 80
DEFAULT_HEIGHT = 20
DEFAULT_BORDER = '='
DEFAULT_PADDING_SPACE = 2
TOTAL_PADDING = DEFAULT_PADDING_LEFT + DEFAULT_PADDING_RIGHT + (
        DEFAULT_PADDING_SPACE * 2)
HEADER_HEIGHT = 15
FOOTER_HEIGHT = 5
MAX_COLUMN_WIDTH = 40
DEFAULT_LEVEL = 5
DEFAULT_MAX_ATTEMPTS = 6


class bcolors:
    """Colors for terminal output."""
    WHITE = '\033[97m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    BLINK = '\033[5m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    YELLOW="\033[1;33m"
    LIGHT_PURPLE="\033[1;35m"
    PURPLE="\033[0;34m"
    KINDA_PURPLE="\033[0;35m"
    FAIL = '\033[91m'
    BGFAIL = '\033[41m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
