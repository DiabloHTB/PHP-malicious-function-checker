# PHP Dangerous Functions Checker

This script checks which potentially dangerous PHP functions are still enabled in PHP configuration based on a given list of disabled functions. It helps you identify PHP functions that could be exploited.


## Usage







Use `phpinfo()` to get a list of disabled fucntions under `disable_functions` from the target and clone this repository to your local machine and run the scrtipt:

```bash
git clone https://github.com/DiabloHTB/php-dangerous-functions-checker.git
cd php-dangerous-functions-checker
python3 php_function_check.py "list,of,disabled,fucntions" #Copy the list directly from the phpinfo page
```
## Example

```bash
┌──(diablo㉿diablo)-[~]
└─$ python3 php_function_check.py "exec,system,passthru,proc_open,pcntl_exec,file_get_contents,fopen,include,include_once,require,require_once,fsockopen,pfsockopen,stream_socket_client,eval,create_function,preg_replace,assert,unserialize"
The following potentially dangerous PHP functions are still enabled:

- shell_exec
- popen
- extract

Check the following link on how to abuse them: https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass
  ____ ___    _    ____  _     ___  
 |  _ \_ _|  / \  | __ )| |   / _ \ 
 | | | | |  / _ \ |  _ \| |  | | | |
 | |_| | | / ___ \| |_) | |__| |_| |
 |____/___/_/   \_\____/|_____\___/ 

```


----
## Disclaimer
This script is for educational and security auditing purposes only. Use it at your own risk. The authors are not responsible for any misuse or damage caused by this script.

