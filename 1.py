# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

# List of keywords to highlight
keywords = ["good", "excellent", "bad", "poor", "average"]

# List of positive and negative words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Task 1: Highlight Keywords
def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        modified_review = review
        for keyword in keywords:
            modified_review = modified_review.replace(keyword, keyword.upper())
        highlighted_reviews.append(modified_review)
    return highlighted_reviews

# Task 2: Tally Sentiments
def tally_sentiments(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    for review in reviews:
        for word in positive_words:
            positive_count += review.lower().split().count(word)
        for word in negative_words:
            negative_count += review.lower().split().count(word)
    return positive_count, negative_count

# Task 3: Review Summary
def summarize_reviews(reviews, length=30):
    summaries = []
    for review in reviews:
        if len(review) > length:
            cutoff = review.rfind(' ', 0, length)
            if cutoff == -1:
                cutoff = length
            summary = review[:cutoff].strip() + '...'
        else:
            summary = review
        summaries.append(summary)
    return summaries

# Run tasks
highlighted_reviews = highlight_keywords(reviews, keywords)
for review in highlighted_reviews:
    print(review)

positive_count, negative_count = tally_sentiments(reviews, positive_words, negative_words)
print(f"Total positive words: {positive_count}")
print(f"Total negative words: {negative_count}")

summaries = summarize_reviews(reviews)
for summary in summaries:
    print(summary)
