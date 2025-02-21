def main():
    problem = input("Enter your problem to solve: ")
    from openai_helpers import get_solution, create_image, perform_search, additional_feature  # import helper functions
    
    solution = get_solution(problem)
    image_url = create_image(problem)
    search_results = perform_search(problem)
    extra = additional_feature(problem)
    
    print("Solution:", solution)
    print("Image URL:", image_url)
    print("Search Results:", search_results)
    print("Extra Feature:", extra)

if __name__ == "__main__":
    main()
