
from asyncio import QueueEmpty


def get_query_update(payload, table, table_name):
    data = []
    query = f"update {table_name} SET "
    for key, value in payload.items():
        query += f"{key} = ?,"
        data.append(value)
    query = query[:-1]
    query += f" where {table['column']} = {table['value']}"
    return (query, data)
        
        