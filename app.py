from flask import Flask, render_template, request, redirect
from services.queue import Queue

app = Flask(__name__)

queue = Queue()

@app.route('/')
def view_form():
    queue_length = queue.length()
    if queue_length > 10:
        custom_counter = queue_length - 9 
    else:
        custom_counter = 0 
    first10 = queue.next()
    print('tamaño de la cola', queue_length)
    print('Primeros diez', first10)
    mensaje = ""
    if queue.length() >= 10:
        mensaje = 'La cola está llena!'
    return render_template('index.html', queue_length=queue.length(), first10=first10, mensaje=mensaje, custom_counter=custom_counter)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        item = request.form.get('items')
        if item:
            queue.enqueue(item)
            print(item)
            print(queue.items)  
    return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
    if request.method == 'POST':
        item = request.form.get('items')
        if item:
            queue.dequeue(item)
            print('Elemento borrado', item)
            print(queue.items)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    queue.clear()
    return redirect('/')

@app.route('/recorrer', methods=['POST'])
def recorrer():
    queue.nextelement()
    return redirect('/')

print('tamaño de la colaws', queue.length())

if __name__=='__main__':
    app.run(debug=True)