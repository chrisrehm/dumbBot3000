#! /usr/bin/env python

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import time
import random

def get_random_quote():
   lines = open("quotes.txt", "r").read().splitlines()
   return random.choice(lines)

def get_quote_by_number(num):
    quote_file = open("quotes.txt", "r")
    lines = quote_file.readlines()
    quote_file.close()
    num = int(abs(num))
    if num < len(lines):
        return "(Quote: " + str(num) + ") " + lines[num]
    else:
        return "Ernt. That quote does not exist." 

def get_last_quote():
    quote_file = open("quotes.txt", "r")
    lastline = quote_file.readlines()
    quote_file.close()
    return "(Last Quote #" + str(len(lastline)) + ") " + lastline[-1]

def count_matching_quotes(searchstr):
    matching_quotes_list = []
    quote_num = 0
    quote_file = open("quotes.txt", "r")
    lines = quote_file.readlines()
    for line in lines:
        if line.strip().lower().find(searchstr.lower()) != -1:
            matching_quotes_list.append(quote_num)
        quote_num = quote_num + 1
    quote_file.close()
    return "Found " + str(len(matching_quotes_list)) + " matching " + searchstr + ": " + str(matching_quotes_list)

def get_random_matching_quote(searchstr):
    matching_quotes_list = []
    quote_num = 0
    quote_file = open("quotes.txt", "r")
    lines = quote_file.readlines()
    for line in lines:
        if line.strip().lower().find(searchstr.lower()) != -1:
            matching_quotes_list.append("(Quote #" + str(quote_num) + ") " + line)
        quote_num = quote_num + 1
    if not matching_quotes_list:
        return "Ernt. No quotes matching: " + searchstr
    else:
        return random.choice(matching_quotes_list)

def add_quote(quote):
    try:
       quote_file = open("quotes.txt", "a")
       quote_file.write(quote + "\n")
       quote_file.close()
       return "Quote added to storage file."
    except IOError:
        return "Ernt. Something went wrong adding quote to storage file."


class dumbBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        user = e.source
        channel = e.target
        message = str(e.arguments[0]).strip() # always a list with one element
        self.do_command(e, message)

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection
        get_bot_command = cmd.split(' ')
        actual_cmd = get_bot_command[0]
        string_without_command = cmd.partition(' ')[2]

        if actual_cmd == ".lastquote":
           self.connection.privmsg(self.channel, get_last_quote().strip())
        elif actual_cmd == ".findall":
            self.connection.privmsg(self.channel, count_matching_quotes(string_without_command))

def main():
    server = "irc.ircserver.net"
    port = 6667
    channel = "#nope"
    nickname = "dumbBot3000"
    bot = dumbBot(channel, nickname, server, port)
    bot.start()

if __name__ == "__main__":
    main()