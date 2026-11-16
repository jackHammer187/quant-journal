messy_tickers = "  es, NQ ,gc , mes "
splits = messy_tickers.split(",")
print(splits)

clean = []
for s in splits:
    clean.append(s.strip().upper())
print(clean)

price = [7300.50, 28000.75, 3800.25, 7300.50]
change = [0.0042, 0.0072, 0.0014, 0.0042]

for t, p, ch in zip(clean, price, change):
    print(f"{t} closed at ${p:.2f} ({ch:.2%})" )

filename = "es_daily.csv" 
if not filename.endswith(".csv"):
    print("none here bro")
else:
    print(f"'{filename}' is a valid name.")