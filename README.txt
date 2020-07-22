This whole system can be used as a shared bike system which can provide bike rent service for user and bike management service for manager and operator.

—How to run it?—
There are 4 .py files and 1 .sql files in total. The main file is all_ui and also the entrance of the program is in it. You need to install MySQL on your computer first. Then import sql files into your computer. Details of the database is listed as follows for setting up: 
host="localhost", user="root", passwd="Liyize97", db="SharedBikes", charset="utf8”.
You can also change the name of variable SQL_Password in the head of each .py files to apply it to your computer.

Then import all .py files into one python project and by running all_ui.py, you can properly see the whole project.

—Login & Register—
No matter you are user/operator/manager, you can directly input your username and password  to login. The system will automatically distinguish your identification can switch to corresponding system. 

By clicking Register button, you will be redirect to a new window to register. Input your information correctly then you are good to go. And if your username has already been taken, you will receive a warning message.

—For User—
1. Check bikes nearby
Once you enter the main window for user, you can firstly check the status of the station you choose by entering the station number ONLY and clicking Check button. You will be shown a list of bikes in this specific station you just input.

2.Rent a bike
Input bike’s number you just checked and click Rent. You are all set and good to go! But before you rent it, check the condition of the bike in case anything goes wrong with it. Once you found it is broken, you can report that situation by clicking Report button.

3.Return a bike
Input the number of a station where you would like to return your bike. Then click Return, you just finish a trip and free to leave!

4.Pay
After returning the bike, you can check how much you just spent and pay the bill. By clicking My Account button and Refresh button within it, you can check everything you’d like to know. And you can just push Pay button to pay for your last ride.

—For Operator And Manager—
1.Track all bikes’ status
Once you enter the management interface, all the information has already been put on the box  in the window. Including all bikes’ id, location and their current status(broken or not and being used or not).

2.Repair a bike
By entering the bike operator just repaired and clicking Repair button. This broken bike’s status will be updated and user can rent it again.

3.Move a bike
Enter bike’s id, the station this bike will end up with. Then this bike is virtually and psychically moved to another station. 

4.Generate report
There is a clear button and by just gently clicking it, you got a fabulous chart to illustrate all the bike’s information in a very intuitive way. It will show during a defined time period, how many bikes are reported as broken. The chart will be saved in your local drive and to will be put into the same folder where this program locates in.