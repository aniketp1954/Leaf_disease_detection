#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from model import result_str
import pickle
import numpy as np

   
app = Flask(__name__)

 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','JPG'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('image.html')


 
@app.route('/pred', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        str=os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        x=str.replace(os.sep, '/')
        pred=result_str(x)
        
        return render_template('image.html', filename=filename, prediction = pred)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    

    
        
    

if __name__ == "__main__":
    app.run(debug = True)




# from flask import Flask, flash, request, redirect, url_for, render_template
# import os
# from werkzeug.utils import secure_filename
# from model import result_str  # Assuming result_str processes the image and returns a prediction

# app = Flask(__name__)

# # Set up upload folder and allowed extensions
# UPLOAD_FOLDER = 'static/uploads/'
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'JPG'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit for file upload
# app.secret_key = "secret key"  # For flashing messages


# def allowed_file(filename):
#     """Check if the file is allowed based on its extension."""
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/')
# def home():
#     return render_template('image.html')


# @app.route('/pred', methods=['POST'])
# def upload_image():
#     """Handle the image upload and prediction."""
#     print("POST request received")  # Debugging line to check if POST is triggered
    
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
    
#     file = request.files['file']
    
#     if file.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
    
#     if file and allowed_file(file.filename):
#         # Save the uploaded image file
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         # Get the absolute path for the uploaded file
#         img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         print(f"File saved to: {img_path}")  # Debugging line to confirm file path

#         # Call the prediction function (assuming it processes the image and returns a prediction)
#         pred = result_str(img_path)
#         print(f"Prediction result: {pred}")  # Debugging line to print the prediction

#         # Return the result with the uploaded image and prediction
#         return render_template('image.html', filename=filename, prediction=pred)
#     else:
#         flash('Allowed image types are - png, jpg, jpeg, gif')
#         return redirect(request.url)


# if __name__ == "__main__":
#     app.run(debug=True)
