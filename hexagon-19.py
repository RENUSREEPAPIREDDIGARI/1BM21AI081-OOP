def calculate_hexagon_area(length):
    if length <= 0:
        return "Length should be a positive number."
    area = (3 * (3 ** 0.5) * (length ** 2)) / 2
    return area
# Example usage
side_length = 5
hexagon_area = calculate_hexagon_area(side_length)
print(f"The area of a regular hexagon with side length {side_length} is: {hexagon_area}")


      
