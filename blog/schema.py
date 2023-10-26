import graphene
from blog import queries,types
from .mutations import CreateUser, CreateComment, UpdatePostLike, UpdateCommentLikes, CreatePost
import graphql_jwt
from graphene_file_upload.scalars import Upload

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)
    
    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_comment = CreateComment.Field()
    update_post_likes = UpdatePostLike.Field()
    update_comment_likes = UpdateCommentLikes.Field()
    create_post = CreatePost.Field()
    
schema = graphene.Schema(query=queries.Query, mutation=Mutation)