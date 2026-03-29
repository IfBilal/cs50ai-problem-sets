Project 5: Traffic
Background
The goal of this project was to build an AI using TensorFlow to classify images of road signs based on the GTSRB dataset. With 43 different categories, the model needed to be complex enough to distinguish between subtle differences (like speed limit numbers) while remaining general enough to handle blurry or off-center photos.

My Observations & Experiments
Attempt 1: The Shallow Model
Architecture: 1 Conv2D layer (32 filters, 3x3), 1 MaxPooling layer, Flatten, 1 Dense layer (128 units), and Dropout (0.5).

Result: Accuracy ~5.7%, Loss ~3.5.

Observation: The model completely failed to learn. An accuracy of 5% is only slightly better than random guessing (1/43). I concluded that a single convolutional layer was not enough to extract the high-level features needed to identify 43 different types of signs.

Attempt 2: The Double-Stack Model (The Breakthrough)
Architecture: * Conv2D (32 filters, 3x3) + MaxPooling

Conv2D (64 filters, 3x3) + MaxPooling

Flatten + Dense (128 units) + Dropout (0.5)

Result: Accuracy 95.82%, Loss 0.15.

Observation: This was the "sweet spot." By adding a second convolutional layer with more filters (64), the AI was able to develop a hierarchy of features. The first layer likely identified edges and colors, while the second layer identified complex shapes like circles and triangles. This moved the accuracy from 5% to over 95%.

Attempt 3: The Randomness Factor
Observation: During testing, I noticed that even with the "Double-Stack" code, the model occasionally failed to start (plateauing at 5% again).

Conclusion: This highlighted the role of Stochastic Gradient Descent and weight initialization. Sometimes the random starting weights lead the model into a local minimum. Re-running the training allowed the model to find a better path to the global minimum.

Final Model Design
The final model uses two stages of convolution and pooling to maximize feature extraction. I kept the Dropout at 0.5 to ensure the model didn't overfit (memorize) the training data, which was confirmed by the high validation accuracy (95.82%) compared to the training accuracy.
