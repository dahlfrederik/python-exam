# python-exam

This git repo is for the examp project for 4 semester elective python at CPH Business Lyngby.

**Group members:**
- Thor Christensen | cph-tc147@cphbusiness.dk
- Josef Marc | cph-jp325@cphbusiness.dk
- Frederik Dahl | cph-fd76@cphbusiness.dk

**Project name:**
- Numberplate scanner to value your car

**Short description:**
This project lets you scan a numberplate of a car and based on this numberplate it will predict the current value of the car.

**List of used technologies**
- Selenium
- BeutifulSoup
- Numpy
- PyTesseract
- CV2 
- Matploblib 
- Imutils 
- SKLearn 
- Pandas 


**Installation guide (if any libraries need to be installed)**
We assume that the user is running this project from the docker enviroments used in this semester. 

Never the less you have to install these librarys:  
- pip install pytesseract
- pip install imutils


**User guide (how to run the program)**
1. Open the program in jupyter notebook 
2. 


**Status (What has been done (and if anything: what was not done))**
What has been done: 
- The program can read a numberplate from a picture and convert it into a string 
- Webscrape the numberplate on nummerplade.net 
- Webscrape data about the car model on bilbasen.dk 
- Put data into a DataFrame 
- Normalizing the data 
- Divide data into test data and training sets, used for regression 
- Training our linear regression model
- Compare the regressions models predictions to real results 
- Predict the price of the car which numberplate we scanned in the beginning 

What has not been done: 
- Explain the accuray of our regression model
- Data visualisation 

**List of Challenges you have set up for your self (The things in your project you want to highlight)**
- Numberplate to string 
- Searching for model on bilbasen 
- Predicting car value with our regression model (also including the setup of the model) 

