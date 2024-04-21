import socket
from getForm import get_latin_form

HOST = 'localhost'
PORT = 8099
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = (HOST, PORT)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a client to connect...')
    client_socket, client_address = server_socket.accept()
    print('Client connected from {}:{}'.format(*client_address))

    try:
        # Send the first message to the client
        message = '''Welcome to get_form for Latin! 
        Please enter a part of speech: noun, verb, or adjective
        You can also use the abbreviations: n, v, or a
     '''
        client_socket.sendall(message.encode())
        print('Sent message: {}'.format(message))
        
        # Receive data from the client
        data = client_socket.recv(1024)
        # Strip whitespaces from data
        data = data.strip()
        #make sure data only has alphabetic characters
        while not data.isalpha() or data[0].lower() not in ['n', 'v', 'a']:
            message = "Please enter a valid part of speech: noun, verb, or adjective"
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
        # save POS as first char and send next messages based on POS
        pos = data[0].lower()
        word = 'NULL'
        case = 'NULL'
        number = 'NULL'
        gender = 'NULL'
        mood = 'NULL'
        tense = 'NULL' 
        voice = 'NULL'
        person = 'NULL'
        if pos == 'n':
            message = 'You selected noun. Please enter a noun:'
            client_socket.sendall(message.encode())
            # Receive noun from the client
            noun = client_socket.recv(1024)

            while not  noun.isalpha():
                message = "Please enter a valid noun: only alphabetic characters are allowed"
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
            word = noun
            # Process the noun
            message = 'You selected noun. Please enter the case (nominative, genitive, dative, accusative, ablative) Use - for any:'
            client_socket.sendall(message.encode())
            # Receive case from the client
            case = client_socket.recv(1024)
            while (case.lower() not in ['nominative', 'genitive', 'dative', 'accusative', 'ablative']) and (case.lower() not in ['n', 'g', 'd', 'a', 'b', '-']):
                message = "Please enter a valid case: nominative, genitive, dative, accusative, ablative"
                client_socket.sendall(message.encode())
                case = client_socket.recv(1024)
            case = case.lower()
            if case == '-':
                case = 'NULL'
            # now number 
            message = 'You selected noun. Please enter the number (singular, plural) Use - for any:'
            # Receive number from the client
            number = client_socket.recv(1024)
            while (number.lower() not in ['singular', 'plural']) and (number.lower() not in ['s', 'p', '-']):
                message = "Please enter a valid number: singular or plural"
                client_socket.sendall(message.encode())
                number = client_socket.recv(1024)
            number = number.lower()
            if number == '-':
                number = 'NULL'
            # Receive gender from the client
            message = 'You selected noun. Please enter the gender (masculine, feminine, neuter) Use - for any:'
            client_socket.sendall(message.encode())
            gender = client_socket.recv(1024)
            while (gender.lower() not in ['masculine', 'feminine', 'neuter']) and (gender.lower() not in ['m', 'f', 'n', '-']):
                message = "Please enter a valid gender: masculine, feminine, neuter"
                client_socket.sendall(message.encode())
                gender = client_socket.recv(1024)
            gender = gender.lower()
            if gender == '-':
                gender = "NULL"
        #END NOUN

        elif pos == 'v':
            message = 'You selected verb. Please enter a verb:'
            client_socket.sendall(message.encode())
            # Receive verb from the client
            verb = client_socket.recv(1024)
            while not  verb.isalpha():
                message = "Please enter a valid verb: only alphabetic characters are allowed"
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
            word = verb

            # Receive person from the client
            message = 'You selected verb. Please enter the person (first, second, third) Use - for any:'
            client_socket.sendall(message.encode())
            person = client_socket.recv(1024)
            while (person.lower() not in ['first', 'second', 'third']) and (person.lower() not in ['1', '2', '3', '-']):
                message = "Please enter a valid person: first, second, third"
                client_socket.sendall(message.encode())
                person = client_socket.recv(1024)
            person = person.lower()
            if person == '-':
                person = 'NULL'

            message = 'You selected verb. Please enter the number (singular, plural) Use - for any:'
            # Receive number from the client
            number = client_socket.recv(1024)
            while (number.lower() not in ['singular', 'plural']) and (number.lower() not in ['s', 'p', '-']):
                message = "Please enter a valid number: singular or plural"
                client_socket.sendall(message.encode())
                number = client_socket.recv(1024)
            number = number.lower()
            if number == '-':
                number = 'NULL'

            # Receive tense from the client
            message = 'You selected verb. Please enter the tense (present, imperfect, future, perfect, pluperfect, future perfect) Use - for any:'
            client_socket.sendall(message.encode())
            tense = client_socket.recv(1024)
            while (tense.lower() not in ['present', 'imperfect', 'future', 'perfect', 'pluperfect', 'future perfect']) and (tense.lower() not in ['p', 'i', 'f', 'r', 'l', 'u', '-']):
                message = "Please enter a valid tense: present, imperfect, future, perfect, pluperfect, future perfect"
                client_socket.sendall(message.encode())
                tense = client_socket.recv(1024)
            tense = tense.lower()
            if tense == '-':
                tense = 'NULL'

            # Receive voice from the client
            message = 'You selected verb. Please enter the voice (active, passive) Use - for any:'
            client_socket.sendall(message.encode())
            voice = client_socket.recv(1024)
            while (voice.lower() not in ['active', 'passive']) and (voice.lower() not in ['a', 'p', '-']):
                message = "Please enter a valid voice: active, passive"
                client_socket.sendall(message.encode())
                voice = client_socket.recv(1024)
            voice = voice.lower()
            if voice == '-':
                voice = 'NULL'

            message = 'You selected verb. Please enter the mood (indicative, subjunctive, imperative) Use - for any:'
            client_socket.sendall(message.encode())
            # Receive mood from the client
            mood = client_socket.recv(1024)
            while (mood.lower() not in ['indicative', 'subjunctive', 'imperative']) and (mood.lower() not in ['i', 's', 'm', '-']):
                message = "Please enter a valid mood: indicative, subjunctive, imperative"
                client_socket.sendall(message.encode())
                mood = client_socket.recv(1024)
            mood = mood.lower()
            if mood == '-':
                mood = 'NULL'
        #END VERB

        elif pos == 'a':
            message = 'You selected adjective. Please enter an adjective:'
            client_socket.sendall(message.encode())
            # Receive adjective from the client
            adjective = client_socket.recv(1024)
            while not  adjective.isalpha():
                message = "Please enter a valid adj: only alphabetic characters are allowed"
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
            word = verb
            # adj case
            message = 'You selected adjective. Please enter the case (nominative, genitive, dative, accusative, ablative) Use - for any:'
            client_socket.sendall(message.encode())
            # Receive case from the client
            case = client_socket.recv(1024)
            while (case.lower() not in ['nominative', 'genitive', 'dative', 'accusative', 'ablative']) and (case.lower() not in ['n', 'g', 'd', 'a', 'b', '-']):
                message = "Please enter a valid case: nominative, genitive, dative, accusative, ablative"
                client_socket.sendall(message.encode())
                case = client_socket.recv(1024)
            case = case.lower()
            if case == '-':
                case = 'NULL'
            # now number 
            message = 'You selected adjective. Please enter the number (singular, plural) Use - for any:'
            # Receive number from the client
            number = client_socket.recv(1024)
            while (number.lower() not in ['singular', 'plural']) and (number.lower() not in ['s', 'p', '-']):
                message = "Please enter a valid number: singular or plural"
                client_socket.sendall(message.encode())
                number = client_socket.recv(1024)
            number = number.lower()
            if number == '-':
                number = 'NULL'
            # Receive gender from the client
            message = 'You selected adjective. Please enter the gender (masculine, feminine, neuter) Use - for any:'
            client_socket.sendall(message.encode())
            gender = client_socket.recv(1024)
            while (gender.lower() not in ['masculine', 'feminine', 'neuter']) and (gender.lower() not in ['m', 'f', 'n', '-']):
                message = "Please enter a valid gender: masculine, feminine, neuter"
                client_socket.sendall(message.encode())
                gender = client_socket.recv(1024)
            gender = gender.lower()
            if gender == '-':
                gender = "NULL"

        # Send a response back to the client
        response = get_latin_form(word=word, case=case, number=number, 
                                  gender=gender, mood=mood, tense=tense, 
                                  voice=voice, person=person)
        
        client_socket.sendall(response.encode())
        print('Sent respsonse: {}'.format(response))

    finally:
        # Clean up the connection
        client_socket.close()