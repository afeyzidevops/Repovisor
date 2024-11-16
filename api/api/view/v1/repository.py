from flask_restful import Resource


class RepositoryResorce(Resource):
    def get(self, repository_id=None):
        return {"ping": "Pong"}

    def post(self):
        return {"ping": "pong"}

    def patch(self, repository_id):
        return {"ping": "pong"}

    def delete(self, repository_id):
        return {"ping": "pong"}
