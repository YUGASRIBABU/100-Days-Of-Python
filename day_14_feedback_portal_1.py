import re 

def analyze_feedback(review):
    #convert to lowercase for easier maching 
    review_lower = review.lower()

    #Define category patterns
    complaint_pattern = r"\b(damaged|refund|replacement|delay|broken|bad|worst|annoying|support|slow)\b"
    praise_pattern = r"\b(love|awesome|great|excellent|smooth|amazing|fantastic|best)\b"
    feature_pattern = r"\b(add|wish|feature|could|please|update|failed|bug|crush|error|freezes)\b"

    print("\n--- Feedback Intelligence Report ---")
    print(f"Review: \"{review}\"")

    # Check categories
    is_complaint = re.search(complaint_pattern, review_lower, re.IGNORECASE)
    is_praise = re.search(praise_pattern, review_lower, re.IGNORECASE)
    is_feature = re.search(feature_pattern, review_lower, re.IGNORECASE)

    if is_complaint:
        print(f"🔴 Category: Complaint/ Issue (Keyword: {is_complaint.group()})")
    if is_praise:
        print(f"🟢 Category: Postive Praise (Keyword: {is_praise.group()})")
    if is_feature:
        print(f"🔵 Category: Feature Request (Keyword: {is_feature.group()})")

    if not (is_complaint or is_praise or is_feature):
        print("⚪ Category: General Feedback / Neutral")
    print("-" * 38)

#<---UN-INDENT EVERYTHHING FROM HERE DOWN SO IT IS ON THE FAR LEFT --->
print("Welcome to Digital Product Feedback Intelligence!")
while True:
    user_review = input("\nEnter customer feedback (or type 'exit' to quit): ")
    if user_review.lower() == 'exit':
        print("Exiting Feedback Intelligence. Good luck wish your mini-project!")
        break
    analyze_feedback(user_review)