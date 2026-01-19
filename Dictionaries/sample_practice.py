user={
    'arun':{
        'first_name':'Arun',
        'last_name':'Pasala',
        'college':'Western New England University',
    },
    'jaya': {
        'first_name':'Jaya',
        'last_name':'Bandanadam',
        'college':'st.Francis College',
    }
}
for username, user_info in user.items():
    print(f"\n username: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    college = user_info['college']
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tCollege: {college.title()}")
    print("\n {username} is attending {college} ".format(username=username.title(), college=college.title()))
