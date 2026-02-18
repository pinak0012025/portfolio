from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Centralized data for easy updates
    profile = {
        "name": "Pinak Das",
        "title": "DevOps & Automation Engineer",
        "email": "pinak3151153@outlook.com",
        "linkedin": "https://www.linkedin.com/in/pinak-pani-das-3160b062/",
        "github": "https://github.com/pinak0012025",
        "total_exp": "12+",
        "devops_exp": "7+",
        "cloud_platforms": ["AWS", "GCP"],
        "tools": ["Jenkins", "GitHub Actions", "ArgoCD", "Docker", "Kubernetes", "Terraform", "Ansible"]
    }
    return render_template('index.html', p=profile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)