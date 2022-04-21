used Django and Postgres 

So the 'project' folder is the main folder that I started the project in, the exterior env folder contains the stuff i installed to make the thing work, like the django framework itself. You can activate the env to activate the things I installed without having to search for them and install them yourself individually. 

The NBAQuery folder represents what Django makes for you when you create the project. The Players folder represents what Django makes for you when you create an app within a project. 

So the 'Project' folder is the whole website, the 'NBAQUERY' folder is like the control center for the whole thing, and the app folders (like 'Players') are the individual pages/games/concepts that are on the website. 

The way Django works is it checks what url you are at through the url.py files, then fires the respective function from the views.py file, which usually just renders an html file which is stored in the templates folders. 
