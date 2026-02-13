import os

os.makedirs("dist", exist_ok=True)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Python CI/CD</title>
</head>
<body>
    <h1>Deployed with GitHub Actions 🚀</h1>
    <p>If you can see this page, your CD pipeline works.</p>
</body>
</html>
"""

with open("dist/index.html", "w") as f:
    f.write(html_content)

print("Website generated in dist/index.html")

