from collections import defaultdict
import math

# Training data
reviews = {
    'A': ('fun, couple, love, love', 'comedy'),
    'B': ('fast, furious, shoot', 'action'),
    'C': ('couple, fly, fast, fun, fun', 'comedy'),
    'D': ('furious, shoot, shoot, fun', 'action'),
    'E': ('fly, fast, shoot, love', 'action')
}

D = 'fast couple shoot fly'

# Vocabulary from the training data
vocabulary = set()
class_word_counts = defaultdict(lambda: defaultdict(int))
class_counts = defaultdict(int)

# Process training data
for review, label in reviews.values():
    words = review.split(', ')
    class_counts[label] += 1
    for word in words:
        vocabulary.add(word)
        class_word_counts[label][word] += 1

# Total number of words in each class
total_words_in_class = {label: sum(word_counts.values()) for label, word_counts in class_word_counts.items()}

# Add-1 smoothing
def word_prob(word, label):
    return (class_word_counts[label][word] + 1) / (total_words_in_class[label] + len(vocabulary))

# Calculate probabilities for the new document
def class_probabilities(doc):
    words = doc.split()
    probabilities = {}
    for label in class_counts:
        log_prob = math.log(class_counts[label] / sum(class_counts.values()))
        for word in words:
            log_prob += math.log(word_prob(word, label))
        probabilities[label] = log_prob
    return probabilities

# Compute the most likely class
probabilities = class_probabilities(D)
most_likely_class = max(probabilities, key=probabilities.get)

print(f"The most likely class for document D is: {most_likely_class}")
