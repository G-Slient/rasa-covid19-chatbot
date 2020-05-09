## search state cases path
* greet
  - utter_greet
* search_no_patients{"location":"Maharashtra"}
  - action_search_no_patients
* goodbye
  - utter_goodbye

## search state cases + location
* greet
  - utter_greet
* search_no_patients
  - utter_ask_location
* inform{"location":"Maharashtra"}
  - action_search_no_patients
* goodbye
  - utter_goodbye

## search cases on date
* greet
  - utter_greet
* search_cases_ondate{"date":"April 25"}
  - action_search_cases_ondate
* goodbye
  - utter_goodbye

## search search_growth_rate
* greet
  - utter_greet
* search_growth_rate{"location":"Maharashtra"}
  - action_search_growth_rate
* goodbye
  - utter_goodbye

## search search_growth_rate + location
* greet
  - utter_greet
* search_growth_rate
  - utter_ask_location
* inform{"location":"Maharashtra"}
  - action_search_growth_rate
* goodbye
  - utter_goodbye

## search search_highest_rate
* greet
  - utter_greet
* search_highest_rate
  - action_search_highest_rate
* goodbye
  - utter_goodbye

## search check_zone
* greet
  - utter_greet
* check_zone{"location":"Chittoor"}
  - action_check_zone
* goodbye
  - utter_goodbye

## search check_zone + location
* greet
  - utter_greet
* check_zone
  - utter_ask_location
* inform{"location":"Chittoor"}
  - action_check_zone
* goodbye
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye


