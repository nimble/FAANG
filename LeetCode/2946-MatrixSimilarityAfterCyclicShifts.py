class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # Make a copy to compare with afterwards
        mats = deepcopy(mat)

        # Perform rightArrayRotation on Array
        def rightArrayRotation(num_array, shift):
            for i in range(0,shift):
                temp = num_array[len(num_array) - 1]
                for j in range(len(num_array) - 1, 0 , -1):
                    num_array[j] = num_array[j-1]
                num_array[0] = temp
            
            # return num_array
        
        # Perform leftArrayRotation on Array
        def leftArrayRotation(num_array, shift):
            for i in range(0, shift):
                temp = num_array[0]
                for j in range(0, len(num_array) - 1):
                    num_array[j] = num_array[j+1]
                num_array[len(num_array) - 1] = temp
            
            # return num_array
        
        # Keep index and Value 
        for i,j in enumerate(mat):
            if(i % 2 == 0):
                leftArrayRotation(j, k)
            else:
                # We will do a shift right rotation.
                rightArrayRotation(j, k)

        if(mat == mats):
            return True
        else:
            return False
