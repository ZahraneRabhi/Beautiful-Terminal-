class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
style = {
        "TERMINAL": '\033[m',
        "PURPLE": '\033[95m',
        "GREEN": '\033[92m',
        "RED": '\033[91m',
          }

speed_dic = {
        "FAST": [0, 0.1],
        "NORMAL": [0.3, 0.4],
        "SLOW": [0.6, 1]
}