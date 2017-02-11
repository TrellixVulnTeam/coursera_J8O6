from math import ceil, floor
from neural_network.functions import cross_entropy
import random

class Evaluator:
    @staticmethod
    def split_dataset(validation_set_ratio, inputs, targets):
        num_examples = len(inputs)

        train_set_ratio = 1 - validation_set_ratio
        num_train_examples = floor((1 - train_set_ratio) * num_examples)

        shuffled_idxs = random.sample(range(num_examples), num_examples)

        train_idxs = shuffled_idxs[:num_train_examples]
        train_inputs = [inputs[i] for i in train_idxs]
        train_targets = [targets[i] for i in train_idxs]

        validation_idxs = shuffled_idxs[num_train_examples:]
        validation_inputs = [inputs[i] for i in validation_idxs]
        validation_targets = [targets[i] for i in validation_idxs]

        return (
            (train_inputs, train_targets),
            (validation_inputs, validation_targets)
        )

    def __init__(self, neural_network):
        self.nn = neural_network
        self.reset_accumulators()

    def reset_accumulators(self):
        self.loss = 0.0
        self.false_neg = 0
        self.false_pos = 0

    # TODO: This is laziness. I should have a real validation set.
    def run(self, inputs, targets):
        self.reset_accumulators()

        for (input_v, target) in zip(inputs, targets):
            self.run_example(input_v, target)

        misclassification_rate = \
          (self.false_neg + self.false_pos) / len(inputs)

        return (
            self.loss,
            self.false_neg,
            self.false_pos,
            misclassification_rate
        )

    def run_example(self, input_v, target):
        output = self.nn.run(input_v)

        if (target == 1) and (output <= 0.5):
            self.false_neg += 1
        elif (target == 0) and (output >= 0.5):
            self.false_pos += 1

        self.loss += cross_entropy(output, target)
