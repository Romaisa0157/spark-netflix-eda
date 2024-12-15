# Netflix Movies and TV Shows EDA using Apache Spark

This project performs **Exploratory Data Analysis (EDA)** on the Netflix Movies and TV Shows dataset using **Apache Spark** in a Dockerized environment.

## Prerequisites
1. **Docker**: Ensure Docker is installed and running on your machine. [Download Docker](https://www.docker.com/products/docker-desktop)
2. **Dataset**: Download the Netflix dataset (`netflix_titles.csv`) from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).
3. Python 3.x (pre-installed in the Docker container).

---

## Project Setup and Execution

Step 1: Pull the Spark Docker Image
Pull the official Spark Docker image for Python:
```bash
docker pull apache/spark-py

Step 2: Start the Docker Container
docker run -it -v /path/to/your/dataset:/data apache/spark-py
Replace /path/to/your/dataset with the path to the directory where your dataset (netflix_titles.csv) is located.

Step 3: Create the EDA Script
Inside the container, create a file named eda_netflix.py in the /data directory.

Step 5: Run the EDA Script
Run the eda_netflix.py script inside the container using Spark.

Results:
The Reuslts can be seen in the "2021538_A03_CE408.pdf" file