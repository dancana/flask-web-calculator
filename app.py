#activate scripts in venv with venv\Scripts\Activate.ps1
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

from flask import Flask, request, render_template

expression = ''

app = Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def index():
    global expression
    result = ''
    
    if request.method == 'POST':
        value = request.form.get('submit')
        
        if value == 'Clear':
            expression = ''
            result = ''
        elif value == '=':
            
            try:
                result = str(eval(expression))
                expression = result
            except:
                result = 'Error'
                expression = ''
    
        else:
            expression += value
            try:
                result = str(eval(expression))
            except:
                result = ''
    
    return render_template('index.html',expression=expression, result=result)



if __name__ == "__main__":
    app.run(debug=True)
