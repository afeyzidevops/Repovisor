from api.util import jsonify


class RepositoryController:
    def get_repositories():
        return jsonify(code=101, status=501)

    def get_repository(repository_id):
        return jsonify(code=101, status=501)

    def create_repository():
        return jsonify(code=101, status=501)

    def update_repository(repository_id):
        return jsonify(code=101, status=501)

    def delete_repository(repository_id):
        return jsonify(code=101, status=501)
