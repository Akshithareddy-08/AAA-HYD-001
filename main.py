import my_programs

def main():
    while True:
        print("\nFUNCTION MENU")
        print("1. Swap Two Numbers")
        print("2. GCD of Two Numbers")
        print("3. Custom Sorting")
        print("4. Reverse a Number")
        print("5. Sum of Digits")
        print("6. Count Vowels in a String")
        print("7. Count Words in a Sentence")
        print("8. Convert String to Title Case")
        print("9. Check for Palindrome")
        print("10. Check for Prime Number")
        print("11. Find Factorial of a Number")
        print("12. Convert Decimal to Binary")
        print("13. Find the Largest of Three Numbers")
        print("14. Remove Duplicates from a List")
        print("0. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting program...")
            break
        elif choice == 1: my_programs.swap_numbers()
        elif choice == 2: my_programs.gcd_numbers()
        elif choice == 3: my_programs.custom_sort()
        elif choice == 4: my_programs.reverse_number()
        elif choice == 5: my_programs.sum_of_digits()
        elif choice == 6: my_programs.count_vowels()
        elif choice == 7: my_programs.count_words()
        elif choice == 8: my_programs.title_case()
        elif choice == 9: my_programs.palindrome_check()
        elif choice == 10: my_programs.prime_check()
        elif choice == 11: my_programs.factorial()
        elif choice == 12: my_programs.decimal_to_binary()
        elif choice == 13: my_programs.largest_of_three()
        elif choice == 14: my_programs.remove_duplicates()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
