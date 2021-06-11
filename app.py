from flask import Flask, make_response, request
import io
from io import StringIO
import csv
import pandas as pd
import numpy as np
import pickle



app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return """
        <html>
  <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://kit.fontawesome.com/bed68fbb2f.js" crossorigin="anonymous"></script>
  </head>
  <body>
    <div style="background-image: url('https://image.freepik.com/free-vector/information-technology-with-infographic-elements-flat-icons-cogs-gear-wheel-mechanisms-hi-tech-digital-technology-engineering-abstract-technical-background_302149-58.jpg'); background-size: cover; height:100vh; padding-top:50px; text-align: right;">
        <div class="container">
        <div class="row">
            <div class="col-12">
                <h1 style=" color: black; font-size: 60px; font-family: 'Bree Serif'; font-style: italic;">Fault Diagnosis...</h1>
                </br>
                </br>
                <p style="font-style: italic"> Insert your CSV file and then download the Result</p>
                </br>
                </br>
                <form action="/transform" method="post" enctype="multipart/form-data">
                <input type="file" name="data_file" class="btn btn-white"/>
                </br>
                </br>
                </br>
                </br>
                <button type="submit" class="btn btn-primary button">Predict</button>
                </form>
            </div>
        </div>
    </div>
    </div>
  </body>
</html>
    """
@app.route('/transform', methods=["POST"])
def transform_view():
    f = request.files['data_file']
    if not f:
        return "No file"

    stream = io.StringIO(f.stream.read().decode('ISO-8859-1'), newline=None)
    csv_input = csv.reader(x.replace('\0', '') for x in stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    print(csv_input)
    for row in csv_input:
        print(row)

    stream.seek(0)
    result = transform(stream.read())

    df = pd.read_csv(StringIO(result))
    

    # load the model from disk
    loaded_model = pickle.load(open('finalized_model3.pkl', 'rb'))
    df['prediction'] = loaded_model.predict(df)

    

    response = make_response(df.to_csv())
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return response

if __name__ == "__main__":
    app.run(debug=True,port=9000)