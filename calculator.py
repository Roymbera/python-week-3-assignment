def calculate_discount(price, discount_percent):
   
    if discount_percent >= 20:
        # Calculate the discount 
        discount_amount = (discount_percent / 100) * price
        # Final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        
        return price

def main():
    # enter the original price
    original_price = float(input("Enter the original price of the item: "))
    # enter the discount percentage
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
   
    print(f"The final price after applying the discount is: ksh{final_price:.2f}")


if __name__ == "__main__":
    main() 
