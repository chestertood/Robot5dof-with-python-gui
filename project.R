library(data.table)
library(dplyr)

Gov_mortage <- fread("Government_Mortage.csv")

# Record with loan amount 114
# With country code 60
Answer <- Gov_mortage


df <- iris
x <- df[, c("Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width")]
y <- df["Species"]
# stats::kmeans()
print(x)


kmeans_result <- stats::kmeans(x, centers = 3)
print(kmeans_result)

# plot(x,
#     col = kmeans_result$cluster, pch = 19,
#     main = "K-means Clustering of Iris Dataset"
# )
# points(kmeans_result$centers, col = 1:3, pch = 8, cex = 2)


ks <- 1:5
tot_within_ss <- sapply(ks, function(k) {
    cl <- kmeans(x, k, nstart = 10)
    cl$tot.withinss
})
# plot(ks, tot_within_ss, type = "b")


tr <- sample(150, 50)
nw <- sample(150, 50)
library("class")
knnres <- knn(df[tr, -5], df[nw, -5], df$Species[tr])
print(knnres)

print(table(knnres, df$Species[nw]))
print(tr)
