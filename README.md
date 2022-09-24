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
| bashtools   |                  git |                            fulls keep |    ok   |
| bin2text    |              python3 |                                       |    ok   |
| cutline     |                      |                                 isnbr |    ok   |
| findev      |                      |                                       |    ok   |
| fulls       |                      |                               isempty |    ok   |
| isempty     |                      |                                       |    ok   |
| isnbr       |                      |                                       |    ok   |
| keep        |                      |                               isempty |    ok   |
| loclog      |                      |                                       |    ok   |
| makegen     |         python3 make |                                       |    ok   |
| pop         |                      |                                       |    ok   |
| randsuite   |                      |                                 isnbr |    ok   |
| repeat      |                      |                                       |    ok   |
| replaceall  |                      |                                       |    ok   |
| splitstr    |                      |                                       |    ok   |
| text2bin    |              python3 |                                       |    ok   |
| tputcolors  |                 tput |                                 fulls |    ok   |
| travelfs    |                      |             fulls replaceall splitstr |    ok   |
| updateall   |                  apt |                                       |    ok   |

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
