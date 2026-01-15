favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': "rust",
    'Arun':'python'
}

print(favorite_languages)
for favorite_language in favorite_languages.keys():
    print(favorite_language.title())
     
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    