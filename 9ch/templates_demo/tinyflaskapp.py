import sys, os
sys.path.append("/usr/local/lib/python3.4/dist-packages")
from flask import Flask, render_template, abort
app = Flask(__name__)
app.debug = True

objs = __builtins__.__dict__.items()
docstrings = {name.lower(): obj.__doc__ for name, obj in objs if
              name[0].islower() and hasattr(obj, '__name__')}

@app.route('/')
def index():
    return render_template('index.html', funcs=sorted(docstrings))

@app.route('/functions/<func_name>')
def show_docstring(func_name):
    func_name = func_name.lower()
    if func_name in docstrings:
        return render_template('docstring.html', func_name=func_name,
                               doc=docstrings[func_name])
    else:
        abort(404)

if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)), debug=False)
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
