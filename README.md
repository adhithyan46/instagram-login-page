# instagram-login-page
![Screenshot (152)](https://github.com/adhithyan46/instagram-login-page/assets/171124070/0814c283-71e6-4acf-95df-20bda9481aed)

This code creates a basic login page using Tkinter, a Python library for creating graphical user interfaces. Here's a description of the code:

**1.Setup the Main Window:**

A main window (root) is created with the title 'login page'.
The window size is set to 1000x600 pixels.
The background color of the window is set to white.

**2.Define Submit Function:**

A function submit() is defined to handle the login logic.
It retrieves the username and password entered by the user.
If the credentials are correct (both username and password are 'admin'), a new window (root2) titled 'feed' is created with a size of 1000x700 pixels.
If the credentials are incorrect, an error message is displayed on the login frame.

**3.Create Login Frame:**

A frame (frame) is created to hold the login form elements, placed at specific coordinates.
Labels and entry fields for username and password are added to the frame.
A 'Log in' button is created, which triggers the submit function when clicked.
Additional labels for 'or', 'Log in with Facebook', and 'Forgot Password?' are added to the frame for a realistic login page feel.

**4.Create Sign-up Frame:**

Another frame (frame2) is created to hold the sign-up prompt, placed at specific coordinates.
A label and button are added to encourage users to sign up if they don't have an account.

**5.Display an Image:**

An image is loaded from a specified file path and displayed on the main window.
![Screenshot (152)](https://github.com/adhithyan46/instagram-login-page/assets/171124070/0814c283-71e6-4acf-95df-20bda9481aed)


**6.Run the Main Loop:**

The root.mainloop() method is called to start the Tkinter event loop, making the window and its contents interactive.
