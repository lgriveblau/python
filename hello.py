def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'en':
        return 'Hello'
    else:
        print 'Error'

lang = raw_input('Select your language: ')
name = raw_input('nme: ')
print greet(lang), name
