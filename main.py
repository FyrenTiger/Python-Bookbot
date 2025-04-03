def main():
    import sys
    from stats import get_num_words
    from stats import char_breakdown
    from stats import sort_dictionary

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    count=get_num_words(filepath)
    raw_char_count=char_breakdown(filepath)
    char_unsorted_dictionary=[]
    
    for char in raw_char_count:
        if char.isalpha():
            char_unsorted_dictionary.append({"name": char, "count": raw_char_count[char]})

    sorted_dictionary = sort_dictionary(char_unsorted_dictionary)

    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print ("Found",count,"total words")
    print ("--------- Character Count -------")
    
    for chars in sorted_dictionary:
        print(f"{chars["name"]}: {chars["count"]}")


##    for chars in sorted_dictionary:
  ##      print (sorted_dictionary(char))
    
    

if __name__ == "__main__":
    main()
