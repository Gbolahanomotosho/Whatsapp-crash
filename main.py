#!/usr/bin/python3
#coding=utf-8
import os
import sys
import time 
from time import sleep


#### colours ####
# B='\033[1;94m'
# R='\033[1;91m'
# G='\033[1;92m'
# W='\033[1;97m'
# S='\033[1;96m'
# P='\033[1;95m'
# Y='\033[1;93m'
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'



Gbolly ="""\033[1;95m

 __.,,------.._
      ,'"   _      _   "`.
     /.__, ._  -=- _"`    Y
    (.____.-.`      ""`   j
     VvvvvvV`.Y,.    _.,-'       ,     ,     ,
        Y    ||,   '"\         ,/    ,/    ./
        |   ,'  ,     `-..,'_,'/___,'/   ,'/   ,
   ..  ,;,,',-'"\,'  ,  .     '     ' ""' '--,/    .. ..
 ,'. `.`---'     `, /  , Y -=-    ,'   ,   ,. .`-..||_|| ..
ff\\`. `._        /f ,'j j , ,' ,   , f ,  \=\ Y   || ||`||_..
l` \` `.`."`-..,-' j  /./ /, , / , / /l \   \=\l   || `' || ||...
 `  `   `-._ `-.,-/ ,' /`"/-/-/-/-"'''"`.`.  `'.\--`'--..`'_`' || ,
            "`-_,',  ,'  f    ,   /      `._    ``._     ,  `-.`'//         ,
          ,-"'' _.,-'    l_,-'_,,'          "`-._ . "`. /|     `.'\ ,       |
        ,',.,-'"          \=) ,`-.         ,    `-'._`.V |       \ // .. . /j
        |f\\               `._ )-."`.     /|         `.| |        `.`-||-\\/
        l` \`                 "`._   "`--' j          j' j          `-`---'
         `  `                     "`,-  ,'/       ,-'"  /
                                 ,'",__,-'       /,, ,-'
                                 Vvv'            VVv'

\033[1;92m┬ ┬┬ ┬┌─┐┌┬┐┌─┐┌─┐┌─┐┌─┐   ┌─┐┬─┐┌─┐┌─┐┬ ┬
\033[1;91m│││├─┤├─┤ │ └─┐├─┤├─┘├─┘───│  ├┬┘├─┤└─┐├─┤
\033[1;94m└┴┘┴ ┴┴ ┴ ┴ └─┘┴ ┴┴  ┴     └─┘┴└─┴ ┴└─┘┴ ┴

\033[1;95m[☢]By \033[1;92mC\033[1;93mY\033[1;94mB\033[1;95mE\033[1;96mR\033[1;97mS\033[1;91mP\033[1;94mL\033[1;95mO\033[1;92mI\033[1;96mT 🗼



\033[1;94m===============================================
\033[1;92m[☢]Author: Omotosho Gbolahan 
===============================================          
\033[1;91m[☢]Disclaimer: I wont be responsible for illegal use
\033[1;97m===============================================
 



                      
*====================================*
\033[1;95m[1] Crash WhatsApp number 
*====================================*                         
\033[1;96m[2] Crash WhatsApp Group
*====================================* 
         
"""


      



                                                                                                                                                               






for i in Gbolly:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.002)
print("\n\n")

try:

        menu = int(input("\033[1;92m[☢]Enter an option:\n\n\033[1;93m[☢]\033[1;92mC\033[1;93mY\033[1;94mB\033[1;95mE\033[1;96mR\033[1;97mS\033[1;91mP\033[1;94mL\033[1;95mO\033[1;92mI\033[1;96mT 🗼>>>>> "))
except ValueError:
        print("\033[1;92mEnter the correct number")
        time.sleep(3)
        loop()



if menu == 1:


    if os.path.exists('whatsapp-numbercrash.py'):
        os.system('clear')
        os.system("python3 whatsapp-numbercrash.py")
        

elif menu == 2:

    if os.path.exists('whatsapp-groupcrash.py'):
        os.system('clear')
        os.system("python3 whatsapp-groupcrash.py")



