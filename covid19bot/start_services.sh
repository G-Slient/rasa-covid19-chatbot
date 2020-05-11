cd app/
# Start rasa server with nlu model
rasa run actions & rasa run --m models --enable-api --cors "*" --debug -p $PORT