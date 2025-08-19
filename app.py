from flask import Flask, render_template, request ,url_for,redirect
from methods import todo

app = Flask(__name__)
todo_list = []
fihisk_list =[]

def del_item(li, ind):
    try:
        del li[ind]
    except IndexError:
        pass  # Optional: silently ignore out-of-range indexes
@app.route("/", methods=["GET", "POST"])
@app.route("/ADD", methods=["GET", "POST"]) 
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form.get('action')  # 'add' or 'view'

        if action == "add":
            title = request.form.get('title')
            content = request.form.get('content')
            if title and content:
                new_todo = todo(title, content)
                todo_list.append(new_todo)

        elif action == "view":
            # Just render the list, nothing to add
            pass
    if request.method == "POST":
        if "delete"in request.form:
            index = int(request.form["delete"])
            if 0<=index<len(todo_list):
                todo_list.pop(index)
        elif "fin" in request.form:
                index = int(request.form["fin"])
                if 0<=index<len(todo_list):
                    fihisk_list.append(todo_list[index])
                    todo_list.pop(index)
                   
                    
    return render_template('additem.html', list=todo_list ,del_item= del_item)


@app.route("/List", methods=["GET", "POST"])
def List():
    if request.method == "POST":
        if "delete"in request.form:
            index = int(request.form["delete"])
            if 0<=index<len(todo_list):
                todo_list.pop(index)
        elif "fin" in request.form:
                index = int(request.form["fin"])
                if 0<=index<len(todo_list):
                    fihisk_list.append(todo_list[index])
                    todo_list.pop(index)
        if  "delete"in request.form:
            index = int(request.form["delete"])
            if 0<=index<len(fihisk_list):
                fihisk_list.pop(index)
    return render_template('list.html',list=todo_list,fin=fihisk_list,del_item= del_item )


if __name__ == '__main__':
    app.run(debug=True) 

