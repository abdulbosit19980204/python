def sequalizers_post(data, many=False):
    if many is True:
        plst = []
        for post in data:
            print(post.author)
            data = {
                'title': post.title,
                'author': post.author.name,
                'description': post.description,
                'created_at': post.created_at,
                'is_published': post.is_published,

            }
            plst.append(data)
        return plst
    return {
        'title': data.title,
        'author': data.author.name,
        'description': data.description,
        'created_at': data.created_at,
        'is_published': data.is_published,

    }


def sequalizers_comment(data, many=False):
    if many is True:
        comments = []
        for comment in data:
            c = {'author': comment.author.name,
                 'post': comment.post.title,
                 'message': comment.message,
                 'created_at': comment.created_at,
                 }
            comments.append(c)

        return comments

    return {'author': data.author.name,
            'post': data.post.title,
            'message': data.message,
            'created_at': data.created_at,
            }
