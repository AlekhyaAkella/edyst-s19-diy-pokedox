from flask import Flask,render_template,jsonify
app=Flask(__name__)


#error handler for invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route('/api/pokemon/<int:id>')
def fun(id):
    if(id>0 and id<152):
        f=open("data.txt",'r')
        data=f.read()
        data=(eval(data))[id]
        data=jsonify(pokemon={'id':data[0],'name':data[1],'sprite':data[2]})
        return data
    else:
        return render_template("404.html"),404


if __name__ == "__main__":
    app.run(port=8006,debug=True)

