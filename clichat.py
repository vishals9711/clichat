import click
import json
import pyperclip
from PyInquirer import prompt, Separator
from halo import Halo
import termcolor
import pyfiglet
from utils import get_chat_response

def print_whole_but_color(start_string, text, color='light_yellow'):
    click.echo(termcolor.colored(start_string, color="light_yellow"), nl=False)
    click.echo(termcolor.colored(text, color), nl=False)
    click.echo()

@click.command()
def chat():
    click.echo(pyfiglet.figlet_format("C L I Chat"))

    while True:
        user_input = click.prompt(termcolor.colored("Query:", color="light_yellow"), prompt_suffix="")
        # user_input = "How to list files in a directory?"
        # Show spinner while waiting for response
        with Halo(text='Waiting for response', spinner='bouncingBar', text_color='grey'):
            try:
                chatbot_response = json.loads(get_chat_response(user_input))
            except ValueError as ve:
                click.echo(termcolor.colored(f"Error: {ve}", color="red"))
                break
            except Exception as e:
                click.echo(termcolor.colored(f"Error: {e}", color="red"))
                break

        print_whole_but_color("Code : ", f"{chatbot_response.get('code', '')}", color='green')
        print_whole_but_color("Info: ", f"{chatbot_response.get('description', '')}", color='grey')

        options = [
            {'type': 'list',
             'name': 'action',
             'message': 'What would you like to do?',
             'choices': [
                 {'name': 'Copy Code to clipboard', 'value': 'copy'},
                 {'name': 'Retry query', 'value': 'retry'},
                 Separator(),
                 {'name': 'Exit', 'value': 'exit'}
             ]}
        ]

        answers = prompt(options)

        if answers['action'] == 'copy':
            pyperclip.copy(chatbot_response.get('code', ''))
            click.echo("Copied to clipboard.")
            break
        elif answers['action'] == 'retry':
            continue
        elif answers['action'] == 'exit':
            break

    click.echo("Exiting chatbot session.")

if __name__ == '__main__':
    chat()
