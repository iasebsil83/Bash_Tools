x----------------------------------------------------------------------x
|                             Projia [0.1.0]                           |
|                                                                      |
|               Project generator using I.A.'s libraries.              |
x----------------------------------------------------------------------x




Welcome to projia !

Your new project generator that will save you time !
- First let's see what projia is able to do for now.
- Secondly we will see how you can CUSTOMIZE your own project generator.




I] Overview

    In some languages like C, C++, java... it can be a bit redundant to
create all the necessary files & folders for each project. Moreover, the
integration of some libraries and their dependencies can make the thing
harder and longer.

    Projia has been made in order to give a simple and fast way to
create a project in these languages with all the stuff you might need
around (src folder, README, makefile...).

    Let's keep it simple and say that projia has project templates that
will be used to create yours.

Example :
    Want to create a Swift project that can use a kind of network ?

     > projia --swift mySwiftProject network

    And there you go !

Possible questions :

- But what kind of templates are used ?
- And Why using only I.A.'s libraries ? Can I use mine ?
- Is that possible to create my own implementation of a language ?
  Or multiple implementations of the same language ?

Answers to these questions are below.




II] Templates

Project templates are sorted by language and stored here :
        ~/.bash_tools/.projia/#language#/default/

    All the files & folders existing in these "default" folders will be
copied at each new project creation.

    So you can customize your project generation as you want by modifying
the folders & files inside the "default" directory. Mind that you can also
define some custom variables that you can use in your template files using
the syntax : #myVariable#
They will be replaced by the text you have set.

There is 2 types of variable :
 - command : Defined when a project is created (project name, language...)
 - global  : Defined in a config file. (pseudo, copyright...)

Command variables are :
    - #project_name#  (project name given by the user)
    - #language#     (selected language)
    - #creation_date# (format : "DD MMM YYYY")
    - #creation_hour# (format : "HH:mm:ss")

Global variables are configurable here :
    ~/.bash_tools/.projia/globvars.bash

Check out the existing templates to get inspired on how to make yours.




III] Libraries

    Projia has a bunch of libraries available in a few languages that
are located in :
    ~/.bash_tools/.projia/#language#/lib/

    These libraries are utility libraries for some basic stuff (file
management, network use...) and are quite easy to manage. They are not
required for the use of a feature, but recommended for an easier
maintainability of the code.

    All that stuff has been made by myself (I.A.) but of course you can
add your own libraries inside the "lib" folder. As soon as you do it,
they will be automatically accessible via the command line when
creating a new project in the corresponding language.

Note : Each default library has an information header at the begining
       of the file giving information about all you have to know in
       order to use it.

WARNING : In some rare cases, a library require specific packages or
          other libraries. Make sure to have all the required stuff to
          make them work.




IV] Add a new language

    It is possible to add as many languages as possible in projia using
the command :
    > projia --add <languageName>

    Make sure to use a language name that can be applied to a file or
folder because adding a language will create a language directory in :
    ~/.bash_tools/.projia/

For instance, the C++ language has been created in projia like this :
    > projia --add C++

You should know all about language creation now.



Projia is part of Bash tools.
More information about Bash Tools at :
        https://github.com/iasebsil83/Bash_Tools

That is all for this tool, hope you will enjoy !




Contact     : i.a.sebsil83@gmail.com
Youtube     : https://www.youtube.com/user/IAsebsil83
GitHub repo : https://github.com/iasebsil83

Let's Code !                                  By I.A.
