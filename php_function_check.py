import sys
import argparse

# List of potentially dangerous PHP functions
dangerous_functions = [
    'exec', 'system', 'shell_exec', 'passthru', '`backticks`', 'popen', 'proc_open',
    'pcntl_exec', 'file_get_contents', 'fopen', 'include', 'include_once', 'require',
    'require_once', 'fsockopen', 'pfsockopen', 'stream_socket_client', 'eval',
    'create_function', 'preg_replace', 'assert', 'unserialize', 'extract'
]

def get_disabled_functions(disabled_functions_string):
    """
    Function to get the list of disabled PHP functions from a string.
    """
    # Split the string into a list of functions
    disabled_functions = disabled_functions_string.split(',')
    return disabled_functions

def check_enabled_functions(dangerous_functions, disabled_functions):
    """
    Function to check which dangerous functions are still enabled.
    """
    # Find the functions that are still enabled
    enabled_functions = [func for func in dangerous_functions if func not in disabled_functions]
    return enabled_functions

def main(disabled_functions_string):
    # Get the list of disabled functions
    disabled_functions = get_disabled_functions(disabled_functions_string)
    
    # Check which dangerous functions are still enabled
    enabled_functions = check_enabled_functions(dangerous_functions, disabled_functions)
    
    if enabled_functions:
        print("The following potentially dangerous PHP functions are still enabled:")
        for func in enabled_functions:
            print(f"- {func}")
        print("\nCheck the following link on how to abuse them: https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass")

    else:
        print("All potentially dangerous PHP functions are disabled.")

    print(r"""
  ____ ___    _    ____  _     ___  
 |  _ \_ _|  / \  | __ )| |   / _ \ 
 | | | | |  / _ \ |  _ \| |  | | | |
 | |_| | | / ___ \| |_) | |__| |_| |
 |____/___/_/   \_\____/|_____\___/ 
                                    
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check which potentially dangerous PHP functions are still enabled.",epilog="Example: python php_function_check.py \"exec,system,shell_exec,passthru\"")
    parser.add_argument('disabled_functions_string', type=str, nargs='?', help="Comma-separated string of disabled PHP functions")

    args = parser.parse_args()

    if args.disabled_functions_string is None:
        parser.print_help()
        sys.exit(1)
    
    main(args.disabled_functions_string)
