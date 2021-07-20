from flask import Flask, render_template, request, session, redirect
from story import write_story
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdeffehhhfhjjdshlkshjbas!'
@app.route('/')
def my_form():
    return render_template('index.html')   

@app.route('/', methods=['GET', 'POST'])
  
def generate_story():                            
    if request.method=='POST':
       
        story_input = request.form['storyInput']  
        if story_input==True:
             session.clear()
        session_story = session.get('session_story')     #for fetching the session data
        if session_story == None: 
            story_prompt=f'You are a kids story generator. Your task is to generate rich, detailed, thrilling and exciting stories for kids. Generate a story about {story_input}. The story about {story_input} should be very interesting to the reader.'
            session_story = write_story(story_prompt)                 
        else:
            session_story = write_story(session_story) 
        return render_template("index.html",session_story = session_story)


# Function to clear the session data
@app.route('/delete')
def delete():
    session.clear()            # clear the session
    return redirect('/')       # redirect to the main page

if __name__ == "__main__":       # main function 
    app.run(debug=True)