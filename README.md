# MariPOS (Experimental)

### Localhost based web application point of sale software


#### Installation
______

To install de depencencies open a terminal in the \backend folder and run
>- `python -m venv venv`  (Windows)
>- `python3 -m venv venv` (Linux/Mac)


Then start the virtual environment by running the command
>- `venv\Scripts\activate.bat` (Windows)
>- `sourse venv/bin/activate`  (Linux/Mac)

And then
>- `pip install -r requirements.txt`  (Windows)
>- `pip install -r requirements.txt` (Linux/Mac)

Update `pip` if needed.
Exit the virtual environment by running
>- `deactivate`


Open a terminal in the \frontend\maripos folder and run
>- `npm install`
  
*NOTE:* To run this command `Node.js` and `React` must be already installed. 
Vist ([https://nodejs.org/es/](https://nodejs.org/es/)) to install `Node.js` and then run the command
>- `npm install -g create-react-app`
_____

MongoDB is used as database, for this proyect to work mongodb must be running or be insatalled as a service in your system