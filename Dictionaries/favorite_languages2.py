favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward': ["rust","go"],
    'Arun':['python','java','c++']}
print(favorite_languages)
for user, languages in favorite_languages.items():
    # # if len(languages) >1:
    #     print(f"\n{user.title()}'s favorite languages are:")
    #     for language in languages:
    #         print(f"\t{language.title()}")
    # # else:
    # #     print(f"\n{user.title()}'s favorite language is:")
    # #     for language in languages:
    # #         print(f"\t{language.title()}")
    if len(languages) >2:
        print(f"\n{user.title()} knows more than two languages:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) >=1 and len(languages)<=2:
        print(f"\n{user.title()} knows only one language:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) <=1:
        print(f"\n{user.title()} knows only one language:")
        for language in languages:
            print(f"\t{language.title()}")
    
for name , language in favorite_languages.items():
    if len(language) >= 2:
            print(f"{name.title()} Knows multiple languages:")
    else:
            print(f"{name.title()} knows only one language:")
        