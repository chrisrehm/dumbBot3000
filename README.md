# dumbBot3000

A painfully simple, always broken, messily-coded IRC quotes bot made for a small private IRC channel. The goals of this bot:

1) To be simple. So simple it hurts.
2) To have very readable code that is easy for even absolute beginners to grasp. Being easy to understand and working reliably is more important than being efficient with this.
3) To annoy pretenious programmers.

This bot currently relies on irc 16.2 library (https://pypi.python.org/pypi/irc). "pip install irc" that bad-boy.

Commands for this bot (most broken / not yet implemented):

".quote" - gives a random quote.<br>
".quote 14" - gives the 14th quote.<br>
".quote chris" - gives a random quote matching search string "chris"<br>
".findall chris" - lists the quote number for all quotes containing "chris"<br>
".addquote <Nick> will be added" - add quote to quotes file (quotes.txt)<br>
".lastquote" - gives the last quote added to the file.<br>

<b>Trying to run this is probably a bad idea. It's always broken. Run away.</b>
