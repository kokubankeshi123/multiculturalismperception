text.raw <- readLines("aus_hansard.txt")
text <- as.vector(paste(text.raw, collapse = " "))

library(tm)
text_source <- VectorSource(text)
corpus <- Corpus(text_source)

corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, stripWhitespace)
corpus <- tm_map(corpus, removeWords, c(stopwords("english"), "i", "the"))

tdm <- TermDocumentMatrix(corpus, control = list(wordLengths = c(1, Inf)))

freq.terms <- findFreqTerms(tdm, lowfreq = 80)
freq.terms
term.freq <- rowSums(as.matrix(tdm))
term.freq <- subset(term.freq, term.freq >= 80)
df <- data.frame(term = names(term.freq), freq = term.freq)
df
library(ggplot2)
ggplot(df, aes(x = term, y = freq)) + geom_bar(stat = "identity") + 
        xlab("Terms") + ylab("Count") + coord_flip()


