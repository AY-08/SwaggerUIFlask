from cProfile import run
from apiapplication import app

if __name__ == '__main__':
    app.run(debug=True,port=5000)