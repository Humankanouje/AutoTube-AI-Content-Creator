from flask import Flask, request, render_template_string, send_from_directory, redirect, url_for
import subprocess
import os
import time

app = Flask(__name__)

FORM_HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AutoTube - Generate Video</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-6">
  <div class="bg-white shadow-xl rounded-xl p-8 w-full max-w-xl">
    <h1 class="text-2xl font-bold mb-6 text-center text-blue-700">AutoTube - Generate Short Video</h1>
    
    <form method="post" class="flex flex-col gap-4">
      <input name="topic" placeholder="Enter a topic..." required 
             class="border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-400" />
      <button type="submit"
              class="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-lg transition">
        🎬 Generate Video
      </button>
    </form>

    {% if topic %}
      <div class="mt-6 text-center text-green-700 font-medium">
        ✅ Topic received: <strong>{{ topic }}</strong>
      </div>
    {% endif %}

    
      <div class="mt-10 border border-gray-300 rounded-lg p-4 bg-gray-50 shadow-inner">
        <h2 class="text-xl font-semibold text-gray-800 mb-3 text-center">🎥 Video Player</h2>
        <video controls autoplay muted class="w-full rounded shadow-md">
          <source src="{{ url_for('serve_video') }}?t={{ timestamp }}" type="video/mp4">
          Your browser does not support the video tag.
        </video>
      </div>
  </div>
</body>
</html> 
"""

@app.route("/", methods=["GET", "POST"])
def index():
    topic = None
    video_path = os.path.join("output", "shorts.mp4")
    video_exists = os.path.exists(video_path)
    timestamp = int(os.path.getmtime(video_path)) if video_exists else 0

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        if topic:
            print(f"Topic received: {topic}")
            try:
                subprocess.Popen(["python", "launcher.py", topic], shell=False)
            except Exception as e:
                print("Error launching script:", e)
        # Redirect to clear form data on refresh
        return redirect(url_for('index'))

    return render_template_string(FORM_HTML, topic=topic, video_exists=video_exists, timestamp=timestamp)


from flask import send_file

@app.route("/video")
def serve_video():
    # Full path to the actual file
    video_path = os.path.join(os.getcwd(), "output", "short.mp4")

    if os.path.exists(video_path):
        return send_file(video_path, mimetype="video/mp4")
    else:
        return "Video not found", 404


if __name__ == "__main__":
    app.run(debug=True)
