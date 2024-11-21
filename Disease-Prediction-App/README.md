# Disease Detection App

The Disease Detection App is a Streamlit-based web application that assists in 

identifying the presence of various diseases using machine learning models. 

The app provides a user-friendly interface where users can log in, view information 

and interact with disease detection functionalities. 

## Features

- User Authentication: Secure login system with session management using cookies.
- Image Slideshow: Automatically rotates through images related to different diseases.
- Logout Functionality: Easily accessible from the side menu.
- MongoDB Integration: User credentials and sessions are managed with MongoDB.


## Prerequisites
  - Python 3.7+
  - MongoDB Atlas or Local MongoDB instance

## Setup instructions

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
git clone <repository-url>
cd disease_detection_app/src
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure MongoDB

  - Open the config.yaml file and update the key and name fields with your desired settings.
    
  - If necessary, modify the MongoDB connection URI in Home.py to match your MongoDB setup.

## Set Up Users

   Before running the app, you need to insert initial users into your MongoDB collection. 
   
   Navigate to the src/ directory and run:

   ```bash
  python setup_mongo.py
  ```
## Run the Application

 - Start the Streamlit app by navigating to the src/ directory and running:

 ```bash
  streamlit run Home.py

  ```
- Open your web browser and go to http://localhost:/ to view and interact with the app.

## Contributing

Pull requests are welcome. For major changes, please open an issue first

to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
