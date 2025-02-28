from flask import Flask, request, render_template
from pickledb import PickleDB
from utils import shorten_url

app = Flask(__name__)
db = PickleDB('data.db')

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == 'POST':
        if "shorten" in request.form:
            # Get the URL inputted in the form
            original_url = request.form['url'].strip()

            # Shorten the URL and save it to the database
            short_url = shorten_url(original_url)
            db[short_url] = original_url
            db.save()

            if short_url:
                return f"""
                <p>Your shortened URL is: <a href='/{short_url}'>{short_url}</a></p>
                <a href='/'><button>Back to Form</button></a>
                """
            else:
                return f"""
                <p>Error generating short URL for <span style='color: red;'>{original_url}</span>. 
                Try inputting a valid URL.</a></p> <a href='/'><button>Back to Form</button></a>
                """
        elif "retrieve" in request.form:
            # Get the URL inputted in the form
            short_url = request.form["short_url"].strip()

            # Find the short URL in the database
            original_url = db[short_url]

            if original_url:
                return f"""
                <p>The original URL for the Short URL <span style='color: green;'>{short_url}
                </span> is: <a href='/{original_url}'>{original_url}</a></p>
                <a href='/'><button>Back to Form</button></a>
                """
            else:
                return f"""
                <p>Short URL <span style='color: red;'>{short_url}</span> not found.</p>
                <a href='/'><button>Back to Form</button></a>
                """    
    return render_template('form.html')
    
if __name__ == "__main__":
    app.run()