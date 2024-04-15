
"""
Discussion: Why are the epochs doubled in sequential training?

Each epoch only contains summer or autumn data and is only of size $K$, whereas interspersed training epochs contain $2K$ data points. In order to expose both models to the same amount of data, the number of epochs must be doubled.

Which mode worked better and why?

Interspersed training works better. In sequential training, the model is constantly shifting from learning one type of relation to another (which is basically what we have tried during the first section of the tutorial); still, here sequential joint training helps because we change data source for each epoch which makes the model still remember both data distributions. With interspersed this ability to remember both distributions is even stronger as both are represented in each epoch.
""";