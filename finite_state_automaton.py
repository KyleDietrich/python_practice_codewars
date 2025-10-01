#!/usr/bin/env python3

# Define a State class to represent each state in the automaton
class State:
    def __init__(self, name, is_accept=False):
        self.name = name
        self.is_accept = is_accept
        self.transitions = {}  # Dictionary: input_symbol -> next_state

    def add_transition(self, symbol, next_state):
        self.transitions[symbol] = next_state

    def next(self, symbol):
        # Return the next state for the given symbol
        return self.transitions.get(symbol, self)

class Automaton(object):
    def __init__(self):
        # Create the three states: q1 (start), q2 (accept), q3
        self.q1 = State('q1')
        self.q2 = State('q2', is_accept=True)
        self.q3 = State('q3')

        # Set up transitions according to the problem description
        self.q1.add_transition("0", self.q1)
        self.q1.add_transition("1", self.q2)

        self.q2.add_transition("0", self.q3)
        self.q2.add_transition("1", self.q2)

        self.q3.add_transition("0", self.q2)
        self.q3.add_transition("1", self.q2)

        # Start state is q1
        self.start_state = self.q1

    def read_commands(self, commands):
        """
        Process a list of input symbols and return True if the automaton
        ends in the accept state (q2), otherwise False.
        """
        current_state = self.start_state
        for symbol in commands:
            current_state = current_state.next(symbol)
        return current_state.is_accept

# Set up the automaton instance with the required states and transitions
my_automaton = Automaton()

# Example usage:
# result = my_automaton.read_commands(["1", "0", "0", "1", "0"])
# print(result)  # Output: False