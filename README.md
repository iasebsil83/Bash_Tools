# **Bash Tools**

***Adding new tools in your bash terminal.***

&nbsp;

&nbsp;



## I] Requirements

Here is what you need to use Bash tools :

    - A Linux based operating system. (preferably Debian based)

    - Some tools are using additional packages which are
      already installed on most of debian-based systems
      so you will probably not have to install them.
      (apt, python3, tput, ...)

    - In all cases, for each tool, the required packages
      are specified.

That should be all for the requirements.

&nbsp;

&nbsp;



## II] Installation

To install :
```bash
#get the repository from GitHub
git clone https://github.com/iasebsil83/Bash_Tools

#get inside
cd Bash_Tools

#run installer
./install
```

To uninstall bash tools, remove "Bash tools" section in file ~/.bashrc and then :
```bash
rm -rf ~/.bash_tools
```

There you go !

&nbsp;

&nbsp;



## III] Use

Now, open a new terminal.
You should be able to run these new commands :

|  *command*  |*package dependencies*|        *bash_tools dependencies*      | *state* |
|:------------|---------------------:|--------------------------------------:|:-------:|
| bashtools   |                  git |                             fulls keep| working |
| bin2text    |              python3 |                                       | working |
| cutline     |                      |                                  isnbr| working |
| find_dev    |                      |                                       | working |
| fulls       |                      |                                isempty| working |
| human       |                      |                                       |  in dev |
| isempty     |                      |                                       | working |
| isnbr       |                      |                                       | working |
| keep        |                      |                                isempty| working |
| loclog      |                      |                                       | working |
| makegen     |         python3 make |                                       | working |
| multitask   |                      |                                       |  in dev |
| pop         |                      |                                       | working |
| randsuite   |                      |                                       | working |
| repeat      |                      |                                       | working |
| replaceall  |                      |                                       | working |
| splitstr    |                      |                                       | working |
| sz          |                      |                    fulls keep travelfs| working |
| text2bin    |              python3 |                                       | working |
| tput_colors |                 tput |                                  fulls| working |
| travelfs    |                      |              fulls replaceall splitstr| working |
| update_all  |                  apt |                                       | working |

To get any help on a command, use its help action as follow :
```bash
<command> --help
```

That's it for the available tools, I hope you will enjoy using them !

&nbsp;

&nbsp;



*Contact     : i.a.sebsil83@gmail.com*<br>
*Youtube     : https://www.youtube.com/user/IAsebsil83*<br>
*GitHub repo : https://github.com/iasebsil83*<br>

Let's Code ! &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;By I.A.
