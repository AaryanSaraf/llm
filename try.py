import os

server_js = """\
const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
"""
index_html = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Express Boilerplate</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin-top: 100px;
    }
  </style>
</head>
<body>
  <h1>Hello from Express + HTML!</h1>
  <p>This file was generated with Python!</p>
</body>
</html>
"""


def create_dir(project_name):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
    elif not os.path.isdir(project_name):
        raise Exception(f"{project_name} exists and is not a directory.")
    os.chdir(f"{project_name}")
    os.makedirs("client", exist_ok=True)
    os.makedirs("server", exist_ok=True)

def boiler():
    with open(os.path.join("client","index.html"), "w") as file:
        file.write(index_html)
    with open(os.path.join("server/server.js"), "w") as file:
        file.write(server_js)  


project_name= input("Enter project name: ")
try:
    create_dir(project_name)
    boiler()
    print("Success")
except Exception as e:
    print(f"Error: {e}")