import graphene
from blog import models
from blog import types


# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)
    all_posts = graphene.List(types.PostType)
    all_categories = graphene.List(types.CategoryType)
    all_tags = graphene.List(types.TagType)
    posts_by_category = graphene.List(types.PostType, category=graphene.String())
    posts_by_tag = graphene.List(types.PostType, tag=graphene.String())
    post_by_slug = graphene.Field(types.PostType, slug=graphene.String())
    comments = graphene.List(types.CommentType)
    user_by_id = graphene.List(types.UserType, id=graphene.String())
    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )
    def resolve_all_posts(root, info):
        return (
            models.Post.objects.all()
        )
    def resolve_all_categories(root, info):
        return (
            models.Category.objects.all()
        )
    def resolve_all_tags(root, info):
        return (
            models.Tag.objects.all()
        )
    def resolve_posts_by_category(root, info, category):
        return (
            models.Post.objects.filter(category__slug__iexact=category)
        )
    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.filter(tag__slug__iexact=tag)
        )
    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.get(slug__iexact=slug)
        )
    
    def resolve_comments(self, info):
        # Return the comments associated with this post
        return self.comment_set.all()
    
    # def resolve_user_by_id(root, info, id):
    #     return (
    #         models.Post.objects.get(id__iexact=id)
    #     )

    def resolve_user_by_id(root, info, id):
        try:
            user = models.User.objects.get(id=id)
            return [user]  # Wrap the user in a list
        except models.User.DoesNotExist:
            return [] 

