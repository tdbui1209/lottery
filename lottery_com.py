import random

class Lottery :
    """Number-1 legit lotto company."""

    def draw_ticket(self):
        """
        Player takes a ticket with 6 non-duplicates random number
        from 1 to 45.
        """
        ticket = random.choices(range(1, 45), k=6)
        ticket.sort()
        return ticket

    def draw_winning_ticket(self):
        """
        Lotto company draws a ticket with 6 non-duplicates random number
        from 1 to 45.
        """
        ticket = random.choices(range(1, 45), k=6)
        ticket.sort()
        return ticket

    def compare(self, player_ticket, winning_ticket):
        """
        Compare player's ticket with winning ticket.
        """
        match_numbers = []
        for number in player_ticket:
            if number in winning_ticket:
                match_numbers.append(number)
        match_numbers.sort()
        print("Player's ticket:")
        print(player_ticket)
        print()
        print("Winning ticket:")
        print(winning_ticket)
        print()
        print('Match numbers: {0}\n{1}'.format(len(match_numbers),
                                               match_numbers))
