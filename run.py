from app import app



if __name__ == '__main__':

    # app.run(debug=True, port=8989)
    app.run(debug=True, host='0.0.0.0', port=5001)