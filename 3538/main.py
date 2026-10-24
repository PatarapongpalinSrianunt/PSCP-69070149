"""[LEARNING LOGS] B - Fully pair?"""
def main():
    """[LEARNING LOGS] B - Fully pair?"""
    text = input().strip()
    if not text:
        return
    counts = {}
    seen = []
    for char in text:
        if char not in counts:
            counts[char] = 0
            seen.append(char)
        counts[char] += 1

    unpaired = []
    for char in seen:
        if counts[char] % 2:
            unpaired.append(char)

    if unpaired:
        print("".join(unpaired))
    else:
        print("fully paired")

main()
