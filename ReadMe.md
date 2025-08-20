# Console Numberal System Converter

A console application for converting numbers between numeral systems (from base **2** to **36**).
Supports **integer and fractional numbers**, including **negative values**.
All calculations are based on 'fractions.Fraction', ensuring **exact results** without floating-point rounding errors.

---

## Features
- Convert numbers from one numeral system to another.
- Supports bases from **2 to 36**.
- Works with fractional numbers (up to **12 digits after the point**).
- Handles negative numbers.
- Input validation included.
- Supports both ',' and '.' as decimal separators.

---

## Installation and run

Clone the projects and go to the foldera:

```bash
git clone https://github.com/msbndn/number-converter.git
cd number-converter
```

Run the programm:

```bash
python3 converter.py
```

## Usage examples

Convert a number from base 16 to base 10
```console 
Converter

Enter notation from (or 0 to exit): 16
Enter notation to (or 0 to exit): 10

Enter value: 2A

Result: 42
```

Convert a decimal fractional number to binary
```console
Converter

Enter notation from (or 0 to exit): 10
Enter notation to (or 0 to exit): 12

Enter value: 49.32

Result: 110001.010100011110
```

## Project structure
```console
.
├── converter.py   # main program code
├── utils.py       # helper utilities (e.g., clear terminal)
├── tests/         # unit tests
└── README.md      # project documentation
```

## Main functions
- conversion_to_decimal(value: str, notation: int) -> str
  Converts a number from any numberal system to decimal.
- conversion_from_decimal(value: str, notation: int) -> str
  Converts a decimal number to the target numberal system.
- conversion(input_value: str, notation_from: int, notation_to: int) -> str
  Converts a number from one numeral system to another.
- validate_value(value: str, notation: int) -> bool
  Validates if a number is correct in the given numeral system.
- is_fraction(value: str) -> bool
  Checks if a number has a fractional part.

## Limitations
- Maximum fractional precision - **12 digits**.
- Supported numeral systems - **from 2 to 36**.

## Testing
The project includes unit tests (using **unittest**).

Run tests:
```bash
python3 test_converter.py
```