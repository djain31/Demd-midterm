from flask import Flask, flash, request
from flasgger  import Swagger ###

app = Flask(__name__)
Swagger(app )

@app.route('/')


def base_route():
    return "Welcome to Praxis"

@app.route("/hello",methods=["GET","POST"])
def hello():   
    """
    Lets try Swagger from Flasgger
    ---
    parameters:
        - name : Username
          in: query
          type: string
          required: true


    responses:
        200:
            description: The result is 

    """
    try:
        name = request.args.get("Username")    
        # numb = request.args.get("RollNo")
        return f"Welcome {name}",201
    except Exception as e:
        return f"Error occurred with message : {e}",401


if __name__ == "__main__":
    app.run(port=8080)
