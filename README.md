# rasa-covid19-chatbot
This is a chatbot developed to provide information about the covid-19 cases

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

```rasa train nlu ```

Once the model is trained, test the model:

```rasa shell nlu```


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


## Integration with FrontEnd Website

    Coming soon ...

