### **Bash Tools**

    **This repository contains a bunch of little tools that
can help you in a bash terminal or just make the use of
your bash terminal easier.***
&nbsp;



## I] Requirements

Here is what you need to use Bash tools :

    - Linux OS

    - Some tools are using additional packages which are
      already installed on most of debian-based systems
      so you will probably not have to install them.
      (apt, python3, tput, ...)

    - In all cases, for each tool, the required packages
      are specified.

That should be all for the requirements.
$nbsp;



## II] Installation

Get the repository from GitHub :
```bash
git clone https://github.com/iasebsil83/Bash_Tools
```

Launch the installer :
```bash
./Bash_Tools/install
```

Installator did not launch ?
Maybe the file is not executable :
```bash
chmod 777 Bash_tools/install
```

To uninstall bash tools :
```bash
remove "Bash tools" section in file ~/.bashrc
rm -rf ~/.bash_tools
```

There you go !
&nbsp;



## III] Use

Now, open a new terminal.
You should be able to run these new commands :

|   command   | package dependencies | bash_tools dependencies|  state  |
|:------------|---------------------:|-----------------------:|:-------:|
| bashtools   |                  git |                   keep | working |
| current_cmd |                      |                        |     bug |
| find_dev    |                      |                        | working |
| keep        |                      |                        | working |
| last_cmd    |                      |            current_cmd |     bug |
| loclog      |                      |                        | working |
| ls_complete |                      |                        | working |
| multitask   |                      |                        |  in dev |
| pop         |                      |                        | working |
| projia      |                 grep |                   keep |  in dev |
| randsuite   |                      |                        | working |
| tput_colors |                 tput |                        | working |
| update_all  |                  apt |                        | working |

To get any help on a command, use its help option as follow :
```bash
<command> --help
```

That's it for the available tools, I hope you will enjoy using them !
&nbsp



*Contact     : i.a.sebsil83@gmail.com*
*Youtube     : https://www.youtube.com/user/IAsebsil83*
*GitHub repo : https://github.com/iasebsil83*

Let's Code !                                  By I.A.
