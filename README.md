# TkinterProjWithDB
My very first project on Python 2.7 with Tkinter GUI Library.

Author/Coder :- Tanay Gupta 
				                                   
                                           
                                            Student Management System
->All the Entries/Button/objects are made user friendly , so even if user does mistake, it will pop up with an error window with info displaying on screen.(This includes syntax errors too.)


Screen 1:- (uses login database file)	
			default username:- tanaygupta2009
			default Password:- pass2009
		(However, A new Account can be made with signup button)
->Login/Signup Screen, Has a seprate database for login accounts.
->With 'Signup' button, A new account can be created, username is a primary key so make sure its 	unique in each case otherwise the programm will keep on displaying error.
->The Login button checks your credentials are correct or not, if it is correct then only the programm will furthur proceed.
->Email should be entered in correct format (for eg: email@example.com), displays an error otherwise.

Screen 2:-(Uses dbproj database file)
->By Successfully logging in , a new Screen will appear with seprate database maintained for it./<Screen2>/
->The Button new entry contains some required fields for data insersion for new student, will directly insert data to a table in database with Enrollment number as primary key./<Screen3>/
->Button Marks Entry is for entering marks of a student, has its own seprate table in database with foreign key Enrollment number./<Screen4/
->Button 'Show Result' displays another window with Enrollment And result in percentage respectively. It also has its own database table with Enrollment number as a foreign key. Will display all the info present in current database records./<Screen5>/
->Button 'Show Info' Displays all the Student info entered by the user, it has five columns and it retrives data from student table with Enrollment number as a primary key. /<screen6>/
->Button 'SignOut' destroys all the windows except login screen.

Screen 3:-
-> all the entries are to be made with enrollment being primary key, it should be unique.
->unique drop down menu for Entering Date of bith
->has its own database. 
->Several checks are made.
->reset button will reset all input fields.

Screen 4:-
->Enrollment number as a forign key , should be entered first in screen 3.
->has its own database. 

Screen 5,6:-
->To retrive and display data from database 'dbproj'
