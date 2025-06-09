from parser import parse_test_case

def main():
    print("Starting script...")  # Debug line
    
    with open(r"G:\nlp project\data\example_cases.txt", "r") as f:
        descriptions = [line.strip() for line in f if line.strip()]

    print("Descriptions loaded:", descriptions)  # Debug line

    for idx, desc in enumerate(descriptions, start=1):
        structured_data = parse_test_case(desc)
        print(f"\nTest Case {idx}:")
        for key, value in structured_data.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    main()