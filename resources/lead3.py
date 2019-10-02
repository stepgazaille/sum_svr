from flask_restful import Resource, reqparse

class Lead3(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'doc',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        doc = Lead3.parser.parse_args()['doc']
        try:
            return {"summary": doc[:11]}
        except Exception as e:
            print(str(e))
            return {'message': 'There was a problem summarizing the document'}, 404
