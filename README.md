###Bash Tools

    This repository contains a bunch of little tools that
can help you in a bash terminal or just make the use of
your bash terminal easier.




##I] Requirements

Here is what you need to use Bash tools :

    - Linux OS

    - Some tools are using additional packages which are
      already installed on most of debian-based systems
      so you will probably not have to install them.
      (apt, python3, tput, ...)

    - In all cases, for each tool, the required packages
      are specified.

That should be all for the requirements.




##II] Installation

Get the repository from GitHub :
    > git clone https://github.com/iasebsil83/Bash_Tools

Launch the installer :
    > ./Bash_Tools/install

Installator did not launch ?
Maybe the file is not executable :
    > sudo chmod 777 Bash_tools/install

To uninstall bash tools :
    > remove "Bash tools" section in file ~/.bashrc
    > rm -rf ~/.bash_tools

There you go !




##III] Use

Now, open a new terminal.
You should be able to run these new commands :

    - dev_finder       [Requires python3]
    - filter
    - loclog
    - mtx_bin
    - mtx_hex
    - multitask                        (comming soon...)
    - projia           [Requires grep] (in development...)
    - tput_allColors   [Requires tput]
    - update_all
    - update_bashTools [Requires git]

    Bash Tools also includes some pretty cool aliases (not active by default).
You should probably go check it out at :
        ~/.bash_tools/aliases

To get any help on a command, use its help option as follow :
    > <command> --help

That's it for the available tools.




##IV] Problems

If you don't find these commands in your new terminal, maybe your system don't
recognize them as executables. You can solve this by doing :

    > chmod 777 ~/.bash_tools/* && chmod 666 ~/.bash_tools/README.txt ~/.bash_tools/aliases

Hope you will enjoy using these tools !




*Contact     : i.a.sebsil83@gmail.com*
*Youtube     : https://www.youtube.com/user/IAsebsil83*
*GitHub repo : https://github.com/iasebsil83*

Let's Code !                                  By I.A.
