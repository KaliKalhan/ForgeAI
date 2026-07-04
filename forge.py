from core.loader import load_text
from core.analyzer import analyze

text = load_text("sources/sample.txt")

stats = analyze(text)

print("=" * 40)
print("ForgeAI v0.1")
print("=" * 40)

print(text)

print("\nStatistics\n")

for key, value in stats.items():
    print(f"{key.capitalize():12}: {value}")
