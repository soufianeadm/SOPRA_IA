from flask import Flask, render_template, request, redirect, url_for
import modules.vertex_ia as vertex_ia
from multiprocessing import Pool
import concurrent.futures


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apropos')
def test1():
    return render_template('apropos.html')

@app.route('/contact')
def test2():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['question_1']
        user_email = request.form['user_email']

        # Vous pouvez effectuer des actions avec les données du formulaire ici
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Submit the functions for execution
            future1 = executor.submit(vertex_ia.main)
            future2 = executor.submit(vertex_ia.main)
            future3 = executor.submit(vertex_ia.main)
            future4 = executor.submit(vertex_ia.main)

            # Retrieve the results
            reponse = future1.result()
            reponse2 = future2.result()
            reponse3 = future3.result()
            reponse4 = future4.result()

        # reponse= vertex_ia.main()
        # reponse2= vertex_ia.main()
        # reponse3= vertex_ia.main()
        # reponse4= vertex_ia.main()

        return render_template('submitted.html', question_1=reponse, user_email=user_email)

if __name__ == '__main__':
    app.run(debug=True)

