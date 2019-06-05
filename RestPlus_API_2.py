from flask import Flask
from flask_restplus import Api, Resource, fields

app=Flask(__name__)
api=Api(app)

language_model = api.model('Language',{'language': fields.String('The language'),'id': fields.Integer(min=0)})

languages=[]
python = {'language':'Python'}
languages.append(python)


@api.route('/language')
class Language(Resource):
    @api.marshal_with(language_model)
    def get(self):
        return languages

    @api.expect(language_model)
    def post(self):
        new_language = api.payload
        new_language['id']= len(languages) + 1
        languages.append(new_language)
        return {'result':'languge added'}, 201

if __name__ =='__main__':
    app.run(debug=True)
