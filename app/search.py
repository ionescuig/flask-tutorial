from flask import current_app

def add_to_index(index, model):
    print('--------------- [add_to_index] ---------------')
    if not current_app.elasticsearch:
        print('--------------- no current_app.elasticsearch ---------------')
        print('--------------- [END OF add_to_index] ---------------')
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    print('--------------- [END OF add_to_index] ---------------')
    current_app.elasticsearch.index(index=index, id=model.id, body=payload)

def remove_from_index(index, model):
    print('--------------- [remove_from_index] ---------------')
    if not current_app.elasticsearch:
        print('--------------- no current_app.elasticsearch ---------------')
        print('--------------- [END OF remove_from_index] ---------------')
        return
    print('--------------- [END OF remove_from_index] ---------------')
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    print('--------------- [query_index] ---------------')
    if not current_app.elasticsearch:
        print('--------------- no current_app.elasticsearch ---------------')
        print('--------------- [END OF query_index] ---------------')
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    print('--------------- [END OF query_index] ---------------')
    return ids, search['hits']['total']['value']
