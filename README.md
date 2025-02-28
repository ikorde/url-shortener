# URL Shortener! 

  
This URL Shortening tool will take a URL and generate a shortened URL using TinyURL. 

  

## Running the code
This project is built in Python3, this will need to be installed on your machine. 

This project requires the following Python libraries:

 - Flask
 - pickledb
 - pyshorteners

### Setup Instructions
	
    # First Clone or download this repository.
    # Create a virtual environment from the url-shortener directory
    python3 -m venv venv
    
    # Activate the virtual environment
    # If using a Mac/Linux machine:
    source venv/bin/activate
    # If using a Windows machine:
    venv\Scripts\activate
  
	# Install the dependencies
    pip3 install -r requirements.txt
    
    # Navigate to the app directory, and run the app
    python3 app.py

  

## Further Development
Given more time to refine this project I would make the following updates: 

 - Deploy the app to a public server"
 - Refine the UI for displaying the result, it is repetitive and verbose right now, writing a template for this would be better.
 - Add functionality to generate custom URLS. I utilized the pyshorteners library here for the sake of efficiency. 
 - If this needed to scale, I would utilize a more robust database, such as PostgreSQL, that is hosted on a server rather than using PickleDB. I would also implement caching in case of a spike in hits to a particular URL.


## Notes
I spent a total of 3 hours on this assignment.
