import cv2
import numpy as np

# Function to detect paper or plastic
def detect_object(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper boundaries for paper color in HSV
    lower_paper = np.array([0, 0, 150])
    upper_paper = np.array([20, 255, 255])
    
    # Threshold the HSV image to get only paper color
    mask_paper = cv2.inRange(hsv, lower_paper, upper_paper)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask_paper, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding box around the detected object // every time I tried to focus the paper object to the border box it will gonna move form 
    if contours:
        # Find the largest contour
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return "Paper"
    
    return "No object detected"

def main():
    try:
        # Initialize webcam
        cap = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Unable to capture frame.")
                break
            
            # Detect the object
            object_type = detect_object(frame)
            cv2.putText(frame, f"Detected object type: {object_type}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Display the resulting frame
            cv2.imshow('frame', frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the capture
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
