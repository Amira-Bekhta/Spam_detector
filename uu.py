from src.bow_model import vectorize
import pandas as pd

df = {
    "Hey Kevin, I hope you are doing well",
    "Grand offer !! [Free houses in the richeest place ever] keanu reeves is the neighbour, send us your ID!!!"
}

df = pd.DataFrame(df)

df = vectorize(df)

print(df)