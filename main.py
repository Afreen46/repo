from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        return render_template('success.html')
    return render_template('index.html')

if __name__=="__main__":
    print("afreen")
    app.run()
