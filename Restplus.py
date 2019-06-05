from flask import Flask
from flask_restplus import Api, Resource, fields

app=Flask(__name__)
api=Api(app)

language_model = api.model('Language',{'language': fields.String('The language')})

languages=[]
python = {'language':'Python'}
languages.append(python)


@api.route('/language')
class Language(Resource):
    def get(self):
        return languages

    @api.expect(language_model)
    def post(self):
        languages.append(api.payload)
        return {'result':'languge added'}, 201

if __name__ =='__main__':
    app.run(debug=True)
