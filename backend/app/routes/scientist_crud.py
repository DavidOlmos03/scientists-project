from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.scientist_service import (
    get_all_scientists, get_scientist_by_id, create_scientist, update_scientist, delete_scientist
)

scientist_api = Namespace('scientists', description='Operations related to scientists')

scientist_model = scientist_api.model('Scientist', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='The name of the scientist'),
    'birthday': fields.String(description='The birthday of the scientist'),
    'description': fields.String(description='A brief description of the scientist'),
    'area': fields.String(description='The area of expertise of the scientist')
})

@scientist_api.route('/')
class ScientistList(Resource):
    @scientist_api.marshal_list_with(scientist_model)
    def get(self):
        return get_all_scientists()

    @scientist_api.expect(scientist_model)
    def post(self):
        data = request.get_json()
        scientist_id = create_scientist(data['name'], data.get('birthday'), data.get('description'), data.get('area'))
        return {'id': scientist_id, **data}, 201

@scientist_api.route('/<int:id>')
class Scientist(Resource):
    @scientist_api.marshal_with(scientist_model)
    def get(self, id):
        scientist = get_scientist_by_id(id)
        if scientist:
            return {'id': scientist[0], 'name': scientist[1], 'birthday': scientist[2], 'description': scientist[3], 'area': scientist[4]}
        scientist_api.abort(404, f"Scientist {id} not found")

    @scientist_api.expect(scientist_model)
    def put(self, id):
        data = request.get_json()
        update_scientist(id, data['name'], data['birthday'], data['description'], data['area'])
        return {'id': id, **data}

    def delete(self, id):
        delete_scientist(id)
        return {'message': f'Scientist {id} deleted'}, 200
