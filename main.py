import pandas as pd

# reads in the csv file which is saved in the directory
encryptionkey = pd.read_csv("decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

# creates a DataFrame which defines the data source for the DataFrame
df = pd.DataFrame(data=encryptionkey)

# within the df, these following lines will redefine the data types from the
#   csv file. Allows for better data handling
df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)


# this function will take in a message as a parameter and split it up character by character
def split(message):
    return [char for char in message]


# definition for a function which codes a message
def code_message(message):
    coded_message = ""

    message_split = split(message)

    # for loop to go through each char in message_split and encrypt it
    for i in range(len(message_split)):
        j = message_split[i]

        try:
            # sets coded_char to the encrypted version of the character
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
        except:
            # if a character is unrecognized in my encryption, use @@@
            print('unrecognized character')
            coded_char = '@@@'

        # add the coded char to the encrypted message string
        coded_message = coded_message + coded_char

    return coded_message


# function definition to decode a message
def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]
        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word


def code_entry():
    code_response = input('What\'s the secret code in order to enter the decryption tool?\n')
    return 1 if code_response == '12345' else 0


def command_line_interaction():
    print('Welcome to encryption by Graham!!')
    user_action = input('\nEnter 0 to encrypt a message and 1 to decrypt a message: ')

    if user_action == '0':
        to_encrypt = input('\nEnter the plain text message you would like to encrypt:\n')
        encrypted = code_message(to_encrypt)
        print('Here is your encrypted message:\n' + encrypted)

    elif user_action == '1':
        if code_entry():
            to_decrypt = input('\nEnter the encrypted message you would like to decrypt:\n')
            decrypted = decode_message(to_decrypt)
            print('Here is your decrypted message:\n' + decrypted)
        else:
            print("Nice try, no entry today...cya")

    else:
        print('You\'ve entered an invalid input, goodbye...')
        return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    command_line_interaction()
