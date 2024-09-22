
# Class definiálása:
class ArrayHelper:
    def findSecondLargestNumber(self, numbers):

        # Megnézzük, hogy kettőnél több számot adtak-e meg (legalább):
        numbers_length = len(numbers)
        if numbers_length == 0 or numbers_length == 1:
            raise ValueError("Please give valid numbers as a param. #1")

        # Megnézzük, hogy a megadott számok különbözőek-e (azonos számok esetében nincs második legnagyobb szám):
        unique_numbers_length = len(set(numbers))
        if unique_numbers_length == 1:
            raise ValueError("Please give valid numbers as a param. #2")

        # Rendezzük a számokat csökkenő sorrendbe (érték szerint)
        sorted_numbers = sorted(numbers, reverse=True)

        # Visszaadjuk a tömb második elemét (Most már biztos, hogy lesz 2. elem a tömbben)
        return sorted_numbers[1]

numbers = [1,2,3,4,1,2,-1,23,49,101,11]
array_helper = ArrayHelper()
second_largest_number = array_helper.findSecondLargestNumber(numbers)
print("second largest number is: " + str(second_largest_number))
