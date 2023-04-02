from flask import Flask,jsonify

app=Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello,world'

def sum(a,b):
    return a+b



def avg(a,b):
    return (a,b)/2


@app.route('/ams/<int:n>')
def ams(n):
    sum=0
    order=len(str(n))
    t=n
    while(n>0):
        d=(n%10)
        sum+=d**order
        n=n/10

    if(sum==t):
        print("yes")
        result={
            "Number":t,
            "Sum":sum,
            "order":d,
            "Amstrong":True,
            "kas":"1515.151.112"
        }
    else :
        print("No")
        result={
            "Number":t,
             "Sum":sum,
            "order":d,
            "Amstrong":False,
            "kas":"1515.151.112"
        }   


    return jsonify(result)

if  __name__=="__main__":
    app.run(debug=True)    

