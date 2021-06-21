                        Bash Tools

    This repository is a bunch of little tools that can
help you in a bash terminal.






I] Requirements

Here is what you need to use Bash tools :

    - Linux OS

    - Some tools are using additional packages which are
      already installed on most of debian-based systems
      so you will probably not have to install them.
      (apt, python3, tput, ...)

    - In all cases, for each tool, the required packages
      are specified.

That should be all for the requirements.






II] Installation

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






III] Use

Now, open a new terminal.
You should be able to run these new commands :

    - update_all       (completely update & upgrade your packages and remove
                        unnecessary files.)

    - dev_finder       (detect the effects of a new device on your computer in /dev)
                        [Requires python3]

    - tput_allColors   (shows the available colors in your terminal.)
                        [Requires tput]

    - mtx_bin          (displays binary numbers randomly in the terminal.)

    - mtx_hex          (same as mtx_bin but in hexadecimal.)

    - update_bashTools (update all the previous tools including this one.)
                        [Requires git]

That's it for the available tools.






IV] Problems

If you don't find these commands in your new terminal, maybe your system don't
recognize them as executables. You can solve this by doing :

    > chmod 777 ~/.bash_tools/* && chmod 666 ~/.bash_tools/README.txt 

Hope you will enjoy using these tools !



Contact     : i.a.sebsil83@gmail.com
Youtube     : https://www.youtube.com/user/IAsebsil83
GitHub repo : https://github.com/iasebsil83

Let's Code !                                  By I.A.

