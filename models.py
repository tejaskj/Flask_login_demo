from .db import get_data_as_dict, insert_data

def register_user(data):

    query = f"""
        INSERT INTO public.users (fname, lname, email, username, password)
        VALUES (%s, %s, %s, %s, crypt(%s, gen_salt('bf')))
    """
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    username = data['username']
    password = data['password']

    new_data = insert_data(query, fname, lname, email, username, password)

    return new_data
