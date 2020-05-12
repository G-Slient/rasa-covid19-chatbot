from utils import getStateCases
from utils import totalCases
from utils import growthRateStates
from utils import highestGrowthRateState
from utils import getZoneType
from utils import preprocess_statedata
from utils import preprocess_districtdata
import warnings
warnings.simplefilter('ignore')
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/getstatecases", methods=['GET'])
def getstatecases():
    """
    endpoint: /getstatecases 
    method: GET
    params: loc 
    value: Short form of a state

    """
    loc = request.args['loc']
    df = preprocess_statedata()
    obj = getStateCases(df,loc)
    return jsonify(obj)


@app.route("/totalcases", methods=['GET'])
def totalcases():
    """
    example: http://127.0.0.1:5000/totalcases?date=06-May-20
    endpoint: /totalcases 
    method: GET
    params: date 
    value: 06-May-20 format

    """
    date = request.args['date']
    df = preprocess_statedata()
    obj = totalCases(df,date)
    return jsonify(obj)

@app.route("/growthrate", methods=['GET'])
def growthrate():
    """
    example: http://127.0.0.1:5000/growthrate?loc=tg 
    endpoint: /growthrate 
    method: GET
    params: loc
    value: short form of a state

    """
    loc = request.args['loc']
    df = preprocess_statedata()
    obj = growthRateStates(df,loc)
    return jsonify(obj)

@app.route("/highestgrowthrate", methods=['GET'])
def highestgrowthrate():
    """
    example: http://127.0.0.1:5000/highestgrowthrate
    endpoint: /highestgrowthrate
    method: GET
    params:None
    value: None

    """
    #loc = request.args['loc']
    df = preprocess_statedata()
    obj = highestGrowthRateState(df)
    return jsonify(obj)


@app.route("/getzonetype", methods=['GET'])
def getzonetype():
    """
    example: http://127.0.0.1:5000/getzonetype
    endpoint: /getzonetype
    method: GET
    params: loc
    value: distict name 

    """
    dis = request.args['loc']
    dfzones = preprocess_districtdata()
    obj = getZoneType(dfzones,dis)
    return jsonify(obj)


if __name__ == '__main__':
    app.run(port=8000,debug=True)