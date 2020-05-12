# Rasa-Covid19-Chatbot
This is a chatbot developed to provide information about the covid-19 cases

### **Short Glimpse of the working of chatbot**

<img src = "images/short.gif">

## How to use this repo

### How to set-up the environment

In ubuntu 18.04, these are steps to be followed to setup the project env

Step 1: Create a Virtual Environment

    python3 -m venv myenv

Step 2: Activate the virtual env 

    Source myenv/bin/activate

Step 3: Deactivate the conda env if it exits

    conda deactivate

Step 4: Install the requirements 

    pip3 install -r requirements.txt

    or 

    pip3 install rasa==1.9.6


### Training the NLU model

Since the release of Rasa 1.0, the training of the NLU models became a lot easier with the new CLI. Train the model by running:  

    rasa train nlu

Once the model is trained, test the model:

    rasa shell nlu

### Training the dialogue model

The biggest change in how Rasa Core model works is that custom action 'actions' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` rasa run actions```  

2. Open a new terminal and train the Rasa Core model by running:  

``` rasa train```  
 
3. Talk to the chatbot once it's loaded after running:  

```rasa shell```  


### Starting the interactive training session:

To run your assistant in a interactive learning session, run:
1. Make sure the custom actions server is running:  

```rasa run actions```  

2. Start the interactive training session by running:  

```rasa interactive```  


### Steps to run the complete project

Run the below steps in different terminals

Step 1: Run the Flask server for getting covid data

    python app.py

Step 2: Run the Actions Server 

    rasa run actions

Step 3: Run the Shell to interact with bot

    rasa shell


## Integration with FrontEnd Website

Step 1: Run the Actions Server

    rasa run actions

Step 2: Run the rasa model

    python -m rasa run --m ./models --endpoints endpoints.yml --port 5005 --cors "*" -vv --enable-api

Step 3: Run the Flask Server for backend data

    python app.py

Step 4: Run the HTTP server for running website for chatbot  

The chatbot UI is provided in index.html 
Second version of the UI [forked](https://github.com/JiteshGaikwad/Chatbot-Widget) from another repo is also placed for individual learnings into chatbot frontend.

    python -m http.server 8008

    Here 8008 is port number, u can change if needed

The chatbot is ready at http://localhost:8008

***Note:* Still the bot needs lot of training data. We can integrate RASA-X for this purpose which is not yet added into this project.**


### Tasks To-Do-List


- [x] create the basic project 
- [x] Make NLU training data
- [x] Make the dialogue management model
- [x] Make a flask server to extract the covid data from https://api.covid19india.org/
- [x] Create the more stories
- [x] Handle the spelling mistakes by the users
- [x] Handle the date format given by the users.
- [x] create a frontend application 
- [x] connect the frontend with the rasa-chatbot
- [x] deploy the flask server.
- [ ] deploy the chatbot app.

## References

1. [RasaMasterClass](https://www.youtube.com/channel/UCJ0V6493mLvqdiVwOKWBODQ) Official Youtube videos.

        Along with references, detailed blogs will be posted soon ...


