# Testing Task (Python)

## Description

This script processes telemetry data from an input file, filters records based on predefined conditions, and saves the matching records to an output file.

A record is considered problematic if:

- `cpu_temp > 85`
- OR `fps_camera < 15`

The filtered records are written to `data/result.txt`.

## Project Structure

```text
.
├── data
│   ├── testData.txt
│   └── result.txt
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or higher

## Run

1. Clone the repository:

```bash
git clone <repository-url>
cd testing-task-py
```

2. Run the script:

```bash
python main.py
```

## Input File

Place the input file at:

```text
data/testData.txt
```

Example:

```text
timestamp,cpu_temp,fps_camera,tracking_confidence,packet_loss
1719321600,62.5,30,0.95,0.0
1719321601,65.4,30,0.94,0.0
1719321602,86.1,14,0.42,1.2
1719321603,88.7,11,0.15,4.5
1719321604,72.1,30,0.88,0.1
```

## Output File

Filtered records are saved to:

```text
data/result.txt
```

## Error Handling

The script handles:

- Missing input file
- Invalid row format
- Invalid numeric values
