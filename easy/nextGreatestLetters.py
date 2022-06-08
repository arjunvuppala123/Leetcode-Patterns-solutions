class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        myNums = [int(ord(letter)) for letter in letters]
        target = int(ord(target))
        for num in myNums:
            if target < num:
                return chr(num)
        return chr(myNums[0])