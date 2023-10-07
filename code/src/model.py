from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


class ClusteringModel:
    """Class responsible for creating student clusters."""

    def __init__(
        self,
        k: int = None,
        max_iter: int = 300,
        n_init: int = 10,
        random_state=1234,
        init="k-means++",
    ) -> None:
        self.k = k
        self.max_iter = max_iter
        self.n_init = n_init
        self.random_state = random_state
        self.init = init
        self.wcss = []

    def build_model(self, k: int = None):
        return KMeans(
            n_clusters=self.k if k is None else k,
            init=self.init,
            max_iter=self.max_iter,
            n_init=self.n_init,
            random_state=self.random_state,
        )

    def train_model(self, data, optimal_k: int):
        kmeans = self.build_model(k=optimal_k)
        kmeans.fit(data)
        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_
        return labels, centroids

    def elbow_method_k(self, data):
        # Calculate the Within-Cluster-Sum-of-Squares (WCSS) for different values of k
        wcss = []
        for k in range(1, 20):
            kmeans = KMeans(
                n_clusters=k, init="k-means++", max_iter=300, n_init=10, random_state=0
            )
            kmeans.fit(data)
            wcss.append(kmeans.inertia_)  # Inertia is the WCSS for that model

        # Plot the elbow method curve
        plt.figure(figsize=(8, 6))
        plt.plot(range(1, 20), wcss, marker="o", linestyle="--")
        plt.title("Elbow Method for Optimal k")
        plt.xlabel("Number of Clusters (k)")
        plt.ylabel("WCSS")
        plt.grid()
        plt.show()
