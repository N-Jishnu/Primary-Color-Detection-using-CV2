# Python code for Multiple Color Detection 
import numpy as np 
import cv2 

webcam = cv2.VideoCapture(0) 


while(True): 
	
        _, imageFrame = webcam.read() 

        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	# Set range for red color  
        r_lower = np.array([136, 87, 111], np.uint8) 
        r_upper = np.array([180, 255, 255], np.uint8) 
        r_mask = cv2.inRange(hsvFrame, r_lower, r_upper)

	# Set range for green color
        g_lower = np.array([25, 52, 72], np.uint8) 
        g_upper = np.array([102, 255, 255], np.uint8) 
        g_mask = cv2.inRange(hsvFrame, g_lower, g_upper) 

	# Set range for blue color  
        b_lower = np.array([94, 80, 2], np.uint8) 
        b_upper = np.array([120, 255, 255], np.uint8) 
        b_mask = cv2.inRange(hsvFrame, b_lower, b_upper) 
s
        kernel = np.ones((5, 5), "uint8") 

	# For red color 
        r_mask = cv2.dilate(r_mask, kernel) 
        res_red = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = r_mask) 
	
	# For green color 
        g_mask = cv2.dilate(g_mask, kernel) 
        res_green = cv2.bitwise_and(imageFrame, imageFrame, 
								mask = g_mask) 
	
	# For blue color 
        b_mask = cv2.dilate(b_mask, kernel) 
        res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = b_mask) 


	# Creating contour to track red color 
        contours, hierarchy = cv2.findContours(r_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 300): 
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 0, 255), 2) 
			
                cv2.putText(imageFrame, "Red Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
						(0, 0, 255))	 

	# Creating contour to track green color 
        contours, hierarchy = cv2.findContours(g_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 300): 
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 255, 0), 2) 
			
                cv2.putText(imageFrame, "Green Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 255, 0)) 

	# Creating contour to track blue color 
        contours, hierarchy = cv2.findContours(b_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
        for pic, contour in enumerate(contours): 
            area = cv2.contourArea(contour) 
            if(area > 300): 
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(255, 0, 0), 2) 
			
                cv2.putText(imageFrame, "Blue Colour", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 0, 0)) 

        cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 
        if cv2.waitKey(10) & 0xFF == ord('q'): 
            cv2.VideoCapture(0) 
            cv2.destroyAllWindows() 
            break
