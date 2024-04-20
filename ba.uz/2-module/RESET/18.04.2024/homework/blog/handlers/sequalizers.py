def sequalizers_post(data, many=False):
    if many is True:
        return list(map(lambda post: {
            'category': post.category.name,
            'title': post.title,
            'author': post.author.name,
            'description': post.description,
            'created_at': post.created_at,
            'is_published': post.is_published,

        }, data))
    return {
        'category': data.category.name,
        'title': data.title,
        'author': data.author.name,
        'description': data.description,
        'created_at': data.created_at,
        'is_published': data.is_published,

    }


def sequalizers_comment(data, many=False):
    if many is True:
        return list(map(lambda comment: {'author': comment.author.name,
                                         'post': comment.post.title,
                                         'message': comment.message,
                                         'created_at': comment.created_at,
                                         }, data))

    return {'author': data.author.name,
            'post': data.post.title,
            'message': data.message,
            'created_at': data.created_at,
            }
