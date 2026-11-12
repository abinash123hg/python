# Python practice: machine learning, deep learning and DSA

Implementations I maintain as an AI/ML student: classical ML and a first
deep-learning model written from scratch, plus solved data-structure problems.

## Layout

- `machine_learning/` - numpy from scratch: linear regression (gradient
  descent), logistic regression (binary cross-entropy), k-means (k-means++
  seeding with multiple restarts)
- `deep_learning/` - multilayer perceptron with manual backpropagation in
  numpy, and a PyTorch training script for the same kind of task
- `dsa/` - classic interview problems: arrays, strings, linked lists,
  stacks and queues, each with complexity notes
- `tests/` - unittest suite covering every module

## Running

Every module prints a small demo on synthetic data:

```
python -m machine_learning.linear_regression
python -m machine_learning.logistic_regression
python -m machine_learning.kmeans
python -m deep_learning.mlp_numpy
python -m deep_learning.mlp_torch
```

Run the test suite from the repository root:

```
python -m unittest discover -s tests -t .
```

## Requirements

See `requirements.txt` (numpy and torch; the DSA modules and the numpy MLP
need only the standard library plus numpy).
