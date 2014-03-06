def object_detail_link(object):
    return str.format("/{}/{}/",object.__class__.__name__.lower(), object.id)
