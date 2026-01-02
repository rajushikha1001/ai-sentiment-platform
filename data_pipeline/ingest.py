import pandas as pd

def load_data():
    data = {
        "text": [
            "I love DevOps!",
            "AI is overrated",
            "Cloud engineering is awesome",
            "This product is terrible"
        ],
        "label": [1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    df.to_csv("data_pipeline/dataset.csv", index=False)
    print("dataset.csv created")

if __name__ == "__main__":
    load_data()
