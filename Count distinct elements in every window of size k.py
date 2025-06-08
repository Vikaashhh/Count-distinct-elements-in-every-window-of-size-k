class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        freq = {}  # using regular dictionary
        result = []

        # Build frequency map for the first window
        for i in range(k):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1

        result.append(len(freq))  # Add count after first window

        # Slide the window
        for i in range(k, n):
            out_elem = arr[i - k]
            in_elem = arr[i]

            # Remove the element going out of the window
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]

            # Add the new element
            if in_elem in freq:
                freq[in_elem] += 1
            else:
                freq[in_elem] = 1

            result.append(len(freq))

        return result
