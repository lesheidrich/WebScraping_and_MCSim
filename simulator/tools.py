import math
import random
from typing import List


class GameTools:
    @staticmethod
    def step(threshold: float) -> bool:
        """
        Step function decides outcomes of individual events (e.g.: Jordan making the free-throw).
        :param threshold:
        :return:
        """
        if random.uniform(0, 1) < threshold:
            return True
        return False

    # @staticmethod
    # def sigmoid(x) -> float:
    #     """
    #     Sigmoid function used to increment/decrement play probability.
    #     1 / (1 + e^(-x)), where e is the base of the natural logarithm.
    #     :param x: float x, the input value
    #     :return: result of function as float
    #     """
    #     return 1 / (1 + math.exp(-x))

    @staticmethod
    def weighted_random_sample(population: List, weights: List, k: int, weight_multiplier: float) -> List:
        result = set()

        while len(result) < k:
            w = [math.pow(_, weight_multiplier) for _ in weights]
            i = random.choices(range(len(population)), weights=w)[0]
            if population[i] not in result:
                result.add(population[i])
        return list(result)

