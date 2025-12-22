import cv2
import os

# 1. Define the filename
filename = "universe.png"

# 2. Load the image
picture = cv2.imread(filename)

# 3. Check if the image loaded successfully
if picture is None:
    print(f"Error: Could not load '{filename}'.")
    print("Make sure the file is in this directory:", os.getcwd())
else:
    # 4. Show the image
    cv2.imshow("winName : universe", picture)

    # 5. Wait indefinitely for a key press
    cv2.waitKey(0)
    
    # 6. Clean up windows (Important for preventing hangs)
    cv2.destroyAllWindows()