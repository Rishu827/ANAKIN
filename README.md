# ANAKIN

1. It was required to get the latitude and longitude, so I have written a pythin script that performs this task.

2. Just run the following command - 

    ## python coordinatesFinder.py filename filepath
        filename : required : name of html/text file that contains the source code of the webpage
        filepath : optional : path to the file, if not then it will look for the file in existing directory

3. For sample input, I have h1.html file here. I have extracted its source code using selenium(python). Since it was not required for the task, so have not pushed it on the repository. If required, I can push the selenium logic too(python/JS).

4. Further, if we want we can use multu-threading in our cooridnateFinder. Since it is taking small time for this test case, so havenot used that approach as of now.

5. For the sample input, I was able to find **"Total of 80 Coordinates found in 0.0019989013671875 seconds"**
