from pathlib import Path

file_path = Path("data/testData.txt")
output_path = Path("data/result.txt")
data = []

if not file_path.exists():
    raise FileNotFoundError("File not found")

with file_path.open() as file:
    for line in file:
        parts = line.strip().split(",")

        if parts[0] == "timestamp":
            continue

        if len(parts) != 5:
            continue

        try:
            item = [
                int(parts[0]),    # timestamp
                float(parts[1]),  # cpu_temp
                int(parts[2]),    # fps_camera
                float(parts[3]),  # tracking_confidence
                float(parts[4])   # packet_loss
            ]
        except ValueError:
            continue

        data.append(item)

with output_path.open("w") as out:
    for item in data:
        if item[1] > 85 or item[2] < 15:
            row = ",".join(map(str, item))
            print(row)
            out.write(row + "\n")



