# clichat

This is a CLI tool for generating shell scripts using OPENAI.

## Installation

Assuming you created a env variable with key named `OPENAI_API_KEY`.
If you don't have a api key [visit here](https://platform.openai.com/account/api-keys) and generate one.

To install ChatGPT-CLI, you'll first need to set up an OpenAI API key. If you don't have one yet, visit the [OpenAI Website](https://platform.openai.com/account/api-keys) to sign up and generate an API key.


Next, add the following line to your `~/.bashrc` or `~/.zshrc` file:

```bash
export OPENAI_API_KEY=<YOUR OPENAI API KEY>

```
Be sure to replace <YOUR OPENAI API KEY> with your actual API key. Then, source the file using:

Lastly source the file using `source ~/.bashrc` or `source ~/.zshrc`


---

You may now install the package using pip:

```bash
$ pip3 install clichat
```

For arch users, this exact package is available on [aur](https://aur.archlinux.org/packages/clichat) by the name clichat
```bash
$ paru clichat
```

## Usage

Once you have installed CLI Chat, you can run it by typing:
```bash
$ clichat
```

This will start the CLI prompt, and you can begin chatting with the AI bot.
