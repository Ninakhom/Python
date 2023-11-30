import random

class UnoGame:
    def __init__(self, players):
        self.players = players
        self.current_player = 0
        self.deck = self.create_deck()
        self.current_card = self.draw_card()
        self.direction = 1  # 1 for clockwise, -1 for counterclockwise

    def create_deck(self):
        colors = ['Red', 'Green', 'Blue', 'Yellow']
        values = [str(i) for i in range(10)] + ['Skip', 'Reverse', 'Draw Two']
        wild_cards = ['Wild', 'Wild Draw Four']

        deck = [(color, value) for color in colors for value in values]
        deck += [(color, value) for color in colors for value in values]
        deck += [(color, value) for color in colors for value in values]
        deck += [(color, value) for color in colors for value in values]
        deck += [(color, wild) for color in colors for wild in wild_cards]
        deck += [(wild, wild) for wild in wild_cards]

        random.shuffle(deck)
        return deck

    def draw_card(self):
        return self.deck.pop()

    def next_player(self):
        self.current_player = (self.current_player + self.direction) % len(self.players)

    def play(self, card):
        if self.is_valid_move(card):
            print(f"{self.players[self.current_player]} plays {card[0]} {card[1]}")
            self.current_card = card
            self.next_player()
        else:
            print(f"Invalid move! Try again.")

    def is_valid_move(self, card):
        return card[0] == self.current_card[0] or card[1] == self.current_card[1]

    def display_state(self):
        print(f"Current card: {self.current_card[0]} {self.current_card[1]}")
        print(f"Next player: {self.players[self.current_player]}")

    def run(self):
        while True:
            self.display_state()
            current_player_input = input(f"{self.players[self.current_player]}, enter your move (color value): ")
            if current_player_input.lower() == 'quit':
                print("Quitting the game.")
                break
            try:
                color, value = current_player_input.split()
                card = (color, value)
                self.play(card)
            except ValueError:
                print("Invalid input. Please enter a valid move (color value) or 'quit' to end the game.")


if __name__ == "__main__":
    player_names = input("Enter player names separated by commas: ").split(',')
    game = UnoGame(player_names)
    game.run()
