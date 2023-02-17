from flask import render_template, request, flash, redirect
from app import flask_app
from app.forms import ConversionForm

@flask_app.route('/', methods=['GET'])
@flask_app.route('/index', methods=['GET'])
def index():
    form = ConversionForm()
    decimal_result = None
    binary_result = None
    if request.method == 'GET':
        decimal = request.args.get('decimal')
        if decimal:
            binary_result = f'{int(decimal):0b}'
        binary = request.args.get('binary')
        if binary:
            decimal_result = f'{int(binary, 2)}'
    return render_template('index.html', form=form,
                           binary_result=binary_result,
                           decimal_result=decimal_result)
