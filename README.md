# ASPJinjaObfuscator

![ninja](img/ninja.webp)

A heavily obfuscated `Windows` based `ASP` web shell generation tool utilizing the power of Python's `Jinja2` templating engine. Generates a web shell with randomized variable/function names and HTML strings of random lengths, XOR encrypted strings with base64 encoding, and a random encryption key per generation. Tested as bypassing the latest version of `Windows Defender` as of `04/22/2024` with `Cloud-delivered protection` enabled.

## Installation

Make sure that you have `Python3` with the `Jinja2` & `pyperclip` `pip` packages installed. Install the `pip` requirements with the following command:

```bash
pip3 install -r requirements.txt
```

## Usage

Run the program with no commandline arguments from the directory where the script and the `Jinja2` template is installed, it will then generate a randomized web shell named `output.asp`. The program will ask you what commands you would like to run, type them into the program in plaintext and it will give you the encrypted versions. It will automatically copy them to the clipboard, paste these encrypted commands into the web shell, it will decrypt and then run them. That's it, time to **PROFIT**!