"""
Module: tools.py

This module provides utility functions for game-related calculations and operations.

Classes:
    - GameTools: Utility class for game-related functions.
"""

import math
import random
from typing import List


class GameTools:
    """
    Utility class for game-related functions.

    This class provides static methods for performing various game-related calculations and operations.

    Static Methods:
        - step: Decides outcomes of individual events based on a threshold.
        - weighted_random_sample: Selects a random sample from a list using weighted probabilities.

    Example:
        To use the step method to determine if a player makes a free-throw:
        FTM = 0.75 (average of free-throws made)
        result = GameTools.step(threshold)
        if result:
            print("Free-throw successful!")
        else:
            print("Free-throw missed.")

        To use the weighted_random_sample method to randomly select players based on their weights:
        players = [...]  # List of Player objects
        weights = [...]  # List of weights corresponding to players
        k = 3  # Number of players to sample
        sample = GameTools.weighted_random_sample(players, weights, k, 1.5)
    """
    @staticmethod
    def step(threshold: float) -> bool:
        """
        Step function decides outcomes of individual events (e.g.: Jordan making the free-throw).
        :param threshold: float of avg stat to use as threshold
        :return: True if random below threshold
        """
        if random.uniform(0, 1) < threshold:
            return True
        return False

    @staticmethod
    def weighted_random_sample(population: List, weights: List, k: int, weight_multiplier: float) -> List:
        """
        Selects a random sample from a list using weighted probabilities.
        :param population: list to choose from
        :param weights: list of weights
        :param k: int of number of elements to sample
        :param weight_multiplier: float multiplier to adjust influence of weights
        :return: random sample list
        """
        result = set()

        while len(result) < k:
            w = [math.pow(_, weight_multiplier) for _ in weights]
            i = random.choices(range(len(population)), weights=w)[0]
            if population[i] not in result:
                result.add(population[i])
        return list(result)
