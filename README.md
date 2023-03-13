<div>
  <p>To run the project locally</p>
  <ol>
    <li>Clone the project</li>
    <ul>
      <li>git clone [repo url]</li>
    </ul>
    <li>Change directory to DjangoChatRooms</li>
    <ul>
      <li>cd DjangoChatRooms</li>
    </ul>
    <li>Create a virtual environment</li>
    <ul>
      <li>python3 -m venv venv</li>
    </ul>
    <li>Activate the virtual environment</li>
    <ul>
      <li>for MAC/Linux: <code>source venv/bin/activate</code></li>
      <li>for Windows: <code>venv\Scripts\activate.bat</code></li>
    </ul>
    <li>Install the requirements</li>
    <ul>
      <li><code>pip install -r requirements.txt</code></li>
    </ul>
    <li>Migrate the database</li>
    <ul>
      <li><code>cd app</code></li>
      <li><code>python manage.py makemigrations</code></li>
      <li><code>python manage.py migrate</code></li>
    </ul>
    <li>Run the server</li>
    <ul>
      <li><code>python manage.py runserver</code></li>
    </ul>
    <li>Open the browser and go to <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a> to see the project</li>
  </ol>
</div>
<style>
  div {
    background-color: #f2f2f2;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-family: Arial, sans-serif;
  }
  p {
    font-size: 1.2em;
    font-weight: bold;
  }
  ul, ol {
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 30px;
  }
  a {
    color: #4CAF50;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
</style>
