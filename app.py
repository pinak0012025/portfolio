from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Pinak Das",
    "role": "AI Systems & Full-Stack DevOps Engineer",
    "headline": "I architect SaaS platforms, AI automation workflows, cloud infrastructure, CI/CD pipelines and production-ready DevOps systems.",
    "location": "India",
    "email": "pinakm007@gmail.com",
    "phone": "+91 9844988752",
    "linkedin": "https://www.linkedin.com/in/pinak-pani-das-3160b062/",
    "github": "https://github.com/pinak0012025",
}

metrics = [
    {"value": "12+", "label": "Years in IT", "detail": "Enterprise engineering background"},
    {"value": "7+", "label": "Cloud & DevOps", "detail": "CI/CD, Kubernetes, IaC"},
    {"value": "3+", "label": "SaaS Projects", "detail": "Client-facing platforms"},
    {"value": "24/7", "label": "Deployment Mindset", "detail": "Cloud-first delivery"},
]

projects = [
    {
        "title": "Strategic Food Reserve Vault",
        "client": "USA Client",
        "type": "Full-Stack SaaS Platform",
        "summary": "A food reserve planning and price-lock SaaS platform with user vault, product catalog, reserve planner, authentication and scalable cloud deployment.",
        "story": "Built the SaaS-ready foundation for a reserve-commerce platform where users can plan emergency food reserves, lock pricing, manage vault-style carts and prepare for staged delivery and payment flows.",
        "stack": ["Next.js", "Supabase", "Stripe-ready", "Vercel", "Tailwind", "Cloud"],
        "impact": "Created a scalable product foundation for long-term food reservation and emergency preparedness.",
        "accent": "blue",
    },
    {
        "title": "AI Recruiter Platform",
        "client": "Singapore Client",
        "type": "AI Automation SaaS",
        "summary": "AI-powered recruitment workflow platform for resume screening, candidate ranking, recruiter automation and interview pipeline optimization.",
        "story": "Designed the automation logic for candidate intelligence, ranking flows and recruiter-side productivity improvements using AI-assisted workflows and API-ready backend architecture.",
        "stack": ["Python", "Flask/FastAPI", "AI APIs", "Docker", "CI/CD", "Cloud"],
        "impact": "Reduced manual recruiter effort through automated shortlisting and pipeline acceleration.",
        "accent": "violet",
    },
    {
        "title": "Customized Designing Platform",
        "client": "USA Client",
        "type": "Design Automation Platform",
        "summary": "Custom design workflow platform with dynamic layouts, user customization, interactive UI and full-stack delivery model.",
        "story": "Built a flexible design experience with configurable UI sections, dynamic content rendering and client-facing customization workflows.",
        "stack": ["React", "Python", "Flask", "JavaScript", "Docker", "Cloud"],
        "impact": "Enabled dynamic design customization for end users.",
        "accent": "cyan",
    },
]

skills = {
    "Frontend Engineering": ["React", "Next.js", "JavaScript", "HTML5", "CSS3", "Tailwind", "Responsive UI"],
    "Backend Engineering": ["Python", "Flask", "FastAPI", "REST APIs", "Auth", "Microservices"],
    "DevOps & CI/CD": ["Docker", "Kubernetes", "Terraform", "Jenkins", "GitHub Actions", "Tekton", "ArgoCD"],
    "Cloud & Monitoring": ["AWS", "GCP", "Vercel", "Linux", "Nginx", "Grafana", "Dynatrace", "Datadog"],
}

services = [
    {"title": "SaaS Platform Development", "text": "Product-ready frontend, backend APIs, auth, dashboards and deployment pipelines."},
    {"title": "DevOps Automation", "text": "CI/CD pipelines, Dockerization, Kubernetes deployment and release automation."},
    {"title": "Cloud Infrastructure", "text": "AWS/GCP/Vercel deployment strategy with scalable architecture and environment management."},
    {"title": "AI Workflow Automation", "text": "AI-assisted screening, ranking, document intelligence and operational workflow automation."},
]

architecture = [
    {"layer": "Frontend", "tools": "React / Next.js / Jinja", "desc": "Premium product UI and responsive interfaces"},
    {"layer": "API Layer", "tools": "Flask / FastAPI", "desc": "Business logic, services and integrations"},
    {"layer": "Auth & Data", "tools": "Supabase / SQL", "desc": "User sessions, profiles and structured data"},
    {"layer": "CI/CD", "tools": "GitHub Actions / Jenkins / Tekton", "desc": "Automated build, test and release flows"},
    {"layer": "Runtime", "tools": "Docker / Kubernetes", "desc": "Containerized apps and scalable workloads"},
    {"layer": "Observability", "tools": "Grafana / Dynatrace / Datadog", "desc": "Metrics, logs, traces and service health"},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=profile,
        metrics=metrics,
        projects=projects,
        skills=skills,
        services=services,
        architecture=architecture,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=54321, debug=True)
