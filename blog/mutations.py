import graphene
from . import models, types
from graphene import Mutation
from graphene_file_upload.scalars import Upload


#mutation sends data to database
class CreateUser(Mutation):
    user = graphene.Field(types.UserType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)
    
    
class CreateComment(Mutation):
    comment = graphene.Field(types.CommentType)

    class Arguments:
        content = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        post_id = graphene.ID(required=True)

    def mutate(self, info, content, user_id, post_id):
        comment = models.Comment(
            content=content,
            user_id=user_id,
            post_id=post_id,
        )
        comment.save()
        return CreateComment(comment=comment)
    

class CreatePost(Mutation):
    post = graphene.Field(types.PostType)
    content = graphene.String(required=True)
    user_id = graphene.ID(required=True)
    

    class Arguments:
        title = graphene.String(required=True)
        slug = graphene.String(required=True)
        content = graphene.String(required=True)
        user_id = graphene.ID(required=True)
        category_id = graphene.ID(required=True)
        featured_image = graphene.String(required=True)
        
    def mutate(self, info, title, slug, content, user_id, category_id, featured_image):
        # Create a new Post object with the provided data
        post = models.Post(
            title=title,
            slug=slug,
            content=content,
            user_id=user_id,
            featured_image=featured_image,
        )

        category = models.Category.objects.get(id=category_id)
        post.category = category

        # Save the new post to the database
        post.save()

        # Return the created post in the response
        return CreatePost(post=post)

class UpdatePostLike(Mutation):
    post = graphene.Field(types.PostType)

    class Arguments:
        post_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    def mutate(self, info, post_id, user_id):
        post = models.Post.objects.get(pk=post_id)
        if post.likes.filter(pk=user_id).exists():
            post.likes.remove(user_id)
        else:
            post.likes.add(user_id)
        post.save()
        return UpdatePostLike(post=post)

class UpdateCommentLikes(graphene.Mutation):
    comment = graphene.Field(types.CommentType)  # Use 'comment' here instead of 'comments'

    class Arguments:
        comment_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    def mutate(self, info, comment_id, user_id):
        comment = models.Comment.objects.get(pk=comment_id)
        if comment.likes.filter(pk=user_id).exists():
            comment.likes.remove(user_id)
        else:
            comment.likes.add(user_id)
        comment.save()
        return UpdateCommentLikes(comment=comment)
        