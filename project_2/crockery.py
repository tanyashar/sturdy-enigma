from flask import Flask
from flask import url_for, render_template, request, redirect
import json
import os

app = Flask(__name__)

@app.route('/')
def page_main():
    if os.path.getsize('f.json') == 0:
        a = []
        json.dump(a, open('f.json', 'w'))
        
    lst = json.load(open('f.json', 'r'))
    if len(request.args)!=0:
        lst.append(request.args)
    
    json.dump(lst, open('f.json', 'w'))
    return render_template('main_page.html')

      
@app.route('/json')
def page_json():
    lst = json.load(open('f.json', 'r'))
    return render_template('json.html', lst=lst)


@app.route('/stats')
def page_stats():
    lst = json.load(open('f.json', 'r'))

    male=female=0
    kol = 0
    for i in lst:
        if i['sex']=='male':
            male += 1
        else:
            female += 1

        if i['type_1']=='bowl' and i['type_2']=='little-bowl':
            if i['type_3']=='salad-bowl' and i['type_4']=='tea-bowl':
                if i['type_5']=='bowl' and i['type_6']=='cup':
                    kol += 1

    s = male + female
    return render_template('stats.html', male=male, female=female, kol=kol, s=s)
    #return render_template('stats.html')

            
@app.route('/search')
def page_search():
    return render_template('search.html')


@app.route('/results')
def page_results():
    dct = request.args
    lst = json.load(open('f.json', 'r'))

    lst_cr={}
    num = 0
    for i in lst:
        if int(dct['age_l']) <= int(i['age']) < int(dct['age_r']):
            lst_cr[i[dct['type']]]=''
            num += 1
            
    return render_template('results.html', dct=dct, num=str(num), lst_cr=lst_cr)

if __name__ == '__main__':
    app.run(debug=True)
