from flask_restful import Resource

from api.controller.v1 import RepositoryController


class RepositoryResorce(Resource):
    def get(self, repository_id=None):
        # Get api/v1/repositoreis  --> Repository List.
        # Get api/v1/repositoreis/<repository_id>  --> Get Repository.
        if repository_id is None:
            return RepositoryController.get_repositories()
        else:
            return RepositoryController.get_repository(repository_id)

    def post(self):
        # Post api/vi/repositories --> Create a new Repository.
        # Post api/v1/repositories/<repository_id> --> Not allowed.
        return RepositoryController.create_repository()

    def patch(self, repository_id):
        # PATCH api/vi/repositories --> Not allowed.
        # PATCH api/v1/repositories/<repository_id> --> Update an existing Repository.
        return RepositoryController.update_repository(repository_id)

    def delete(self, repository_id):
        # DELETE api/vi/repositories --> Not allowed.
        # DELETE api/v1/repositories/<repository_id> --> Delete an existing Repository.
        return RepositoryController.delete_repository(repository_id)
