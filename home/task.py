from bucket import bucket


def all_bucket_object_task():
    res = bucket.get_object()
    return res


def delete_single_object_task():
    res = bucket.delete_obbject()
    return res