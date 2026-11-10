# Computer Vision Mock Exam - 2BI

## Lecture 06 to Lecture 09

This mock exam is intended to **guide your studies on the topics that may be covered in the exam**. Questions may be presented in different formats, including **open-ended questions, multiple-choice questions, true/false statements, algorithm analysis and validation, and code interpretation**, among others.

**This mock exam should not be used as your only study resource.** Its primary purpose is to familiarize you with the **question formats and expected level of reasoning**, rather than to cover all topics and content that may be assessed in the exam.

### Question 01 – Deep Learning and Convolutional Neural Networks (CNNs)

Traditional Machine Learning and Deep Learning approaches differ in how they extract and represent information from images. Convolutional Neural Networks (CNNs) are widely used in Computer Vision because of their ability to learn hierarchical representations directly from image data.

**Considering the fundamental concepts of Deep Learning and CNNs, which of the following statements is CORRECT?**

A) Deep Learning eliminates the need for training data because neural networks can automatically extract discriminative features without supervision or optimization.

B) Unlike traditional approaches that often rely on handcrafted features, CNNs learn convolutional filters during training, enabling the extraction of increasingly complex visual representations.

C) CNNs use convolutional layers primarily for classification, while fully connected layers are responsible for extracting spatial features directly from the original image.

D) Increasing the number of layers in a CNN always improves generalization, since deeper architectures automatically prevent overfitting.

E) Convolutional filters in CNNs are predefined using traditional image processing operators, such as Sobel and Gaussian filters, and remain fixed throughout training.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>

<p><strong>Correct answer: B</strong></p>

<p><strong>Explanation:</strong></p>

<ul>
<li><strong>A — Incorrect:</strong> Deep Learning requires training data and optimization.</li>
<li><strong>B — Correct:</strong> CNNs learn convolutional kernels during training.</li>
<li><strong>C — Incorrect:</strong> Convolutional layers primarily extract spatial features.</li>
<li><strong>D — Incorrect:</strong> Increasing network depth does not guarantee better generalization.</li>
<li><strong>E — Incorrect:</strong> CNN filters are generally learned rather than predefined.</li>
</ul>

</div>
</details>

### Question 02 – Weight Optimization and Backpropagation

In Deep Learning, neural networks learn by iteratively adjusting their parameters to minimize a loss function. In Convolutional Neural Networks (CNNs), this optimization process extends beyond the weights of fully connected layers to include the convolutional kernels responsible for feature extraction.

**Considering the training and optimization processes of neural networks, which of the following statements is CORRECT?**

A) During feedforward propagation, the network updates its weights based on the prediction error, while backpropagation is responsible for generating the final predictions.

B) Backpropagation directly minimizes the loss function by replacing incorrect predictions with their corresponding ground-truth labels, without modifying the network parameters.

C) Gradient descent updates the network weights in the direction of the gradient of the loss function, increasing the error temporarily to improve generalization.

D) Backpropagation computes gradients of the loss function with respect to trainable parameters, allowing an optimization algorithm to update both fully connected weights and convolutional kernels.

E) In CNNs, only the fully connected layers are optimized during training, since convolutional kernels are fixed feature extractors.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>

<p><strong>Correct Answer: D</strong></p>

<p><strong>Explanation:</strong></p>

<ul>
<li><strong>A — Incorrect:</strong> Feedforward propagation computes the network predictions using the current parameters. Backpropagation computes the gradients required for parameter optimization.</li>

<li><strong>B — Incorrect:</strong> Backpropagation applies the chain rule to compute gradients of the loss function with respect to trainable parameters. It does not replace predictions with ground-truth labels.</li>

<li><strong>C — Incorrect:</strong> Gradient descent updates parameters in the opposite direction of the gradient to reduce the loss function locally. Although individual optimization steps do not guarantee a decrease in loss, increasing the error is not its objective.</li>

<li><strong>D — Correct:</strong> Backpropagation computes the gradients of the loss function with respect to trainable parameters. Optimization algorithms, such as SGD and Adam, use these gradients to update the weights. In CNNs, this includes both fully connected weights and convolutional kernels, allowing the network to learn feature extraction and classification jointly.</li>

<li><strong>E — Incorrect:</strong> Convolutional kernels are generally trainable parameters. Unlike handcrafted image descriptors, CNN filters can be optimized through backpropagation to learn representations relevant to the target task.</li>
</ul>

<p><strong>Key Concept:</strong> Feedforward propagation computes predictions, the loss function measures prediction errors, backpropagation computes gradients, and the optimizer updates the trainable parameters.</p>

</div>
</details>

</div>
</details>

### Question 03 – Convolutional Filters and Feature Extraction

Convolutional filters (kernels) are fundamental components of Convolutional Neural Networks (CNNs). They operate on local regions of an input image or feature map, producing new representations that can be progressively refined across multiple convolutional layers.

**Regarding convolutional filters and their role in CNNs, analyze the following statements:**

**01.** Convolutional filters operate on local receptive fields, applying the same set of weights across different spatial positions of the input.

**02.** Each convolutional filter is responsible for extracting exactly one predefined visual pattern, such as a vertical edge, and its weights remain unchanged during training.

**04.** A convolutional layer can learn multiple filters, each producing a corresponding feature map that responds to different patterns in the input.

**08.** Increasing the number of convolutional filters necessarily increases the spatial resolution (height and width) of the output feature maps.

**16.** In a standard convolutional layer, each filter spans all input channels, and its weights are optimized through backpropagation.

**The sum of the CORRECT statements is:**

- a) 05
- b) 13
- c) 17
- d) 21
- e) 29

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: D (21 = 01 + 04 + 16)</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>01 — Correct:</strong> Convolutional filters use local receptive fields and weight sharing. The same kernel weights are applied across different spatial positions, enabling the detection of similar patterns throughout the input.</li>
<li><strong>02 — Incorrect:</strong> Convolutional filters are generally learned during training rather than predefined. Their weights are updated through optimization, allowing them to discover task-relevant visual patterns.</li>
<li><strong>04 — Correct:</strong> A convolutional layer can contain multiple learnable filters. Each filter produces an output feature map, potentially capturing different characteristics such as edges, textures, or more complex patterns.</li>
<li><strong>08 — Incorrect:</strong> The number of filters determines the number of output channels, not the spatial resolution. Output height and width depend on kernel size, stride, padding, and dilation.</li>
<li><strong>16 — Correct:</strong> In standard convolution, each filter spans the full depth of the input tensor. Its trainable weights are updated using gradients computed through backpropagation.</li>
</ul>
<p><strong>Key Concept:</strong> Convolutional filters combine local connectivity, weight sharing, and learnable parameters. Multiple filters allow CNNs to construct increasingly rich feature representations.</p>
</div>
</details>

### Question 04 – The Curse of Dimensionality

In Machine Learning and Computer Vision, increasing the number of features may provide additional information about the input data. However, high-dimensional feature spaces introduce challenges that can negatively affect model training, computational efficiency, and generalization.

**Regarding the Curse of Dimensionality, which of the following statements is CORRECT?**

A) Increasing the number of features consistently improves classification performance because additional dimensions provide more information, regardless of dataset size.

B) As dimensionality increases, the feature space grows exponentially, potentially making data increasingly sparse and requiring more training samples to achieve reliable generalization.

C) Distance-based algorithms become more reliable in high-dimensional spaces because Euclidean distances naturally distinguish similar and dissimilar samples more effectively.

D) The Curse of Dimensionality primarily affects Deep Learning models, since traditional Machine Learning algorithms operate independently of the number of input features.

E) Principal Component Analysis (PCA), feature selection, and autoencoders eliminate the Curse of Dimensionality by guaranteeing that all relevant information is preserved during dimensionality reduction.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: B</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Incorrect:</strong> More features do not necessarily improve classification performance. Irrelevant or redundant features can increase model complexity, introduce noise, and increase the risk of overfitting.</li>
<li><strong>B — Correct:</strong> As the number of dimensions increases, the volume of the feature space grows exponentially when the range of each dimension is fixed. Consequently, data becomes increasingly sparse, and substantially more training samples may be required to adequately represent the feature space and achieve reliable generalization.</li>
<li><strong>C — Incorrect:</strong> In high-dimensional spaces, distances between samples may become less discriminative, making similarity measurements less reliable for algorithms that depend on distance metrics.</li>
<li><strong>D — Incorrect:</strong> The Curse of Dimensionality affects several Machine Learning approaches, particularly those relying on distance metrics, density estimation, or high-dimensional feature representations. It is not exclusive to Deep Learning.</li>
<li><strong>E — Incorrect:</strong> Feature selection, PCA, and autoencoders are techniques used to mitigate dimensionality-related problems. However, dimensionality reduction may discard useful information and does not guarantee improved performance or complete elimination of these challenges.</li>
</ul>
<p><strong>Key Concept:</strong> More features do not always mean better learning. Increasing dimensionality can lead to data sparsity, unreliable distance measurements, higher sample requirements, and overfitting. Dimensionality reduction techniques can mitigate these effects by producing more compact feature representations.</p>
</div>
</details>

### Question 05 – Learning Convolutional Kernels Through Optimization

Traditional Computer Vision approaches frequently rely on handcrafted feature extractors, such as predefined convolutional kernels for edge detection. In contrast, Deep Learning extends the concept of weight optimization to the feature extraction process itself.

**Considering the transition from handcrafted features to learnable convolutional kernels in CNNs, which of the following statements is CORRECT?**

A) In traditional image processing, convolutional kernels are optimized through backpropagation, whereas CNNs use fixed filters to ensure consistent feature extraction.

B) Learning convolutional kernels eliminates the need for classification layers, since each filter directly produces the final class prediction.

C) CNNs extend weight optimization to convolutional kernels, allowing the network to automatically learn feature extractors that minimize a task-specific loss function.

D) Convolutional kernels can only be optimized after all fully connected layers have completed their training, since feature extraction and classification must be learned independently.

E) The optimization of convolutional kernels guarantees that the learned features will generalize to any image dataset, regardless of differences in visual characteristics.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: C</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Incorrect:</strong> Traditional image processing commonly uses predefined filters, such as Sobel or Gaussian kernels. In CNNs, convolutional kernels are generally trainable and optimized through backpropagation.</li>
<li><strong>B — Incorrect:</strong> Convolutional kernels extract feature representations. Classification is typically performed by subsequent layers or a classification head that processes these representations.</li>
<li><strong>C — Correct:</strong> CNNs extend the optimization of neural network weights to convolutional kernels. Through backpropagation and gradient-based optimization, the network learns filters that extract features useful for minimizing the task-specific loss function. This enables feature extraction and classification to be optimized jointly.</li>
<li><strong>D — Incorrect:</strong> Convolutional kernels and fully connected weights can be optimized simultaneously through end-to-end training. Gradients propagate backward through the network, allowing both feature extraction and classification components to learn together.</li>
<li><strong>E — Incorrect:</strong> Learned convolutional features are influenced by the training data and optimization objective. They do not guarantee generalization to different datasets or domains, particularly when significant distribution shifts occur.</li>
</ul>
<p><strong>Key Concept:</strong> The fundamental transition from traditional feature engineering to CNNs is the ability to learn feature extractors directly from data. Instead of manually defining which visual patterns should be detected, CNNs optimize convolutional kernels jointly with the remaining network parameters.</p>
</div>
</details>

### Question 06 – CNN Architecture: Feature Extraction and Classification

Convolutional Neural Networks (CNNs) typically consist of two main stages: **feature extraction** and **classification**. These stages combine different operations to progressively transform raw image data into discriminative representations suitable for prediction.

**Regarding the components and their roles in a CNN architecture, analyze the following statements:**

**01.** Convolutional layers apply learnable kernels to extract spatial features, and stacking multiple convolutional layers enables the network to learn increasingly complex representations.

**02.** Activation functions, such as ReLU, introduce nonlinearity into the network, allowing it to learn more complex mappings than a sequence of linear transformations.

**04.** Pooling layers are primarily responsible for optimizing convolutional kernel weights through backpropagation, rather than modifying the spatial dimensions of feature maps.

**08.** Fully connected layers can use features extracted by convolutional layers to perform classification. Alternatively, these features may be provided to other classifiers, such as Support Vector Machines (SVMs).

**16.** Feature extraction and classification must always be performed by separate models, since convolutional and fully connected layers cannot be trained jointly.

**The sum of the CORRECT statements is:**

- a) 07
- b) 11
- c) 13
- d) 19
- e) 27

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: B (11 = 01 + 02 + 08)</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>01 — Correct:</strong> Convolutional layers use learnable kernels to extract spatial patterns from input data. By stacking multiple convolutional layers, CNNs can progressively learn representations ranging from low-level features, such as edges and textures, to more complex visual structures.</li>
<li><strong>02 — Correct:</strong> ReLU introduces nonlinearity by applying the function f(x) = max(0, x). Without nonlinear activation functions, a sequence of linear layers would be equivalent to a single linear transformation, limiting the network's representational capacity.</li>
<li><strong>04 — Incorrect:</strong> Pooling layers typically aggregate information from local regions, often reducing the spatial dimensions of feature maps. They are not responsible for optimizing convolutional kernel weights, although gradients can propagate through pooling operations during backpropagation.</li>
<li><strong>08 — Correct:</strong> Fully connected layers can transform learned feature representations into class predictions. Alternatively, features extracted by CNNs can be used as input to traditional classifiers, such as SVMs, demonstrating that feature extraction and classification can be implemented using different approaches.</li>
<li><strong>16 — Incorrect:</strong> CNNs commonly support end-to-end training, in which convolutional and fully connected layers are jointly optimized through backpropagation. Separate training is possible but not mandatory.</li>
</ul>
<p><strong>Key Concept:</strong> A typical CNN architecture combines sequential convolutional layers, learnable kernels, nonlinear activation functions, and pooling operations for feature extraction, followed by a classification stage that may use fully connected layers or alternative classifiers such as SVMs.</p>
</div>
</details>

# CNN Applications, Architectures, and Training Strategies (Lecture 07)

This section explores the **architecture, training, and practical applications of Convolutional Neural Networks (CNNs)**. The questions assess your understanding of **convolutional layers, kernel size, stride, padding, pooling operations, activation functions, and classification layers**, including how these components influence feature extraction and network behavior.

The section also covers **training strategies and generalization challenges**, including overfitting, dropout, data augmentation, transfer learning, early stopping, and model checkpoints.

Additionally, questions may address **the evolution of CNN architectures**, including LeNet-5, AlexNet, VGG, ResNet, DenseNet, MobileNet, and EfficientNet, as well as challenges associated with training deep networks, such as vanishing gradients, and techniques used to mitigate them, including ReLU and Batch Normalization.

Questions may involve **architectural interpretation, hyperparameter analysis, computational reasoning, training strategies, and comparisons between CNN architectures**.

### Question 08 – CNN Feature Extraction and Hierarchical Representations

![](./images/2026-11-10-14-18-14-image.png)

In a Convolutional Neural Network (CNN), feature extraction is performed through successive convolutional layers that transform an input image into increasingly abstract representations. Each layer processes the feature maps produced by previous layers, allowing the network to progressively learn relevant visual patterns.

**Regarding feature extraction in CNNs, which of the following statements is CORRECT?**

A) Each convolutional layer independently processes the original input image, since feature maps generated by previous layers cannot be used as inputs to subsequent layers.

B) Convolutional layers progressively extract hierarchical representations, where early layers typically capture simple patterns, such as edges and textures, while deeper layers can learn more complex visual structures.

C) The feature extraction stage always reduces the number of feature maps after each convolutional layer, since deeper layers must represent images using fewer channels.

D) Convolutional layers require handcrafted descriptors to be computed before training, since their kernels cannot learn visual patterns directly from image data.

E) The main objective of feature extraction is to convert the input image directly into class probabilities, without requiring a classification stage.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: B</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Incorrect:</strong> In a sequential CNN, each convolutional layer typically processes the feature maps generated by the preceding layer, allowing representations to become progressively more complex.</li>
<li><strong>B — Correct:</strong> CNNs learn hierarchical representations. Early convolutional layers typically detect low-level features, such as edges and textures, while deeper layers combine these features into increasingly complex patterns and structures.</li>
<li><strong>C — Incorrect:</strong> The number of feature maps is determined by the number of convolutional filters. Deeper layers may increase, decrease, or maintain the number of channels depending on the architecture.</li>
<li><strong>D — Incorrect:</strong> Convolutional kernels are generally learned automatically during training, reducing the need for manually designed feature descriptors.</li>
<li><strong>E — Incorrect:</strong> Feature extraction produces representations that can subsequently be processed by classification layers. Class probabilities are typically generated by the classification stage, often using Softmax.</li>
</ul>
<p><strong>Key Concept:</strong> CNNs perform hierarchical feature extraction through sequential convolutional layers, transforming raw image information into increasingly abstract and discriminative representations.</p>
</div>
</details>

---

### Question 09 – Convolutional Layers and Hyperparameters

![](./images/2026-11-10-14-18-33-image.png)

Convolutional layers use learnable filters to extract spatial information from input images or feature maps. Their behavior is controlled by several hyperparameters, including **kernel size, stride, padding, and number of filters**.

**Regarding these hyperparameters, analyze the following statements:**

**01.** Kernel size determines the spatial dimensions of the local region processed by a convolutional filter.

**02.** Increasing the stride generally reduces the spatial dimensions of the output feature maps, assuming the other convolutional parameters remain unchanged.

**04.** Padding can be used to control the spatial dimensions of the output, including preserving the input height and width under appropriate convolutional settings.

**08.** Increasing the number of convolutional filters directly increases the spatial dimensions (height and width) of the output feature maps.

**16.** The number of filters determines the number of output channels produced by a standard convolutional layer.

**The sum of the CORRECT statements is:**

- a) 07
- b) 15
- c) 19
- d) 23
- e) 31

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: D (23 = 01 + 02 + 04 + 16)</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>01 — Correct:</strong> Kernel size defines the spatial dimensions of the convolutional filter, such as 3×3 or 5×5, determining the local region examined at each spatial position.</li>
<li><strong>02 — Correct:</strong> Stride controls how far the filter moves between consecutive positions. Increasing stride generally produces smaller output feature maps when the other parameters remain fixed.</li>
<li><strong>04 — Correct:</strong> Padding adds values, commonly zeros, around the input boundaries. Appropriate padding can preserve spatial dimensions, such as using a 3×3 kernel with stride 1 and padding 1.</li>
<li><strong>08 — Incorrect:</strong> The number of filters determines the number of output channels, not their spatial dimensions. Output height and width depend on kernel size, stride, padding, and dilation.</li>
<li><strong>16 — Correct:</strong> Each convolutional filter produces one output channel in a standard convolutional layer. Therefore, a layer with 32 filters produces an output tensor with 32 channels.</li>
</ul>
<p><strong>Key Concept:</strong> Kernel size controls the local receptive field, stride controls the spatial step, padding influences boundary handling and output dimensions, and the number of filters determines the output depth.</p>
</div>
</details>

### Question 10 – Pooling Layers in Convolutional Neural Networks

<img title="" src="./images/2026-11-10-14-19-12-image.png" alt="" width="351" data-align="center">

Pooling layers are commonly used in Convolutional Neural Networks (CNNs) to reduce the spatial dimensions of feature maps while retaining relevant information. Two widely used approaches are **Max Pooling** and **Average Pooling**, which aggregate information from local regions using different operations.

**Regarding pooling layers and their role in CNN architectures, which of the following statements is CORRECT?**

A) Max Pooling computes the average activation within each local region, preserving the overall distribution of features, while Average Pooling selects the strongest activation.

B) Pooling layers increase the spatial resolution of feature maps, allowing CNNs to recover fine-grained details lost during convolution.

C) Pooling layers are responsible for learning convolutional filters, since their weights are optimized through backpropagation to identify relevant visual patterns.

D) Max Pooling preserves the strongest activation within each local region, while Average Pooling computes the mean activation. Both operations can reduce spatial dimensions and provide some robustness to small spatial translations.

E) Pooling layers guarantee complete translation invariance, ensuring that the extracted features remain identical regardless of how far an object moves within an image.

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: D</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Incorrect:</strong> The operations are reversed. Max Pooling selects the maximum activation within a local region, while Average Pooling computes the arithmetic mean of the activations.</li>
<li><strong>B — Incorrect:</strong> Pooling layers commonly reduce spatial dimensions rather than increase them. This reduction decreases computational requirements in subsequent layers but may discard spatial details.</li>
<li><strong>C — Incorrect:</strong> Standard Max Pooling and Average Pooling do not contain trainable weights. They apply fixed aggregation operations, although gradients can propagate through them during backpropagation.</li>
<li><strong>D — Correct:</strong> Max Pooling retains the strongest activation in each local region, emphasizing prominent features. Average Pooling computes the mean activation, producing a smoother representation. Both can reduce feature map dimensions and provide limited robustness to small spatial translations.</li>
<li><strong>E — Incorrect:</strong> Pooling can provide some local translation invariance, but it does not guarantee complete invariance. Larger translations or changes in feature positions may still affect the resulting feature maps.</li>
</ul>
<p><strong>Key Concept:</strong> Pooling layers aggregate local information, commonly reducing spatial resolution and computational cost. Max Pooling emphasizes strong activations, whereas Average Pooling preserves average responses. Both may improve robustness to small spatial variations, but can also discard useful spatial information.</p>
</div>
</details>

### Question 11 – CNN Architecture and Feature Extraction

Consider a Convolutional Neural Network (CNN) designed for image classification with the following architecture:

Input Image → Conv2D → ReLU → MaxPooling → Conv2D → ReLU → MaxPooling → Flatten → Fully Connected → Softmax

**Regarding the operations performed by this architecture, analyze the following statements:**

**01.** Convolutional layers use learnable kernels to extract spatial features, while ReLU introduces nonlinearity into the network.

**02.** MaxPooling reduces spatial dimensions by selecting the maximum activation within local regions, potentially discarding some spatial information.

**04.** The second convolutional layer processes feature maps generated by previous layers, allowing the network to learn more complex representations.

**08.** The Flatten operation learns additional convolutional filters to convert spatial features into class probabilities.

**16.** The Softmax function transforms classification scores into a probability distribution over the output classes.

**The sum of the CORRECT statements is:**

- a) 07
- b) 15
- c) 19
- d) 23
- e) 31

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: D (23 = 01 + 02 + 04 + 16)</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>01 — Correct:</strong> Convolutional layers apply learnable kernels to extract spatial patterns, while ReLU introduces nonlinearity, allowing the network to represent more complex relationships.</li>
<li><strong>02 — Correct:</strong> MaxPooling selects the maximum activation within each pooling window. With appropriate stride and window size, it reduces spatial resolution, potentially discarding detailed positional information.</li>
<li><strong>04 — Correct:</strong> Sequential convolutional layers operate on feature maps produced by preceding layers. This allows CNNs to progressively combine simple patterns into more complex representations.</li>
<li><strong>08 — Incorrect:</strong> Flatten is a parameter-free reshaping operation that converts multidimensional feature maps into a one-dimensional vector. It does not learn convolutional filters or directly generate class probabilities.</li>
<li><strong>16 — Correct:</strong> Softmax converts classification scores (logits) into normalized values between 0 and 1 that sum to 1, producing a probability distribution over the classes.</li>
</ul>
<p><strong>Key Concept:</strong> CNN architectures combine convolutional layers for feature extraction, activation functions for nonlinearity, pooling for spatial aggregation, and classification layers for prediction.</p>
</div>
</details>

---

### Question 12 – Convolutional Layers, Pooling, and Output Dimensions

Consider a CNN that receives an RGB image with dimensions **64 × 64 × 3** and applies the following operations sequentially:

1. **Conv2D:** 16 filters, kernel size 3 × 3, stride 1, padding = "same".
2. **MaxPooling2D:** pool size 2 × 2, stride 2.
3. **Conv2D:** 32 filters, kernel size 3 × 3, stride 1, padding = "same".
4. **MaxPooling2D:** pool size 2 × 2, stride 2.

Assume that all operations use standard convolution and pooling without dilation.

**What are the output dimensions after each operation?**

A) 64 × 64 × 16 → 32 × 32 × 16 → 32 × 32 × 32 → 16 × 16 × 32

B) 62 × 62 × 16 → 31 × 31 × 16 → 29 × 29 × 32 → 14 × 14 × 32

C) 64 × 64 × 3 → 32 × 32 × 3 → 32 × 32 × 16 → 16 × 16 × 16

D) 64 × 64 × 16 → 32 × 32 × 8 → 32 × 32 × 32 → 16 × 16 × 16

E) 64 × 64 × 16 → 32 × 32 × 16 → 16 × 16 × 32 → 8 × 8 × 32

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: A</strong></p>
<p><strong>Step-by-Step Explanation:</strong></p>
<ol>
<li><strong>First Conv2D:</strong> The input is 64 × 64 × 3. With kernel size 3 × 3, stride 1, and "same" padding, the spatial dimensions remain unchanged. The 16 filters produce 16 output channels. Output: <strong>64 × 64 × 16</strong>.</li>
<li><strong>First MaxPooling2D:</strong> A 2 × 2 pooling window with stride 2 reduces height and width by a factor of 2, while preserving the number of channels. Output: <strong>32 × 32 × 16</strong>.</li>
<li><strong>Second Conv2D:</strong> The spatial dimensions remain unchanged because of "same" padding and stride 1. The 32 filters produce 32 output channels. Output: <strong>32 × 32 × 32</strong>.</li>
<li><strong>Second MaxPooling2D:</strong> The spatial dimensions are reduced by another factor of 2, while the number of channels remains unchanged. Output: <strong>16 × 16 × 32</strong>.</li>
</ol>
<p><strong>Why the other alternatives are incorrect:</strong></p>
<ul>
<li><strong>B — Incorrect:</strong> The dimensions correspond to convolutions without appropriate padding. The specified "same" padding preserves spatial dimensions for stride 1.</li>
<li><strong>C — Incorrect:</strong> The number of output channels in a standard convolution is determined by the number of filters, not by the original number of input channels.</li>
<li><strong>D — Incorrect:</strong> Standard MaxPooling does not reduce the number of channels. It performs spatial aggregation independently within each channel.</li>
<li><strong>E — Incorrect:</strong> The second convolution has stride 1 and "same" padding, so it does not reduce spatial dimensions from 32 × 32 to 16 × 16.</li>
</ul>
<p><strong>Key Concept:</strong> Convolutional layers control output channels through the number of filters, while kernel size, stride, and padding determine spatial dimensions. Pooling commonly reduces spatial resolution without changing the number of channels.</p>
</div>
</details>

### Question 14 – CNN Architecture Implementation

Consider the Convolutional Neural Network (CNN) architecture illustrated in the figure below.

![](images/2026-11-10-15-38-09-image.png)The architecture receives an RGB image and applies convolutional layers, ReLU activation functions, MaxPooling operations, and fully connected layers to perform image classification.

In TensorFlow/Keras, the configuration of convolutional layers depends on parameters such as the number of filters, kernel size, stride, padding, and activation function.

**Which of the following TensorFlow/Keras implementations CORRECTLY reproduces the illustrated architecture, including the dimensions of the intermediate feature maps?**

Assume that:

- `tensorflow` has been imported as `tf`.
- `C = 3` represents the number of output classes.
- Convolutional layers use 3 × 3 kernels, stride 1, and padding that preserves spatial dimensions.
- MaxPooling uses 2 × 2 windows with stride 2.
- All unspecified parameters use their TensorFlow/Keras default values.

**A)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**B)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(64, (32, 16), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**C)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**D)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(16, (32, 32), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**E)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='64'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**F)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='valid'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: A</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Correct:</strong> The implementation correctly reproduces the illustrated architecture. It receives a 64 × 64 × 3 RGB image, applies a convolution with 16 filters, reduces spatial dimensions through MaxPooling, applies another convolution with 32 filters, performs a second MaxPooling operation, and uses Flatten followed by Dense layers with 128 and 3 neurons.</li>
<li><strong>B — Incorrect:</strong> The first convolution uses 64 filters with a kernel size of 32 × 16. In Conv2D(filters, kernel_size), the first argument specifies the number of output channels, while the second specifies the spatial dimensions of the convolutional kernel. Therefore, the first output would have 64 channels instead of the expected 16.</li>
<li><strong>C — Incorrect:</strong> Both convolutional layers are applied before the pooling operations. Although the final feature map dimensions are 16 × 16 × 32, the intermediate representations do not match the illustrated architecture. The first pooling layer should occur immediately after the convolution with 16 filters.</li>
<li><strong>D — Incorrect:</strong> The first convolution uses a 32 × 32 kernel instead of the specified 3 × 3 kernel. Although same padding preserves the spatial dimensions and the resulting tensor shape matches the figure, the convolutional operation and its number of trainable parameters are different.</li>
<li><strong>E — Incorrect:</strong> The padding argument does not accept '64' as a valid configuration. TensorFlow/Keras Conv2D supports padding values such as 'same' and 'valid'. The value 64 cannot be used to specify the spatial dimensions of the feature maps.</li>
<li><strong>F — Incorrect:</strong> The first convolution uses valid padding, which reduces the spatial dimensions from 64 × 64 to 62 × 62. The subsequent MaxPooling operation produces 31 × 31 × 16 instead of the expected 32 × 32 × 16. Consequently, the remaining feature map dimensions also differ from the illustrated architecture.</li>
</ul>
<p><strong>Expected Output Dimensions:</strong></p>
<ol>
<li>Input: <strong>64 × 64 × 3</strong></li>
<li>Conv2D (16 filters, 3 × 3): <strong>64 × 64 × 16</strong></li>
<li>MaxPooling2D (2 × 2): <strong>32 × 32 × 16</strong></li>
<li>Conv2D (32 filters, 3 × 3): <strong>32 × 32 × 32</strong></li>
<li>MaxPooling2D (2 × 2): <strong>16 × 16 × 32</strong></li>
<li>Flatten: <strong>8,192 features</strong></li>
<li>Dense: <strong>128 neurons</strong></li>
<li>Output: <strong>3 classes (Softmax)</strong></li>
</ol>
<p><strong>Key Concept:</strong> In TensorFlow/Keras, Conv2D(filters, kernel_size) defines the number of output channels and the spatial size of the convolutional kernel, respectively. The spatial dimensions of feature maps depend on kernel size, stride, and padding, while MaxPooling reduces spatial resolution without changing the number of channels. Different layer sequences may produce identical final tensor dimensions without representing the same CNN architecture.</p>
</div>
</details>

### Question 16 – Deep CNN Architecture Implementation

Consider the Convolutional Neural Network (CNN) architecture illustrated in the figure below.

![](./images/2026-11-10-15-18-13-image.png)

The network receives an RGB image of size **128 × 128 × 3** and performs feature extraction using six convolutional layers organized into three blocks, interleaved with MaxPooling operations. The extracted features are subsequently processed by fully connected layers for classification.

**Which of the following TensorFlow/Keras implementations CORRECTLY reproduces the architecture illustrated in the figure, including the number of filters, layer sequence, spatial dimensions, and classification stage?**

Assume that:

- `tensorflow` has been imported as `tf`.
- `C` represents the number of output classes.
- Convolutional layers use 3 × 3 kernels, stride 1, `padding='same'`, and ReLU activation.
- MaxPooling operations use 2 × 2 windows with stride 2.
- All unspecified parameters use their TensorFlow/Keras default values.

**A)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32768, activation='relu'),
    tf.keras.layers.Dense(C, activation='sigmoid')
])
```

**B)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**C)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(C, activation='sigmoid')
])
```

**D)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 64, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 128, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**E)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

**F)**

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128, 128, 3)),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    tf.keras.layers.MaxPooling2D(2),
    tf.keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(C, activation='softmax')
])
```

<details>
<summary><strong>▶ Show answer</strong></summary>
<div>
<p><strong>Correct Answer: E</strong></p>
<p><strong>Explanation:</strong></p>
<ul>
<li><strong>A — Incorrect:</strong> The fully connected layer contains 32,768 neurons instead of 256. The value 32,768 represents the number of features produced by Flatten, not the number of neurons required in the Dense layer. Additionally, the output layer uses sigmoid instead of Softmax.</li>
<li><strong>B — Incorrect:</strong> The first MaxPooling operation occurs immediately after the first convolutional layer instead of after two consecutive convolutions. This changes the sequence of feature extraction and spatial downsampling.</li>
<li><strong>C — Incorrect:</strong> Flatten is applied before the final MaxPooling operation. Flatten converts the feature maps into a one-dimensional feature vector, making the resulting tensor incompatible with MaxPooling2D. Additionally, the output layer uses sigmoid instead of Softmax.</li>
<li><strong>D — Incorrect:</strong> The final two convolutional layers use Conv2D(32, 64) and Conv2D(32, 128). In TensorFlow/Keras, the first argument specifies the number of filters, while the second specifies the kernel size. These layers produce 32 output channels with large convolutional kernels instead of 64 and 128 output channels with 3 × 3 kernels.</li>
<li><strong>E — Correct:</strong> The implementation contains six convolutional layers organized into three blocks: (16, 16), (32, 32), and (64, 128) filters. Each block is followed by MaxPooling. Flatten produces 32,768 features, followed by Dense(256) and Softmax classification.</li>
<li><strong>F — Incorrect:</strong> The final MaxPooling operation is placed between the fifth and sixth convolutional layers instead of after both convolutions. Although the final tensor dimensions may match, the order of operations differs from the illustrated architecture.</li>
</ul>
<p><strong>Expected Output Dimensions:</strong></p>
<ol>
<li>Input: <strong>128 × 128 × 3</strong></li>
<li>Conv2D (16 filters): <strong>128 × 128 × 16</strong></li>
<li>Conv2D (16 filters): <strong>128 × 128 × 16</strong></li>
<li>MaxPooling2D: <strong>64 × 64 × 16</strong></li>
<li>Conv2D (32 filters): <strong>64 × 64 × 32</strong></li>
<li>Conv2D (32 filters): <strong>64 × 64 × 32</strong></li>
<li>MaxPooling2D: <strong>32 × 32 × 32</strong></li>
<li>Conv2D (64 filters): <strong>32 × 32 × 64</strong></li>
<li>Conv2D (128 filters): <strong>32 × 32 × 128</strong></li>
<li>MaxPooling2D: <strong>16 × 16 × 128</strong></li>
<li>Flatten: <strong>32,768 features</strong></li>
<li>Dense: <strong>256 neurons</strong></li>
<li>Output: <strong>C classes (Softmax)</strong></li>
</ol>
<p><strong>Key Concept:</strong> Correctly interpreting CNN architectures requires distinguishing the number of convolutional filters from kernel dimensions, understanding the order of convolutional and pooling operations, and recognizing that Flatten converts feature maps into a vector without introducing trainable parameters. Different sequences of operations may produce identical final tensor dimensions while implementing different architectures.</p>
</div>
</details>

![](./images/2026-11-10-15-23-23-image.png)
