
try:
    from pathlib import Path
    import os
    import requests
    from requests.auth import HTTPBasicAuth
    import cache_functions as cache

    #LINE 7 is for development purposes ONLY
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    from dotenv import load_dotenv
    load_dotenv()
    env_path=Path('.','.env')
    load_dotenv(dotenv_path=env_path)
    from flask import Flask,render_template,url_for,request,redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
except Exception as e:
    print("Some Modules are Missing {}".format(e))


app = Flask(__name__)
app.config["SECRET_KEY"]=os.getenv('SECRET_KEY')

github_blueprint = make_github_blueprint(client_id=os.getenv('CLIENT_ID'),
                                         client_secret=os.getenv('CLIENT_SECRET'), scope='repo')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

APP_CACHE=cache.open_cache()


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            if 'account_info' not in APP_CACHE.keys():
                APP_CACHE['account_info']=account_info_json
            else:
                if APP_CACHE['account_info'] != account_info_json:
                    APP_CACHE['account_info']=account_info_json

            cache.save_cache(APP_CACHE)
            return render_template("credentials.html", account_name=account_info_json['login'])

    return '<h1>Request failed!</h1>'

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        ownername=APP_CACHE['account_info']['login']
        repo_name=request.form['reponame']

        url=f"/repos/{ownername}/{repo_name}/commits"
        fetched_data=github.get(url)
        if fetched_data.ok:
            fetched_data_json=fetched_data.json()
            return render_template('result.html', repo_data=fetched_data_json)

if __name__ == "__main__":
    app.run(debug=True)