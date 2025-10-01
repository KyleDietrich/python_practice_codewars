#!/usr/bin/env python3

def calculate_damage(your_type, opponent_type, attack, defense):
    """
    Calculate the damage dealt in a Pokémon battle based on type advantages and attack/defense stats.

    :param your_type: str - The type of your Pokémon (e.g., 'Fire', 'Water')
    :param opponent_type: str - The type of the opponent's Pokémon (e.g., 'Grass', 'Electric')
    :param attack: int - The attack stat of your Pokémon
    :param defense: int - The defense stat of the opponent's Pokémon
    :return: float - The calculated damage
    """
    type_effectiveness = {
        ('fire', 'grass'): 2.0,
        ('grass', 'fire'): 0.5,
        ('fire', 'water'): 0.5,
        ('water', 'fire'): 2.0,
        ('fire', 'electric'): 1.0,
        ('electric', 'fire'): 1.0,
        ('water', 'grass'): 0.5,
        ('grass', 'water'): 2.0,
        ('water', 'electric'): 0.5,
        ('electric', 'water'): 2.0,
        ('grass', 'electric'): 1.0,
        ('electric', 'grass'): 1.0,
    }

    if your_type.lower() == opponent_type.lower():
        effectiveness = 1.0
    else:
        effectiveness = type_effectiveness.get(
            (your_type.lower(), opponent_type.lower()), 1.0
        )

    damage = 50 * (attack / defense) * effectiveness
    return damage




        