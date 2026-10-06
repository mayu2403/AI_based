import streamlit as st
from textblob import TextBlob

# Page title
st.set_page_config(page_title="Product Review Sentiment Analysis")

st.title("🛍️ Product Review Sentiment Analysis")
st.write("Analyze the sentiment of a product review using NLP.")

# User input
review = st.text_area(
    "Enter your product review:",
    placeholder="Example: This product is very good and I really like it!"
)

# Analyze button
if st.button("Analyze Sentiment"):

    if review.strip() == "":
        st.warning("Please enter a product review.")

    else:
        # NLP sentiment analysis
        analysis = TextBlob(review)
        polarity = analysis.sentiment.polarity

        # Classify sentiment
        if polarity > 0:
            sentiment = "Positive 😊"
        elif polarity < 0:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        # Display results
        st.subheader("Analysis Result")
        st.write("**Review:**", review)
        st.write("**Sentiment:**", sentiment)
        st.write("**Polarity Score:**", round(polarity, 2))

        # Explanation
        if polarity > 0:
            st.success("The review expresses a positive opinion.")
        elif polarity < 0:
            st.error("The review expresses a negative opinion.")
        else:
            st.info("The review expresses a neutral opinion.")
            