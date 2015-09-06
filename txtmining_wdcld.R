text.raw <- readLines("canall_hansard.txt")
text <- as.vector(paste(text.raw, collapse = " "))

library(tm)
text_source <- VectorSource(text)
corpus <- Corpus(text_source)

corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, removeWords, stopwords("english"))

dtm <- DocumentTermMatrix(corpus)
dtm2 <- as.matrix(dtm)

freq <- colSums(dtm2)
freq <- sort(freq, decreasing = TRUE)
top50 <- head(freq, 50)
top50

library(wordcloud)
words <- names(freq)
wordcloud(words[1:50], freq[1:50])
