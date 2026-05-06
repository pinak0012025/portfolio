from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "AI Recruiter Platform",
        "client": "Singapore Client",
        "type": "AI Automation SaaS",
        "desc": "AI-powered recruitment workflow platform for resume screening, candidate ranking, recruiter automation and interview pipeline optimization.",
        "stack": ["Python", "Flask/FastAPI", "AI APIs", "Docker", "CI/CD", "Cloud"],
        "impact": "Automated candidate shortlisting and reduced manual recruiter effort."
    },
    {
        "title": "Strategic Food Reserve Vault",
        "client": "USA Client",
        "type": "Full-Stack SaaS Platform",
        "desc": "Food reserve planning and price-lock SaaS platform with user vault, product catalog, reserve planner, authentication and scalable cloud deployment.",
        "stack": ["Next.js", "Supabase", "Stripe-ready", "Vercel", "Docker", "Cloud"],
        "impact": "Built SaaS-ready foundation for long-term food reservation and emergency preparedness."
    },
    {
        "title": "Customized Designing Platform",
        "client": "USA Client",
        "type": "Design Automation Platform",
        "desc": "Custom design workflow platform with dynamic layouts, user customization, interactive UI and full-stack delivery model.",
        "stack": ["React", "Python", "Flask", "JavaScript", "Docker", "Cloud"],
        "impact": "Enabled dynamic design customization for end users."
    }
]

skills = {
    "Full Stack": ["React", "Next.js", "JavaScript", "Python", "Flask", "FastAPI", "REST APIs"],
    "DevOps": ["Docker", "Kubernetes", "Terraform", "Git", "GitHub Actions", "Jenkins", "Tekton", "ArgoCD"],
    "Cloud": ["AWS", "GCP", "Vercel", "Linux", "Nginx", "Cloud Deployment"],
    "Monitoring": ["Prometheus", "Grafana", "Datadog", "Dynatrace", "Logs", "Metrics", "Tracing"]
}

@app.route("/")
def home():
    return render_template("index.html", projects=projects, skills=skills)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321, debug=True)
