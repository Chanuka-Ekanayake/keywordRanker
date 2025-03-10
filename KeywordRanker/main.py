#------------------------------------------------------------------------------------------------------------------------------

#                                                 -- MoReach: Smarter SEO, Bigger Impact--

# MoReach Phase 1
# Development Start date: 2024-11-25
# Main goal - Keyword ranker by city and City ranker by keyword
# Sub goal - Content Extractor

#------------------------------------------------------------------------------------------------------------------------------


#Importing Libraries
import keywordR



def inputKeyword():
    keyword = input("\nEnter the keyword: ").strip()
    return keyword.split(" ")


def inputRegion():
    region = input("\nEnter the region: ").strip()


def int_inputValidation():
    while True:
        try:
            choice = int(input("\nEnter your choice: ").strip())
            if type(choice) == int:
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError:
            print("\nInvalid choice. Please try again.")
    return choice



def main():
    print("-- MoReach Phase 1 --".center(120))

    print("\n1. Keyword ranker by city")
    print("2. City ranker by keyword")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        keywordR.keywordRanker(inputKeyword(), inputRegion())


if __name__ == "__main__":
    main()