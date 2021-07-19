# Lottery Simulator

A simple lottery simulator.
<hr>
Initialize the Lottery class:<br>
<code>
\>>> vietlott = Lottery()
</code>

To draw a ticket:<br>
<pre>
>>> player_ticket = vietlott.draw_ticket()
>>> print(player_ticket)
[8, 14, 20, 23, 25, 45]
</pre>

Draws winning ticket:<br>
<pre>
>>> winning_ticket = vietlott.draw_winning_ticket()
>>> print(winning_ticket)
[2, 8, 14, 15, 26, 44]
</pre>

Compare player's ticket with winning ticket:
<pre>
>>> vietlott.compare(player_ticket, winning_ticket
Player's ticket:
[8, 14, 20, 23, 25, 45]

Winning ticket:
[2, 8, 14, 15, 26, 44]

Match numbers: 2
[8, 14]
</pre>
