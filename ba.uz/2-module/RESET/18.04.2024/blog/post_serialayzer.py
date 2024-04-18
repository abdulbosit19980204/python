def commets_serialize(data):
    return list(map(lambda comment: {
        'id': comment.id,
        "message": comment.message
    }, data))


def data_serialize(data, many=False, comments=None):
    if many is True:
        return list(map(lambda post: {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'created_at': post.created_at
        }, data))

    return {
        'id': data.id,
        'title': data.title,
        'description': data.description,
        'created_at': data.created_at,
        "comments": comments,
    }
