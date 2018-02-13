PLAY_LEARNED_AI = False

# Network Parameters
NUM_HIDDEN_UNITS = 32

# Training Parameters
BATCHES_PER_LOG = 100
CHECKPOINT_FILENAME = "checkpoints/default.checkpt"
LEARNING_RATE = 0.01
MEMORY_LEN = 1_000_000
MINIBATCH_SIZE = 32
NUM_BATCHES_PER_EPOCH = 50000
NUM_EPOCHS = 100

# Evaluation Parameters
NUM_EPOCHS_PER_EVAL = 1
NUM_POINTS_PER_EVALUATION = 200
POINTS_PER_LOG = 100

# Game Params
NUM_ACTIONS = 2 # Can move up or down.
NUM_STATE_DIMENSIONS = 6 # 2x positions of paddle; pos and vel of ball

# Exploration Params
EXPLORATION_START_RATE = 0.90
EXPLORATION_DECAY_RATE = 1e-3
EXPLORATION_RATE_MIN = 0.01
REWARD_DECAY_START = 0.0
REWARD_DECAY_GROWTH_FACTOR = 0.00
REWARD_DECAY_MAX = 0.0

TRAINING_MODE = True
CHOOSE_BEST_ALWAYS = False
CHOOSE_BEST_STOCHASTIC_RATIO = 1.0
TRAINING_MODE_NO_BOUNCES = False
REWARD_TYPE = "IDEAL_ANTICIPATION_REWARD"
REWARD_PROBABILITY = 1.0
REWARD_SCALING_FACTOR = 100
SCALE_REWARD_BY_DISTANCE_TO_PADDLE = 1.0
#CRITICAL_ZONE_WIDTH = 0.2
#CRITICAL_ZONE_BONUS_FACTOR = 100
REWARD_BOUNCES_FACTOR = 10000
# Don't htink this should matter...
DISTANCE_ERROR_POWER = 1.0
