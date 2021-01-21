from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
from forms import NewsLetterForm
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/ourstory')
def ourstory():
    return render_template('ourstory.html', title='Our Story')

@app.route('/products')
def products():
    return render_template('products.html', title='Products')
    
@app.route('/applecake')
def applecake():
    return render_template('applecake.html', title='Apple cake')
    
@app.route('/custard')
def custard():
    return render_template('custard.html', title='Custard Tart')
    
@app.route('/donuts')
def donuts():
    return render_template('donuts.html', title='Donuts')
    
@app.route('/randy')
def randy():
    return render_template('randy.html', title='Randy Tart')
    
@app.route('/raspberry')
def raspberry():
    return render_template('raspberry.html', title='Raspberry Cheesecake')
    
@app.route('/vanilla')
def vanilla():
    return render_template('vanilla.html', title='Vanilla Slice')
    
@app.route('/specials')
def specials():
    return render_template('specials.html', title='Specials')
    
@app.route('/brownies')
def brownies():
    return render_template('brownies.html', title='Brownies')  
    
# @app.route('/cart')
# def cart():
#     return render_template('car.html', title='Cart')


###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv')
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################
@app.route('/newsletter', methods=["GET","POST"])
def get_newsletter():
    form = NewsLetterForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        res = pd.DataFrame({'name':name, 'email':email}, index=[0])
        res.to_csv('./newsletter.csv', mode='a')
        return render_template('newsletter.html', form=form)
    else:
        return render_template('newsletter.html', form=form)